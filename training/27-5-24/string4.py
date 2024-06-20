'''ip:  string:  2 4 6 3.3 5 6.3
op: even sum: 12
odd sum: 5
decimal sum: 9.6 '''
s=input()
s=s.split()
es,os,ds=0,0,0
for i in s:
    if "." in i:
        ds+=float(i)
    elif int(i)%2==0:
        es+=int(i)
    else:
        os+=int(i)
print("even sum:",es)
print("odd sum:",os)
print("decimal sum:",ds)
    