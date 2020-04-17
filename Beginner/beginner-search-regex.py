#Author : Muhammad Handry Wahyudi
#Date : 10-08-2016
#Filename : beginner-search-regex.py 

#!/usr/bin/python 
import re
hand = open('data/mbox-short.txt')

# for line in hand:
# 	line = line.rstrip()
# 	if re.search('^X\S*: [0-9.]+', line):
# 		print line

#Searching and extracting
for line in hand:
	line = line.rstrip()
	x = re.findall('^X\S*: ([0-9.]+)', line)
	if len(x) > 0:
		print x


# output
# ['0.0000']
# ['0.7556']
# ['0.0000']