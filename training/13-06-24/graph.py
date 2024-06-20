d={5:[3,7],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
d2={1:[2,3,4],2:[1,4,6],3:[1,4],4:[1,2,3,5,6],5:[4],6:[2,4,7],7:[6]}
def dfs(x,l):
    l.append(x)
    print(x,end=" ")
    for i in d[x]:
        if i not in l:
            dfs(i,l)
def paths(x,l):
    l.append(x)
    if x==2:
        print(l)
        l.pop()
        return
    for i in d[x]:
        if i not in  l:
            paths(i,l)
    l.pop()
def all_paths(x,e,l):
    l.append(x)
    if x==e:
        print(l)
        l.pop()
        return
    for i in d[x]:
        if i not in  l:
            all_paths(i,e,l)
    l.pop()
def BFS(x,q,v):
    q.append(x) 
    while q:
        for i in d[q[0]]:
            if i not in q and i not in v:
                q.append(i)
        r=q.pop(0)
        v.append(r)
    return v









dfs(5,[])
print("paths")
paths(7,[])
print("all paths")
for i in d:
    all_paths(5,i,[])
print("breadth first search")
print(BFS(5,[],[]))




d1={5:[(7,11),(3,10)],7:[(5,11),(4,12),(3,25)],4:[(7,12),(8,10),(2,13)],8:[(3,15),(4,10),(2,16)],3:[(3,10),(7,14),(8,15)],2:[(4,13),(8,16)]}
def path_cost(x, l, c):
    l.append(x)
    if x == 2:
        print(l,c)
        l.pop()
        return
    for i in d1[x]:
        if i[0] not in l:
            path_cost(i[0], l, c + i[1])
    l.pop()


print("path cost")
path_cost(5,[],0)


def least_cost(d1,l,x,e, c,m,l1):
    l.append(x)
    if x == e:
        if c<m:
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d1[x]:
        if i[0] not in l:
            m,l1=least_cost(d1,l,i[0], e, c + i[1],m,l1)
    l.pop()
    return m,l1
def all_least_cost(d1,l,x,e, c,m,l1):
    l.append(x)
    if x == e:
        if c<m:
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d1[x]:
        if i[0] not in l:
            m,l1=all_least_cost(d1,l,i[0], e, c + i[1],m,l1)
    l.pop()
    return m,l1

print("least cost",least_cost(d1,[],5,2,0,99999,[]))
for i in d:
    print("all least cost",least_cost(d1,[],5,i,0,99999,[]))
