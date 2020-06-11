def sockMerchant(n, ar):
    count=0
    d=dict()
    for i in ar:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d:
        count+=d[i]//2
    print(count)


n = int(input())
ar = list(map(int, input().rstrip().split()))
sockMerchant(n, ar)