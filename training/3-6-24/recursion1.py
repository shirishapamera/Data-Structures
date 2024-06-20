#using recursion print sum of even numbers in list1 and odd numbers in list2
a=[3,8,5,4,3]
b=[5,0,9,3,2]
def sum(i,e,o):   
    if i==len(a):
        return (e,o)
    if a[i]%2==0:
        e+=a[i]
    if b[i]%2!=0:
        o+=b[i]
    return sum(i+1,e,o)
print(sum(0,0,0))
