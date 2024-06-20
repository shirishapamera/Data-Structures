def fun(i,j,c):
    if(i<0 or i>=n or j>=m or j<0):#(i == k and j == l):
        return c
    if (i==n-1 and j==m-1):
        c = c+1
        return c
    vi.append((i,j))
    if((i-1,j) not in vi):
        c = fun(i-1,j,c)
    if((i+1,j) not in vi):
        c = fun(i+1,j,c)
    if((i,j-1) not in vi):
        c = fun(i,j-1,c)
    if((i,j+1) not in vi):
        c = fun(i,j+1,c)
    vi.pop()
    return c
n = int(input())
m = int(input())
vi=[]
print(fun(0,0,0))