#check whether the string contains all alphabets
s=input()
'''cs=set(s)
if len(cs)==27:
    print("yes")
else:
    print("no")
'''


'''
cs=97
c=0
for i in s:
    if i.islower():
        if chr(cs) in s:
            c=c+1
            cs=cs+1
if c==26:
    print("yes")
else:
    print("no")
    '''

'''
b="abcdefghijklmnopqrstuvwxyz"
for i in b:
    if i not in s:
        print("no")
        break
else:
    print("yes")     
'''

'''
for i in range(97,123):
    if chr(i) not in s:
        print("no")
        break
else:
    print("yes") 
'''

d=[0]*26
for i in s:
    if i.islower():
        d[ord(i)-97]+=1
print(all(d))