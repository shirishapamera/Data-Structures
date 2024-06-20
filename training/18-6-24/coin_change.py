l=[1,3,4,5]
r=17
m=[-1]*(r+1)
m[0]=0
for i in l:
    for j in range(1,r+1):
        if j>=i:
            if m[j-i]!=-1:
                if m[j]!=-1:
                    m[j]=min(m[j],m[j-i]+1)
                else:
                    m[j]=m[j-i]+1

print(m[-1])


'''for i in range(len(l)):
    m.append([0]*(r+1))
for i in range(len(l)):
    for j in range(r+1):
        if i==0 and  j<l[i]:
            m[i][j]=0
        elif i!=0 and j<l[i]:
            m[i][j]=m[i-1][j]
        elif l[i]<=j:
            x=j-l[i]
            y=(m[i][x])+1
            if i!=0:
                m[i][j]=min(y,m[i-1][j])
            else:
                m[i][j]=y
        
        
print(m,end="\n")
print(m[i][j])'''

