# count no of digits,special characters, lowercase,uppercase vowels and lower,upper case vowels
inp=input("enter the string:")
lv,uv=0,0
lc,uc=0,0
s,d=0,0
for i in inp:
    if(i.isupper()):
        if( i in 'AEIOU'):
            uv+=1
        else:
            uc+=1
    elif(i.islower()):
        if( i in "aeiou"):
            lv+=1
        else:
            lc+=1
    elif(i.isdigit()):
        d+=1
    elif (not i.isalnum()):
        s+=1

print("lv -",lv)
print("uv -",uv)
print("lc -",lc)
print("uc -",uc)
print("s- ",s)
print("d -",d)




    

