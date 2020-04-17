# Name : Muhammad Handry Wahyudi
# Date : 28 Juni 2016
# filename : beginner-rps.py
# RPS (Rock, Paper, Scissors)

#!/usr/bin/python

import random

user = raw_input("Choose your weapon (Choose rock, paper or scissors): ")
comp = random.choice(['rock', 'paper', 'scissors'])
user = user.lower()

print 'the user (you) chose', user
print 'the comp (I) chose', comp

if user == "rock":
  if comp == "rock":
    print "Ha! I really Chose", comp,'-- We are Tie'
  elif comp == "paper":
    print "Ha! I really Chose", comp,'-- I WIN'
  elif comp == "scissors":
    print "Ha! I really Chose", comp,'-- I Lose'
elif user == "paper":
  if comp == "rock":
    print "Ha! I really Chose", comp,'-- I Lose'
  elif comp == "paper":
    print "Ha! I really Chose", comp,'-- We are Tie'
  elif comp == "scissors":
    print "Ha! I really Chose", comp,'-- I WIN'
elif user == "scissors":
  if comp == "rock":
    print "Ha! I really Chose", comp,'-- I WIN'
  elif comp == "paper":
    print "Ha! I really Chose", comp,'-- I Lose'
  elif comp == "scissors":
    print "Ha! I really Chose", comp,'-- We are Tie'
