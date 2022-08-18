import matplotlib.pyplot as plt
import csv
x=[]
y=[]
with open('ejemplo.txt','r') as csvfile:
    plots=csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
plt.plot(x,y,label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('x')
plt.title('Haleakala NM\n 2003/11/04')
plt.legend()
plt.show()
