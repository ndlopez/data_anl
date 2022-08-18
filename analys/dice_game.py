import dado

num=eval(input('choose one number between 4,6,8,12,20:'))
#note! on Python3 and up use eval(input('msg'))

my_dice=dado.Dice(num)
cpu_dice=dado.Dice(num)

my_pip=my_dice.shoot()
cpu_pip=cpu_dice.shoot()
print('The dice is rolling...\n')
print('CPU:' + str(cpu_pip)+' You:'+ str(my_pip))
if my_pip>cpu_pip:
    print('congratulations! you won!!')
elif my_pip < cpu_pip:
    print('PC wins! You lose!')
else:
    print('draw')
