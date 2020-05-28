d={0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
n=int(input())
for _ in range(n):
    q=input()
    q1=int(q)
    m=0
    for i in range(len(q)):
        m+=d[int(q[i])]
    start=''
    if m%2!=0:
        start='7'
        m-=3
    l=['1']*(m//2)
    print(start+"".join(l))