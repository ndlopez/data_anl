#building functions in Python
test_list=[1,2,3]
print(len(test_list))
length=0
for i in test_list:
    length+=1
print(length)
'''def func():
    i=3
    return i
print(func())'''
def func(v):
    i=v+3
    return i
print(func(5))
import random
print(random.random())
print('1. Random number between -1 and 10:',random.randint(-10,10))
'''import my_module #my_module.py exists in the same dir as this code
my_module.func(3) # func() is defined in my_module.py
import importlib
importlib.reload(my_module)'''
from random import *
print('2. Random number between -1 and 10:',randint(-1,10))
import random as r
print('3. Random number between -10 and 0:',r.randint(-10,0))
