
'''
ip:FMFMFF
op:feamle are more
'''
ip=input()
c=0
for i in ip:
    if i=='M':
        c=c+1
    else:
        c=c-1
if c==0:
    print("male and female are equal")
elif c>=1:
    print("male are more")
else:
    print("feamle are more")

    
'''
for i in ip:
    if i=='F':
        f+=1
    else:
        m+=1
if f==m:
    print(0)
elif m>f:
    print("m")
elif m<f:
    print("f")

'''

