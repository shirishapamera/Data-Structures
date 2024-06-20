#check whether given password is strong or not if not print how many characters we need to include
'''
ip:Shirisha987@
op:0
ip:shirisha12@
op:1(capital letter)
ip:Ss@1
op:4(length less than 8)

'''
s=input()
c,c1,c2,c3,c4=0,0,0,0,0
for i in s:
    if (i.isupper()):
        c1=1
        continue
    elif (i.islower()):
        c2=1
        continue
    elif (i.isdigit()):
        c3=1
        continue
    elif (not i.isalnum()):
        c4=1
c=c1+c2+c3+c4
m=4-c
if(len(s)+m)<8:
    print(8-len(s))
else:
    print(m)