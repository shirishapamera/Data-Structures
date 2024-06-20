'''
ip=[2,5,2,3,6,7,1,0,5]
op: 14

ip=[2,5,2,3,6,7,1,0,5,7]
op: 20
'''
arr=[2,5,2,3,6,7,1,0,5]

l=[0]*len(arr)
r=[0]*len(arr)
m=0
m1=0
for i in range(len(arr)):
    if(arr[i]>m):
        m=arr[i]
    l[i]=m
    
for i in range(len(arr)-1,-1,-1):
    if(arr[i]>m1):
        m1=arr[i]
    r[i]=m1
s=0
for i in range(len(arr)):
    s=s+abs(min(l[i],r[i])-arr[i])
print(s)
