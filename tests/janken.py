import random
data=['goo','choki','pa']
data_choice=random.choice(data)
print('jan-ken-po...\n')
print(data_choice)

'''import sys
a=float(sys.argv[1])
b=float(sys.argv[2])
print(a+b)'''
import sys
try:
    a=float(sys.argv[1])
    b=float(sys.argv[2])
    print(a+b)
except:
    print('Error!')
    print('Input 2 arguments!\n')
print('bye')
