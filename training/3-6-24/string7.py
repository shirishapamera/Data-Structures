#arrange the trings in proper order

s="is2 sentence4 this1 a3"
s=s.split()
l=[0]*len(s)
for i in s:
    l[int(i[-1])-1]=i[:-1]
    
print(' '.join(l))
