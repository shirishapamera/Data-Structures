'''
count of numbers in the list
ip:2 3 4 2 3 4 5
op:2-2
3-2
4-2
5-1'''
l=list(map(int,input().split()))
l1=[]
for i in l:
      if i not in l1:
        l1.append(i)
for i in l1:
    print(i,"-",l.count(i))