from collections import Counter
n=int(input())
for i in range(n):
    flag=1
    s,d=input().split(" ")
    d1=Counter(s)
    d2=Counter(d)
    for i in range(len(s)):
        if s[i] in d:
            if d1[s[i]]!=d2[s[i]]:
                flag=0
                break
        else:
            flag=0
            break
    for i in range(len(d)):
        if d[i] not in s:
            flag=0
            break
    if flag==1:
        print("YES")
    else:
        print("NO")