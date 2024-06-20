'''
*****
*123*
*456*
*789*
*****
'''

n=int(input())
k=1
for i in range(n+1):
    for j in range(n+1):
        if i==0 or j==0 or i==4 or j==4:
            print("*",end=" ")
        else:
            print(k,end=" ")
            k+=1  
    print()
            