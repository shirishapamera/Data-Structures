
#ip:khoor  k=4
#op:hello
s=input()
k=int(input())
c=k%26
res=""
for i in s:
    if (ord(i)-c)>=97:
        res=res+(chr(ord(i)-c))
        
    else:
        res=res+(chr(ord(i)-c+26))
print(res)
