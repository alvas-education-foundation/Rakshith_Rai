def sumprimes(l):
    tot=0
    i=0
    while i < len(l):
               if(l[i]>1):
                    if l[i] == 2:
                        tot=tot+2
                    else:
                        h=l[i]
                        for j in range(2,h):
                            if l[i]%j == 0:
                                break
                        if(j==h-1):
                            tot=tot+l[i]
               i=i+1         
    return tot

l=[1,3,4,5,6,7]
m=sumprimes(l)
print(m)