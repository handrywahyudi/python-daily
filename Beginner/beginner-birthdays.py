#Author : Muhammad Handry Wahyudi
#Date : 18-07-2016
#Filename : beginner-birthdays.py

birthdays = {'handry' : '14 november 1989', 'wahyudi' : '12 juli 1990', 'hendrik' : '9 agustus 1987', 'linda' : '4 mei 1992',
             'maya' : '4 april 1992'}

while True:
    name = raw_input('Input Name ? ')
    if name == '':
        break

    if name in birthdays:
        print birthdays[name], 'is the birthdays of',  name
    else:
        print 'I dont have birthday information of', name
        bday = raw_input('What is their birthday ? ')
        birthdays[name] = bday
        print 'Birthday database updated.'
        
