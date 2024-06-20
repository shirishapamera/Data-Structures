'''  
from the given strings extract the  unique numbers and form the largest even number
ip:tu5g2k1h8
   g5g8gd6h3
op:865312
'''

a=input()
b=input()
c=set()
for i in a:
    if(i.isdigit()):
        c.add(i)
for i in b:
    if(i.isdigit()):
        c.add(i)
d=list(sorted(c,reverse=True))
if(int(d[-1])%2==0):
    print(''.join(d))
else:
    for i in range(len(c)-2,-1,-1):
        if(int(d[i])%2==0):
            d.append(d.pop(i))
            print(''.join(d))
            break
    else:
        print(-1)
'''
s1=input()
s2=input()
s=""
for i in s1:
    if i in "123456789":
        s=s+i
for i in s2:
    if i in "123456789" and i not in s:
        s=s+i
l=list(s)
l.sort()
ss=""
for i in range(len(l)-1,-1,-1):
    if int(l[i])%2==0:
        ss=ss+l[i]
    else:

print(ss)

'''


