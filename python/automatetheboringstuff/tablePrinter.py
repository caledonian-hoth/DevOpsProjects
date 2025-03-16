#! /usr/bin/python
"""
Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. 
Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:

   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose
"""
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table) # This is a list that will hold the column width based on the longest item in the inner lists
    printedTable = [[] for _ in range(len(table[0]))] # I'm initializing the list that will hold the table to be printed 
    for i in range(len(table)):
        for j in range(len(table[i])):
            if colWidths[i] < len(table[i][j]): # I'm first checking for the longest column width and putting it in colWidths
                colWidths[i] = len(table[i][j])
            printedTable[j].append(table[i][j]) # Here I am building the resulting table
    for i in range(len(printedTable)):
        row = '' # I want to print the table row by row.
        for j in range(len(printedTable[i])): # I scan the table row column by column
            row += str(printedTable[i][j]).rjust(colWidths[j]+1,' ')  # I add the column value right justified to the column width and one space to separate the columns neatly
        print(row)    

printTable(tableData)