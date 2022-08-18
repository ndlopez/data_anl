x=1.0/3.0
print(x)
print('answer= '+str(x))
print('answer= %0.1f' % x)
#print(answer)
while True:
    height=input('altura[m]?:') #for python 3 and up
    #height=raw_input('altura[m]?:') for python 2.7 and before
    if len(height)==0:
        break
    height=float(height)
    weight=float(input('peso[kg]?:'))
    bmi=weight/pow(height,2)

    print('BMI is %0.1f' %bmi)
    if bmi<18.5:
        print('lil weight loss.')
    elif 18.5 <= bmi <25.0:
        print('hyojuntekina taikei desu')
    elif 25.0 <= bmi < 30.0:
        print('put a lil on weight')
    else:
        print('koudonohiman desu')
