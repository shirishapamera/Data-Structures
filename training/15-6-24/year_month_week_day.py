'''
1y=360  1m=30  1w=6

ip:65476

n=int(input())
y=n//360
y1=n%360
m=y1//30
m1=m%6
w=m1//6
d=w%6
print(y,m,w,d)
'''
n=int(input())
def fun(n):
    if n<0:
        return
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return fun(n-1)+fun(n-2)
x=fun(n)
print(x)