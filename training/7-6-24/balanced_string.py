a = "(([{}])]"
s = []
f = 0
c = 0

for i in a:
    if i in '{[(':
        s.append(i)
    elif not s:
        print(c)
        f = 1
        break
    else:
        if (i == '}' and s[-1] == '{') or (i == ']' and s[-1] == '[') or (i == ')' and s[-1] == '('):
            s.pop()
        else:
            print(c)
            f = 1
            break
    c += 1

if f == 0:
    if s:
        print(c)
    else:
        print("-1")