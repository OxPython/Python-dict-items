'''
Created on Jul 2, 2014

@author: viejoemer

HowTo get all the items from a dict in python?

¿Cómo obtener todos los elementos de un diccionario en Python?

'''

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

#Loop the data
for key, value in items:
    print(key , value)
