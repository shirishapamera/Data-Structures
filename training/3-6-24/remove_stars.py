#remove the stars in the given string
s="leet**cod*e"
b=[]
for i in s:
    if i!='*':
        b.append(i)
    else:
        b.pop()
print(b)
print("".join(b))
        


