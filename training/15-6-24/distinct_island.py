"""
ip:  5
     0 1 0 0 1
     1 0 0 1 1
     0 0 0 0 0 
     1 0 0 0 0 
     1 0 0 0 1

op:  5
"""


def fun(i,j,c): 
    if(i<0 or j<0 or i>=n or j>=n or l[i][j]!=1):
        return c
    l[i][j]=2
    c=c+1
        

    c=fun(i-1,j,c)
    c=fun(i,j-1,c)
    c=fun(i+1,j,c)
    c=fun(i,j+1,c)
    return c

n=int(input())
l=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    l.append(a) 
count=0
m=0
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            count+=1
            x=fun(i,j,0)
            if x>m:
                m=x
print(m)
print("Number of Islands:",count)