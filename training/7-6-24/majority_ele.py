'''l=[2,1,2,1,1,2]
l1=set(l)
n=len(l)/2
a,x=0,0
for i in l1:
    a=l.count(i)
    if a>n:
        x=i
print(x)'''

a=[1,1,1,2,2,2,2]
c=1
p=a[0]
for i in range(1,len(a)):
    if a[i]==p:
        c=c+1
    else:
        if c!=0:
           c=c-1
        if c==0:
            c=1
            p=a[i]
print(p)
    
