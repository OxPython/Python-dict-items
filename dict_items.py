'''
Created on Jul 1, 2014

@author: viejoemer
'''
############################################################
#HowTo get all the items from a dict in python?

#Creating a empty dict

d = {}

d = dict()

#Creating a dict with data

d = {
     "red":100,
     "yellow":200,
     "blue" : 300
     }

print(d)

#Get the items from a dict
items = d.items()

print(type(items))

print(items)

for key, value in items:
    print(key , value)

print(d)

print(d)
