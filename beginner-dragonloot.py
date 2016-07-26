#Author : Muhammad Handry Wahyudi
#Date : 25-07-2016
#Filename : beginner-dragonloot.py

#!/usr/bin/python

dragonLoot = ['gold coin', 'dagger', 'ruby', 'ruby', 'gold coin', 'gold coin', 'ruby', 'dagger', 'bomb']
inv = {'gold coin' : 100, 'arrow' : 3, 'ruby' : 0}

def addToInventory(inventory, addItems):
    count = {}
    for item in addItems:
        count.setdefault(item, 0)
        count[item] = count[item] + 1

    for item in count:
        inventory[item] = inventory.get(item, 0) + count[item]
    
    #print count
    #print inventory
    return inventory
        
print addToInventory(inv, dragonLoot)


