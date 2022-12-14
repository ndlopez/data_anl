"""The following Python implementation of Shamir's secret sharing is
released into the public domain under the terms of CC0 and OWFa.
"""
from __future__ import division
import random
import functools

"""12th Mersenne prime
for this app we want to a known prime number as close as possible to
our security level; e.g. desired security level of 128bits 
---too large and all the cyphertext is large; 
too small and security is compromised. 
"""
_PRIME = 2**10 -1
_rint =functools.partial(random.SystemRandom().randint,0)

def _eval_at(poly,x,prime):
    """Evaluates polynomial (coeff tuple) at x, used to generate a
    Shamir pool in make_random_shares below"""
    accum=0
    for coeff in reversed(poly):
        accum *= x
        accum += coeff
        accum %= prime
    return accum

def make_random_shares(minimum, shares,prime= _PRIME):
    """Generates a random shamir pool, returns the secret and share points"""
    if minimum > shares:
        raise ValueError("pool secret would be irrecoverable")
    poly= [_rint(prime) for i in range(minimum)]
    points = [(i,_eval_at(poly,i,prime))
              for i in range(1,shares + 1)]
    return poly[0],points

def _extended_gcd(a,b):
    '''div in integers mod p means finding the inverse of the denominator
    mod p and then multiplying the num by this inverse.
    Note:inv of A is B such that A*B %p==1 this can be computed via extended Euclidean alg'''
    x=0
    last_x =1
    y=1
    last_y =0
    while b != 0:
        quot=a // b
        a,b =b,a%b
        x, last_x = last_x -quot *x,x
        y, last_y = last_y -quot *y,y
    return last_x,last_y

def _divmod(num,den,p):
    '''Compute num/den mod prime p
    The return value will be such that the following is true:
    den * _divmod(num,den,p) %p == num'''
    inv, _ = _extended_gcd(den,p)
    return num * inv

def _lagrange_interpolate(x, x_s, y_s, p):
    '''Finds the y-value for the given x, given n (x,y) points;
    k points will define a polynomial of up to the kth order'''
    k=len(x_s)
    assert k==len(set(x_s)), "points must be distinct"
    def PI(vals): #upper-case PI --product of inputs
        accum=1
        for v in vals:
            accum *=v
        return accum
    nums=[] #avoid inexact division
    dens=[]
    for i in range(k):
        others = list(x_s)
        cur = others.pop(i)
        nums.append(PI(x - o for o in others))
        dens.append(PI(cur - o for o in others))
    den = PI(dens)
    num = sum([_divmod(nums[i]* den * y_s[i] % p,dens[i],p)
               for i in range(k)])
    return (_divmod(num,den,p) +p) % p

def recover_secret(shares, prime= _PRIME):
    '''Recover the secret from share points (x,y) points of the polynomial'''
    if len(shares) < 2:
        raise ValueError("need at least two shares")
    x_s, y_s = zip(*shares)
    return _lagrange_interpolate(0, x_s, y_s,prime)

secret, shares = make_random_shares(minimum=3, shares=6)

print('secret and shares: ',secret,shares)

print('secret recovered from minimum subset of shares', recover_secret(shares[:3]))
print('secret recovered from a diff min of subset of shares',recover_secret(shares[-3:]))
        
