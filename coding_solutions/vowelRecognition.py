m1=int(input())
m=list()
for _ in range(m1):
    count=0
    name=input()
    y=name.lower()
    s=list()
    for i in range(len(y)):
        if y[i] in "aeiou":
            m=len(y)-i
            count+=m*(i+1)
            m=0
    print(count)