#print all 3 possible pairs from the list
'''for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            print(l[i],l[j],l[k])
'''
'''def pairs(l,n,i,j,k): 
    if i==n-2 and j==n-1 and k==n:
        return 
    for j in range(i+1,n):
        for s in range(j+1,n):
            print(l[i],l[j],l[s]) 
    pairs(l,n,i+1,i+2,i+3)
pairs(l,n,0,1,2)
'''
def three(l,k): 
    def fun(curr,start):
        if(len(curr)==k):
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
        return
    fun([],0)
l=[3,2,5,4,1,6,8]
n=3
three(l,n)


        