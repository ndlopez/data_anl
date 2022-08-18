#washizu-san and niwa-san
import datetime
date_a=datetime.date.today()
date_b=datetime.date(2016,3,25)
life=date_a-date_b
#print(life)
#print(life.days)
hoy=datetime.datetime.now()
print('Son las...',hoy.hour,':',hoy.minute)
'''list1=[0,1,2,3,4,'test'] list2=[0.2,1.3,3.141592654]
print(list2) list1.append(6) list1.insert(2,5)
print(list1.pop(2)) print(list1)
list1.remove('test') print(list1)
print(list1+list2) list1.extend(list2) print(list1)
list3=[0,1,1,2,3,5,8,13,21,34,55]
print(list3[0:3])
#sorting lists
list4=[4,2,3,0,-3,1] print('List4:',list4)
list4.sort() print('List4 sorted',list4)
list4.reverse() print('List4 reversed',list4)
list_os=['Wind','mac','linux','Unix']
list_os.sort() print('OS list sorted',list_os)
newl=[] print(newl)
newl.append('apple') newl.append('orange')
print(newl) countryl={1:'US',39:'Italia',81:'Japan',591:'Bolivia'}
countryl[86]='China' print(countryl)'''
import random
def mylist(itemes):   # numb=1
    lon=len(itemes)
    #for i in range(0,numb):
    ran=random.randint(0,lon-1)
    return ran #newlist

us_key=('q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',';',':',']','z','x','c','v','b','n','m',',','.','/','+','1','2','3','4','5','6','7','8','9','0','-','~')
jp_key=('ta','te','i','su','ka','n','na','ni','ra','se','chi','to','shi','ha','ki','ku','ma','no','ri','re','ke','mu','tsu','sa','so','hi','ko','mi','mo','ne','ru','me','ro','nu','fu','a','u','e','o','ya','yu','yo','wa','ho','he')
kus=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
knum=[0,1,2,3,4,5,6,7,8,9] #int vector
ksym=('!','[','@','#','{','.','$','}','%',']','(',')','&','+','=')
us=len(kus)#jp=len(kjp)

UU=[]#empty vector for uppercase
for i in range(us):
    cap=kus[i].upper() #converting to uppercase
    #print(cap)
    UU.append(cap) #filling UU with capital letters
UU.reverse()#print(UU) #Ulen=len(UU) 
pwdd=[] #password string vector
my_len=int(input('Length of the passphrase:'))
for i in range(3):    #rj=random.randint(0,jp-1) #pwdd.append(kjp[rj]) #0
    ru=mylist(kus)
    rn=mylist(knum)
    rs=mylist(ksym)
    rcap=mylist(UU)
    #pwdd.insert(i,mylist(kus))#pwdd.insert(1,kjp[rj])
    pwdd.append(kus[ru]) #1
    pwdd.append(UU[rcap])#4
    pwdd.append(str(knum[rn])) #2 str(numbers)
    pwdd.append(ksym[rs])#3
    #12 chars on pwdd list
random.shuffle(pwdd)
print('printed elms ',pwdd)#print(mine.count('a'))
mine=str(' ') #cat empty-space string
for j in range(my_len):
    mine+=pwdd[j]
print('Pass length:',len(mine)-1,', Your pass:',mine)
#print('LongPass ',mine)#print(mine.count('a'))
mine=str(' ')
aux=0#Re-arranging...??!
for j in range(my_len):
    k=random.randint(0,len(pwdd)-1)
    print(aux,' : ',k)
    if aux==k:
        k=random.randint(0,len(pwdd)-1)
        aux=k
    else:
        aux=k
    mine+=pwdd[k] #cat a new passphrase

#print('Simple 5char pass:',kjp[rj],kus[ru],UU[rcap],knum[rn],ksym[rs])
##psd=pwdd[0]+pwdd[1]+str(pwdd[2])+pwdd[3]+pwdd[4] #one way
#psd=pwdd[0]+pwdd[1]+pwdd[2]+pwdd[3]+pwdd[4]
#print('Passphrase length:',len(pwdd),'cat',psd)
#print('New Passphrase(no cat):',pwdd) ##print(mine.index('0'))
print('Pass length:',len(mine)-1,', Re-arranged?:',mine)
