#check palindrome or not using recursion
n=int(input())
def fun(n,res):
    if n==0:
        return res
    res=res*10+(n%10)
   
    return fun(n//10,res)

r=fun(n,0)
if r==n:
    print("palindrome")
else:
    print("no")
