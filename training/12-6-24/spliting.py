"""
ip: hello:5438,car:214,book:8799,apple:2187
op: oaxp
"""
s=input()
s=s.split(",")
res=""
for i in s:
    c=0
    for j in i:
        if j==":":
            break
        else:
            c=c+1
    for k in range(c,0,-1):
        if str(k) in i[c+1:]:
            res=res+i[k-1]
            break
    else:
        res=res+"x"
print(res)

'''
a=list(input().split(",")) 
s=""
for i in a: 
    b=i.split(":")
    l=len(b[0])
    if(str(l)in b[1]):
        s=s+b[0][-1]
    else:
        for i in range(l-1,0,-1):
            if(str(i) in b[1]):
                s=s+b[0][i-1]
                break
        else:
            s=s+'x'
print(s)
'''

