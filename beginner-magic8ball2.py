#Author : Muhammad Handry Wahyudi
#Date : 13-07-2016
#Filename : beginner-magic8ball2.py

#!/usr/bin/python

import random
messages = [
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print messages[random.randint(0, len(messages) - 1)]
