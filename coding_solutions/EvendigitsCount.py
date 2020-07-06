l=[]
n=101027
m=n
while(m>0):
    l.append(m%10)
    m=m//10
    
count=0
for i in range(len(l)):
    if l[i]!=0 and n % l[i]==0:
        count+=1
print(count)
