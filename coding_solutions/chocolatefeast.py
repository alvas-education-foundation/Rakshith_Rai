
def chocolateFeast(n, c, m):
    k=n//c
    n=k
    while(n>=m):
        n=n-m
        n=n+1
        k+=1

    return k

t = int(input())
for t_itr in range(t):
    ncm = input().split()
    n =int(ncm[0])
    c = int(ncm[1])
    m = int(ncm[2])
    result = chocolateFeast(n, c, m)
    print(result)

