s1=input()
r=int(input())
l=[('L',2),('R',3),('L',1)]
s=""
for i in range(3):
    if l[i][0]=='L':
        x=l[i][1]
        s=s+s1[x]
    if l[i][0]=='R':
        x=l[i][1]
        s=s+s1[-x]
print(s)
st=sorted(s)
for i in range(len(s1)-(n+1)):
    st1=sorted(s1[i:i+r])
    if st==st1:
        print("yes")
        break
else:
    print("no")



'''
ip:
school
3
L 2
R 3
L 1"
-------------

a=input()
n=int(input())
str=''
for i in range(n):
    b=input()
    if(b[0]=='L'):
        str=str+a[int(b[2])]
    else:
        str=str+a[-int(b[2])]
print(str)
str=list(str)
str.sort()
b=[]
for i in range(len(a)-n+1):
    t=list(a[i:n+i])
    t.sort()
    b.append(t)
print(b)
print(str)
for i in b:
    if(i==str):
        print("yes")
        break
else:
    print("no")'''