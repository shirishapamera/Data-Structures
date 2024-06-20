''' 
ip=3
abc
xyz
pqr
string=axpby (be in order and shold not repeat)
op:yes
string: apbyq
op:no

string:axpbyqcxr
op:no

'''
n=int(input())
m=[]
f=0
for i in range(n):
    m.append(list(input()))
s=input()
for i in range(len(s)):
    if s[i]  not in m[i%n]:
        print("no")
        f=1
        break
    else:
        m[i].remove(s[i])
        
if(f==1):
    print("no")
else:
    print("yes")


