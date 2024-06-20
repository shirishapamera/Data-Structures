#buy a item on any day and sell it with maximum profit
'''l=list(map(int,input().split()))
sell=0
for i in range(len(l)):
    for j in range(i,len(l)):
        if (l[i]<l[j] and l[j]-l[i]>sell):
            sell=l[j]-l[i]
print(sell)
'''
l=list(map(int,input().split()))
pr=0
b=0
for i in range(1,len(l)):
    if l[b]> l[i]:
        b=i
    pr=l[i]-l[b]
print(pr)
