#Author : Muhammad Handry Wahyudi
#Date : 11-07-2016
#Filename : beginner-even-odd.py
#This program provides a different output between even and odd numbers

#!/usr/bin/python

def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print 'It is even number'
        return result
    elif number % 2 == 1:
        result = 3 * number + 1
        print 'It is odd number'
        return result

inputNumber = raw_input('Input your number : ')
try:
    inputNumber = int(inputNumber)
    print collatz(inputNumber)
except:
    print 'Error : Input must be integer'


