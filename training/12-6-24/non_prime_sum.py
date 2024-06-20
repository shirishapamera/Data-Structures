#print the sum of the larget prime numbers between the given numbers
'''ip:4 8 14 22 36 68
exp:
7
13
19
31
67
op:137
'''
l=list(map(int,input().split()))
def prime(k,j):
    while(1):
        c=0
        for i in range(2,(j//2)+1):
            if j%i==0:
                c+=1
                break
        if c==0:
            return j
    
        if j==k:
            return 0
        else:
            j=j-1
x=0
for i in range(len(l)-1):
    x=x+prime(l[i],l[i+1])
print(x)



'''
def isprime(x):
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1

def largep(n,m):
    for i in range(m-1,n,-1):
        if(isprime(i)):
            return i
    return 0

a=list(map(int,input().split()))
s=0
for i in range(len(a)-1):
    s=s+largep(a[i],a[i+1])
print(s)
'''
