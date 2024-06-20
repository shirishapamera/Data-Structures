#find the kth largerst number that is divisible by the given number
n=int(input())
k=int(input())
c1=0
c=0
if k==1:
    print(k)
else:
    for i in range(n,0,-1):
        if n%i==0:
            c1=c1+1
            if c1==k:
                print(i)
                break

            