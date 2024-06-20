#ip: aabbaaadddd
#op: a2b2a3d4

s=input()
res=""
c=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c=c+1
    else:
        res=res+s[i]+str(c)        
        c=1
res=res+s[-1]+str(c)
print(res)
