provider "aws" {
  region = var.aws_region

  # Fake creds if testing without real AWS
  access_key                  = "mock"
  secret_key                  = "mock"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
}

locals {
  name_prefix = "demo"
}

resource "aws_security_group" "shared_sg" {
  name        = "${local.name_prefix}-db-sg"
  description = "Allow EKS or app access"
  vpc_id      = var.vpc_id

  ingress {
    description = "Postgres"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = var.allowed_cidrs
  }

  ingress {
    description = "Redis"
    from_port   = 6379
    to_port     = 6379
    protocol    = "tcp"
    cidr_blocks = var.allowed_cidrs
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

module "rds_postgres" {
  source  = "terraform-aws-modules/rds/aws"
  version = "~> 6.1"

  identifier = "${local.name_prefix}-postgres"

  engine            = "postgres"
  engine_version    = "15.3"
  instance_class    = "db.t3.micro"
  allocated_storage = 20
  db_name           = "mydb"
  username          = "postgres"
  password          = var.rds_password

  vpc_security_group_ids = [aws_security_group.shared_sg.id]
  subnet_ids             = var.subnet_ids

  publicly_accessible = false
  skip_final_snapshot = true

  family = "postgres15"
}

module "redis" {
  source  = "terraform-aws-modules/elasticache/aws"
  version = "~> 4.4"

  name                 = "${local.name_prefix}-redis"
  engine               = "redis"
  engine_version       = "7.0"
  node_type            = "cache.t3.micro"
  number_cache_clusters = 1

  vpc_id                 = var.vpc_id
  subnet_ids             = var.subnet_ids
  security_group_ids     = [aws_security_group.shared_sg.id]
  apply_immediately      = true
  parameter_group_name   = "default.redis7"
}

output "rds_endpoint" {
  value = module.rds_postgres.db_instance_endpoint
}

output "redis_endpoint" {
  value = module.redis.cluster_configuration_endpoint_address
}

# variables.tf
variable "aws_region" {
  default = "us-west-2"
}

variable "vpc_id" {
  description = "VPC where RDS and Redis will be deployed"
  type        = string
}

variable "subnet_ids" {
  description = "Private subnet IDs"
  type        = list(string)
}

variable "rds_password" {
  description = "Master password for RDS"
  type        = string
  sensitive   = true
}

variable "allowed_cidrs" {
  description = "CIDRs allowed to access DB and Redis"
  type        = list(string)
  default     = ["10.0.0.0/16"]
}

# tfvars
vpc_id     = "vpc-123456"
subnet_ids = ["subnet-aaa111", "subnet-bbb222"]
rds_password = "StrongPassword123!"

