'''l=[2,3,5,6]
op:11'''
l=list(map(int,input().split()))
t=int(input())
m=[]
for i in range(len(l)+1):
    m.append([0]*(t+1))
for i in range(1,len(l)+1):
    for j in range(t+1):
        if j==0 :
            m[i][j]=1
        elif j!=0 and j<l[i-1]:
            m[i][j]=m[i-1][j]
        elif l[i-1]>j:
            m[i][j]=m[i-1][j]
            print(m,end="*****************************************")
        elif l[i-1]<=j:
            if m[i-1][j]==0:
                x=j-(l[i-1])
                m[i][j]=m[i-1][x]
                print("*********")
            else:
                m[i][j]=m[i-1][j]

print(m)
    