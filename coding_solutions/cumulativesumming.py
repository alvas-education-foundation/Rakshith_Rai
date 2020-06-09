l=list(map(int,input().split(" ")))
sum1=[0]
sum2=0
for i in range(len(l)):
    sum2+=l[i]
    sum1.append(sum2)
print(sum1)
n=int(input("enter the starting point in list"))
m=int(input("enter the ending point in list"))
mean=(sum1[m+1]-sum1[n])/(m-n+1)
print(mean)