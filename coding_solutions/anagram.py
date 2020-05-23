from collections import Counter
import math
n=int(input())
for j in range(n):
    count=0
    s=input()
    b=input()
    d=Counter(s)
    d1=Counter(b)
    for i in range(len(b)):
        if b[i] in s :
            if d[b[i]] != 0:
                count=count+(abs(d[b[i]]-d1[b[i]]))
                d[b[i]]=0
        else:
            count+=1
    for i in range(len(s)):
        if s[i] not in b:
            count+=1
    print(count)
