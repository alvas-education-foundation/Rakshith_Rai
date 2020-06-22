def minimumDistances(l):
    d=list()
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if(l[i]==l[j]):
                d.append(abs(i-j))
                break
    try:
        return min(d)
    except:
        return -1

n = int(input())
a = list(map(int, input().rstrip().split()))
result = minimumDistances(a)
print(result)
