#find the length of the longest subsequence in lexographical order
#ip:xyzabcde
#op:5
s=input()
max1=0
ma=1
for i in range(len(s)-1):
    if (ord(s[i+1])-ord(s[i]))==1:
        ma=ma+1
    else:
        if max1<=ma:
            max1=ma
            ma=1
if(max1<ma):
    max1=ma
print(max1)
