#Author : Muhammad Handry Wahyudi
#Date : 08-07-2016
#Filename : beginner-raining.py
#This program ask me if outside is raining or not

#!/usr/bin/python

import time

weather = raw_input('Is raining ? Yes or No ? ')
weather = weather.lower()

def isRaining(weather):
    if weather == 'yes' or weather == 'y':
        print 'Wait a while!!!'
        time.sleep(3)
        raining = raw_input('Is still raining ? Yes or No ? ')
        raining = raining.lower()
        if raining == 'yes' or raining == 'y':
            isRaining(raining)
        elif raining == 'no' or raining == 'n':
            print 'Go Outside!!!'        
        
if weather == 'yes' or weather == 'y':
    umbrella = raw_input('Do you have an umbrella ? Yes or No ? ')
    umbrella = umbrella.lower()
    if umbrella == 'yes' or umbrella == 'y':
        print 'Go Outside!!!'
    elif umbrella == 'no' or umbrella == 'n':
        print 'Wait a while!!!'
        time.sleep(3)
        stillRaining = raw_input('Is still raining ? Yes or No ? ')
        stillRaining = stillRaining.lower()
        if stillRaining == 'yes' or stillRaining == 'y':
            isRaining(stillRaining)
        elif stillRaining == 'no' or stillRaining == 'n':
            print 'Go Outside!!!'
elif weather == 'no' or weather == 'n':
    print 'Go Outside!!!'
        
        
