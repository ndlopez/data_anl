'''Newton method for approximating square roots
newguess= 0.5(root+n/root), where n/2 is root'''
def squareroot(n):
    root=n/2
    for k in range(20):
        root = (1/2)*(root+(n/root))
    return root
number=45
print(squareroot(number))
