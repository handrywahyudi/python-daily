#Author : Muhammad Handry Wahyudi
#Date : 14-07-2016
#Filename : beginner-comma-code.py

#!/usr/bin/python

def printList(fruit):
    result = ""
    for i in range(len(fruit) - 1):
        result = result + fruit[i] + ', ' 

    result = result + 'and ' + fruit[-1]
    print result

fruitList = ['apples', 'bananas', 'strawberry', 'mango', 'lemon', 'melon']
printList(fruitList)
