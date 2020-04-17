#Author : Muh Handry Wahyudi
#Date : 08-07-2016
#Filename : beginner-hello.py
#This Program Say Hello and Ask My Name

#!/usr/bin/python

print "Hello Bro, What's Your Name ?"
myName = raw_input()
print 'Hello, ' + myName
lenghtOfName = len(myName)
upperCase = myName.upper()
capital = myName.capitalize()
print 'The lenght of your name is : ' + str(lenghtOfName)
print 'The uppercase of your name is : ' + upperCase
print 'The capitalize of your name is : ' + capital

print ''

print 'How old are you ?'
myAge = raw_input()
print 'You will be ' + str(int(myAge) + 1) + ' in year'
