def migratoryBirds(l):
    l.sort()
    d=dict()
    for i in l:
        if  i in d:
            d[i]+=1
        else:
             d[i]=0
    max=0
    for i in d:
        if d[i]>max:
            max=d[i]
            key=i
    return key


arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = migratoryBirds(arr)
print(result)
