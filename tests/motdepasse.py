import datetime,copy
hoy=datetime.datetime.now()
print('Son las...',hoy.hour,':',hoy.minute,':',hoy.second)
seg=[]#seg.append(hoy.minute)
if hoy.second<10:
    seg.append(hoy.second*10)
else:
    seg.append(hoy.second)
import random
def MyList(itemes,numb):   # numb=1
    newlist=[]
    #newlist=copy.copy(itemes)
    lon=len(itemes)
    for i in range(numb):
        j=random.randint(0,lon-1)
        newlist.append(itemes[j])
    #random.shuffle(newlist)
    #print(newlist)#(numb,item)   # numb+=1
    return newlist

us_key=('q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',';',':',']','z','x','c','v','b','n','m',',','.','/','+','1','2','3','4','5','6','7','8','9','0','-','~')
jp_key=('ta','te','i','su','ka','n','na','ni','ra','se','chi','to','shi','ha','ki','ku','ma','no','ri','re','ke','mu','tsu','sa','so','hi','ko','mi','mo','ne','ru','me','ro','nu','fu','a','u','e','o','ya','yu','yo','wa','ho','he')
kus=('z','x','c','v','b','n','m','a','s','d','f','g','h','j','k','l','q','w','e','r','t','y','u','i','o','p')
ksym=(']','!','@','(','#','.','}','$','%','[',')','&','+','=','-','_','{')
us=len(kus)

UU=[]#empty vector for uppercase
for i in range(us):
    cap=kus[i].upper() #converting to uppercase
    #print(cap)
    UU.append(cap) #filling UU with capital letters
#kus.reverse()#print(UU) #Ulen=len(UU)
uk=[]
uk.extend(UU)
for item in ksym+kus:
    uk.append(item)
my_len=int(input('Length of passphrase [max12]:'))
pwdd2=MyList(uk,12)#+MyList(ksym,3)
random.shuffle(pwdd2)
print('printed elms ',pwdd2)#print(mine.count('a'))
mine=str(' ') #cat empty-space string
#delimiting passphrase to desired length
for i in range(my_len-2):#at least 2chars are numbers
    mine+=pwdd2[i]
mine+=str(seg[0])#print(seg[0],seg[1])
print('LongPass ',mine[:my_len+1])#print(mine.count('a'))
