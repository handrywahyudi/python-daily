#Author : Muhammad Handry Wahyudi
#Date : 11-07-2016
#Filename : beginner-magic8ball.py
#This program that returns a different string depending on what number it is passed an argument

#!/usr/bin/python

import random

def getAnswer(number):
    if number == 1:
        return 'It is certain'
    elif number == 2:
        return 'It is decidely so'
    elif number == 3:
        return 'yes'
    elif number == 4:
        return 'Reply hazy try again'
    elif number == 5:
        return 'Ask again later'
    elif number == 6:
        return 'Concetrate and ask again'
    elif number == 7:
        return 'My reply is no'
    elif number == 8:
        return 'Outlook not so good'
    elif number == 9:
        return 'very doubtful'

number = random.randint(1, 9)
result = getAnswer(number)
print result
