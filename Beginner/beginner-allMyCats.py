#Author : Muhammad Handry Wahyudi
#Date : 12-07-2016
#Filename : beginner-allMyCats.py

#!/usr/bin/python

cats = []

while True:
    print 'Masukkan nama kucing ke', str(len(cats)), 'Tekan enter untuk menghentikan aplikasi'
    nameOfCat = raw_input('Masukkan Nama Kucing : ')
    cats = cats + [nameOfCat]

    if nameOfCat == '':
        break

print 'Nama-nama kucing : '
for cat in cats:
    print cat
