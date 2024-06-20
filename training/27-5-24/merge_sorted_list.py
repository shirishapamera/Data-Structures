#merge two sorted lists
'''ip: 1 2 5 6
    3 7 9
op: 1 2 3 5 6 7 9
'''
l1=list(map(int,input("enter list1").split()))
l2=list(map(int,input("enter list2").split()))
n=len(l1)
m=len(l2)
l3=[]
i=0
j=0
while i<n and j<m:
    if l1[i]<l2[j]:
        l3.append(l1[i])
        i+=1
    else: 
        l3.append(l2[j])
        j+=1
while i < n:
    l3.append(l1[i])
    i += 1
while j < m:
    l3.append(l2[j])
    j += 1

print(l3)
        



