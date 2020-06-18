def cutTheSticks(l):
            cut=min(l)
            for i in range(len(l)):
                    if l[i]>0:
                        l[i]=l[i]-cut
            print(l)

n = int(input())
arr = list(map(int, input().rstrip().split()))
print(arr)
result = cutTheSticks(arr)