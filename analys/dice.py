'''import datetime
dig=datetime.date(2011,7,24)
print('Digital TV available in Japan on',dig)
print(dig.year)
print(dig.month)
print(dig.day)
print(dig.weekday)
semana={'lunes':0,'martes':1,'miercoles':2,'jueves':3,'viernes':4,'sabado':5,'domingo':6}
dia=semana[6]
print(dia)'''

'''class Dice:
    face_num=6
sai=Dice()
print(sai.face_num)
import random
def shoot():
    return random.randint(1,6)
for i in range(10):
    print(shoot())
'''
import random
class Dice:
    #face_num=6
    def __init__(self,val=6):#in the shell: sai="my_module".Dice()
    #def __init__(self,val): #in the shell: sai="my_module".Dice(4)
        print('hallo!')
        self.face_num=val
    def shoot(self):
        return random.randint(1,self.face_num)
'''sai=Dice()
for i in range(6):
    print(sai.shoot())'''
