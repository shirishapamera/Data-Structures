#check a given two numbers are co primes or not
import math
n=int(input())
m=int(input())
c=math.gcd(m,n)
if c==1:
    print("co prime")
else:
    print("not")