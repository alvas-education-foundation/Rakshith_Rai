def transpose(l):
    m=len(l)
    n=len(l[0])
   
    t=[]
    z=[]
    for j in range(0,n):
        t=[]
        for i in range(0,m):
           t.append(l[i][j])
        z[j:n]=[t]
    return z

l=[[1,2],[2,3],[3,4],[4,5]]
a=transpose(l)
print(a)
