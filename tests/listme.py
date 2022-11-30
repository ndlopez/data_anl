wordlist=['cat','dog','rabbit']
letterlist=[]
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
count=0
i=0
letterlist2=[]
while i<len(letterlist)-1:
    aletter=letterlist[i]
    if letterlist[i]!=letterlist[i+1]:
        letterlist2.append(aletter)
    else:
        count+=1
    i+=1
print(letterlist2)
