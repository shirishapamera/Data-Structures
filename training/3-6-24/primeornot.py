def add(n):
    s=0
    while(n):
        s=s+(n%10)
        n=n//10
    return s
def pnp(x):
    if x in [2,3,5,7]:
        return m
    else:
        return m+1
n=int(input())
m=n
if n<10:
    print(pnp(n))
else:
    while(1):
        n=add(n)
        if n<10:
            break
    print(pnp(n))

