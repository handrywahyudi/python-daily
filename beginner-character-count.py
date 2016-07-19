#Author : Muhammad Handry Wahyudi
#Date : 19-07-2016
#Filename : beginner-character-count.py

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print count['o']

#output
#2
