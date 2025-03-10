#!/usr/bin/python

def commacode(list):
    result = ''
    for i in range(len(list)-1):
        result += list[i] + ', '
    return result + list[-1]

#spam = ['apples', 'bananas', 'tofu', 'cats']

list = []
while True:
    print('Please enter a list item or enter nothing to stop.')
    item = input()
    if item == '':
        break
    list += [item]

try:
    print(commacode(list))  
except IndexError:
       print('You need to enter at least one item. Try again.')
