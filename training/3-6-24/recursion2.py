#print sum of even numbers from 0 to n
def fac(x,s):
    if x==1:
        return s
    if x%2==0:
        s+=x
    return fac(x-1,s)
n=int(input("enter the number:"))
print(fac(n,0))

'''
def fac(x):
    if x==0:
        return 0
    return x+(fa(x-2))
    
n=13
if n%2==0:
print(fa(n)) 
else:
print(fa(n-1))   
    '''

