
n=int(input("enter a number"))
def sum(n):
    s=0
    while n:
        r=n%10
        s=s+r
        n=n//10
    if s<=9:
        return s
    else:
        s1=0
        while s:
            r=s%10
            s1=s1+r
            s=s//10
        return s1
res=sum(n)
print(res)
def prime(res):
        if res in [2,3,5,7]:
            print(n)
        else:
            sum(n+1)
    
prime(res)

