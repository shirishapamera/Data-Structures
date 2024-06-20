s=input()
s1=""
max1=0
l=0
i=0
j=0
while i<len(s):
    while j<len(s):
        if s[j] not in s1:
            s1=s1+s[j]
            l=l+1
            j=j+1
        else:
            if max1<l:
                max1=l
                l=0
                s1=""
            j=s.index(s[j])       
    i=i+1
print(s1)
if max1>l:
    print(max1)
else:
    print(l)

