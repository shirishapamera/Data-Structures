'''
if 1 inser
2 search for word
3  search for prefix
ip:7
1 school
1 world
1 word
1 scholar
2 word
2 wood
3 sch
op:
true
false
true
'''


n=int(input())
l=[]
for i in range(n):
    l.append(input())
print(l)
def search(i):
    for j in l:
        if i[2:]==j[2:] and j[0]=='1':
            return True
    return False
def prefix(i):
    x=len(i[2:])
    for j in l:
        if i[2:(2+x)]== j[2:]:
            return True
    return False


        
for i in l:
    if i[0]=='2':
        print(search(i))
    if i[0]=='3':
        print(prefix(i))
            