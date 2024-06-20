l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
l3=[]
l4=[]
def fun1(i,j):
    if j==len(l2):
        return l3
    if l2[j]%2!=0:
        l3.append(i+l2[j])
    return fun1(i,j+1)

def fun(i):
    if i==len(l1):
        return 
    if l1[i]%2==0:
        l4.append(sum(fun1(l1[i],0)))
        fun(i+1)
    else:
        fun(i+1)  
fun(0)
print(l3)
print(l4)
s=0
