#Author : Muhammad Handry Wahyudi
#Date : 30-07-2016
#Filename : beginner-password.py

#!/usr/bin/python

import sys,pyperclip

password = {'email':'!@#$%^qwer321',
            'blog' : '!@#@#$sdrfrafsdf1234',
            'dropbox' : 'erqwr@#$@#$#e'}

if len(sys.argv) < 2:
    print 'Usage: python beginner-password.py [account] - copy account password'
    sys.exit()

account = sys.argv[1]

if account in password:
    pyperclip.copy(password[account])
    print 'Password for ' + account + ' copied to clipboard'
else:
    print 'There is no account named ' + account
