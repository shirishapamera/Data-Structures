'''
ip: 7262
op:2h:1m:2s

ip:500
op: 0h:8m:20s
'''

n=int(input())
h=n//3600
m=n%3600
m1=m//60
m2=m%60
print(h,"h:",m1,"m:",m2,"s")
