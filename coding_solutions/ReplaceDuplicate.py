from collections import Counter
n=int(input())
l=list(map(int,input().split(" ")))
l.sort()
print(l)
d=Counter(l)
dist=list()
for i in d:
    if d[i]>=2:
        dist.append(i)

max2=max(l)
if dist!=[]:
    min2=min(dist)
    replace=list()
    for i in range(min2,max2+1):
        if i not in l and l[i]>=i:
            replace.append(i)
    
    for i in range(len(l)):
        if l[i] in dist and d[l[i]]>1:
            if replace!=[]:
                d[l[i]]-=1
                l[i]=replace[0]
                del(replace[0])
            else:
                max2+=1
                d[l[i]]-=1
                l[i]=max2
print(l)