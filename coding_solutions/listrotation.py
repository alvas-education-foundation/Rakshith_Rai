l=list()
s=list(input())
q=int(input())
for _ in range(q):
    m=list(input().split(" "))
    if m[0] == 'L':
         for i in range(int(m[1])):
                     t=s[0]
                     s[0:len(s)-1]=s[1:len(s)]
                     s[len(s)-1]=t
    elif m[0]=='R':
              for i in range(int(m[1])):
                     t=s[len(s)-1]
                     s[1:len(s)]=s[0:len(s)-1]
                     s[0]=t
    l.append(s[0])

print("".join(l))