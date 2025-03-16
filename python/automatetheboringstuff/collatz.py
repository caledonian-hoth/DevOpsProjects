#! /usr/bin/python
import sys
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1
    else:
        print('Please input a positive integer.')


while True:
    try:
        print('Please enter a positive integer:')
        number = input()
        try:
            collatz(int(number))
        except ValueError:
            print('You need to enter a positive integer.')
    except KeyboardInterrupt:
        sys.exit()                     