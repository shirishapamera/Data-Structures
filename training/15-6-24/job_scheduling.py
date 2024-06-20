jo=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
b=a.copy()
i=1
while i<len(jo):
    j=0
    while j<=i-1:
        if jo[j][1]<=jo[i][0]:
            if b[j]+a[i]>b[i]:
                b[i]=b[j]+a[i]
        j=j+1
    i=i+1
print(b)
print(max(b))



        
