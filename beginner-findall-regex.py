#Author : Muhammad Handry Wahyudi
#Date : 03-08-2016
#Filename : beginner-findall-regex.py 

#!/usr/bin/python
import re
hand = open('data/mbox-short.txt')
for line in hand:
	line = line.rstrip()
	line = re.findall('\S+@\S+', line)
	if len(line) > 0:
		print line

# Output
# ['gopal.ramasammycook@gmail.com']
# ['source@collab.sakaiproject.org']
# ['gopal.ramasammycook@gmail.com']
# ['gopal.ramasammycook@gmail.com']
