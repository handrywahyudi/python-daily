#Author : Muhammad Handry Wahyudi
#Date : 09-07-2016
#Filename : beginner-valid-pass.py
#This program ask your name and your password

#!/usr/bin/python

while True:
  name = raw_input("Who are you ? ")
  if name != "handry":
    print "i'm fine, thanks."
    continue
  else:
    print "Hello handry."
    password = raw_input("What is your password ? (it is a fish.) ")
    if password != "lele":
      continue
    break

print "Access Granted"
