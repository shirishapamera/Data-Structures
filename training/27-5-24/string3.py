# replace vowels in capital consonants in small in a string with thw same letter
#ip: school
#op: schOOl
s=input()
s=s.lower()
b=""
for i in s:
    if (i in 'aeiou'):
        b=b+(i.upper())
    else:
        b=b+i
print(b)


