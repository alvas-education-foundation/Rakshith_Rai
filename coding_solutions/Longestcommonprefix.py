class Solution:
    def longestCommonPrefix(self, l: List[str]) -> str:
        m=[]
        if len(l)==0:
            return ""
        else:
            
            for i in range(len(l)):
                for j in range(0,len(l)-i-1):
                    if(len(l[i])>len(l[j+1])):
                        t=l[j+1]
                        l[j+1]=l[i]
                        l[i]=t
            count=1
            print(l)
            for i in range(len(l[0])):
                count=1
                for j in range(len(l)-1):
                    if l[0][i]==l[j+1][i]:
                        count+=1
                if count==len(l):
                    m.append(l[0][i])
                else:
                    break
                
            return "".join(m)