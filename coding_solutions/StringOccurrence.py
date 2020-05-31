c=input("enter the input:")
sub=input("enter the substring:")
j=0
count=0
t=0
i=0
while(i!=len(c)):
   if count!=len(sub) and sub[j]==c[i]:
       count+=1
       j+=1
   if sub[j-1]!=c[i] and count>0:
       j=0
       count=0
       
   if count==len(sub):
       i-=1
       count=0
       j=0
       t+=1
              
   i+=1
    
print("The total number of occurences:",t)
