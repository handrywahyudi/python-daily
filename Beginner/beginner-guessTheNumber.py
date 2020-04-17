#Author : Muhammad Handry Wahyudi
#Date : 11-07-2016
#Filename : beginner-guessTheNumber.py
#This program guess the number

#!/usr/bin/python


import random

secretNumber = random.randint(1, 20)
print 'I am thinking of number between 1 and 20.'

print 'You have 6 chance to choose'

for guessTaken in range(1, 7):
    guess = raw_input('Choose your number ? ')
    guess = int(guess)

    if guess < secretNumber:
        print 'Your guess is low'
    elif guess > secretNumber:
        print 'Your guess is high'
    else:
        break

if guess == secretNumber:
    print 'Good job! your guessed my number in', str(guessTaken), 'guesses!'
else:
    print 'Nope, The number i was thinking of was', str(secretNumber)
