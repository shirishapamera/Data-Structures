#find the missing element in the given range
'''
iop:5
0 1 3 4 5
op:2
'''
n=int(input("enter"))
l=list(map(int,input().split()))[:n]
l.sort()
for i in range(0,n):
    if l[i]!=i:
        print(i)
        break

'''b=sum(l)
n=n*(n+1)//2
print(n-b)'''