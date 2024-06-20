g={1:[(2,2),(3,2),(4,1)],2:[(1,2),(4,2),(5,3)],3:[(1,2),(4,3)],4:[(1,1),(2,2),(3,3),(5,2)],5:[(2,3),(4,2)]}
def dij(x):
    d={1:0,2:999,3:999,4:999,5:999}
    d[x]=0
    vi=[]
    q=[x]

    while q:
        m=99999
        for i in q:
            if d[i]<m:
                m=d[i]
                x=i
        for i in g[x]:
            if i[0] not in vi:
                if d[i[0]]>i[1]+d[x]:
                    d[i[0]]=i[1]+d[x]
                if i[0] not in q:
                    q.append(i[0])
        vi.append(x)
        q.remove(x)
    return d
print(dij(1))


