l=list(input().split(" "))
answer=1
for i in range(1,len(l)):
    answer=(answer*int(l[i])) % (10**9 + 7)
print(answer)
