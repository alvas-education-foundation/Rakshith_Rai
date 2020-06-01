def enc(str2):
    count=len(str2)
    p=int(count**(1/2))
    k=0
    l=[[]]
    if (p**2)-count==0:
        m,n=p,p
    else:
        m=p
        n=m+1
        if m*n>=count:
            pass
        else:
            m=m+1
    for i in range(m):
        if(k<len(str2)):
                l.insert(i,str2[k:k+n].replace(''," ").strip().split(" "))
                k=k+n

    t=[]
 
    for j in range(n):
        for i in range(m):
            try:
                v=l[i][j]
                t.append(v)
            except:
                pass
        t.append(" ")        
        
    return "".join(t).strip()


result=enc("iffactsdontfittotheorychangethefacts")
print(result)