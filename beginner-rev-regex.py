#Author : Muhammad Handry Wahyudi
#Date : 10-08-2016
#Filename : beginner-search-regex.py 

#!/usr/bin/python 
import re
hand = open('data/mbox-short.txt')

for line in hand:
	line = line.rstrip()
	x = re.findall('^Details:.*rev=([0-9]+)', line)
	if len(x) > 0:
		print x

# Output
# ['39745']
# ['39744']
# ['39743']
# ['39742']