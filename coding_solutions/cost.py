n=int(input())
for j in range(n):
    count=0
    count1=0
    cost=input().split(" ")
    if int(cost[0])<int(cost[1]):
        cost[0],cost[1]=cost[1],cost[0]
    par=int(input())
    for i in range(par):
        l=input().split(" ")
        if int(l[0])==1:
            count1+=1
        if int(l[1])==1:
            count+=1
    if count1<count:
        count1=count1*int(cost[0])
        count=count*int(cost[1])
    else:
        count=count*int(cost[0])
        count1=count1*int(cost[1])
    print(count+count1)