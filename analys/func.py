def numberlist(items):
    numb=1
    for item in items:
        print(numb,item)
        numb+=1
def main():
    numberlist(['red','orange','yellow','green'])
    print()
    numberlist(['apple','banana','pears'])
main()
