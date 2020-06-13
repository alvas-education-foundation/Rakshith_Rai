def countApplesAndOranges(s, t, a, b, apples, oranges):
    apcount=0
    orcount=0
    for i in range(len(apples)):
        m=apples[i]+a
        if  m >=s and  m<=t:
            apcount+=1
    for i in range(len(oranges)):
        j= oranges[i]+b 
        if j <=t and j>=s:
            orcount+=1
    print(apcount)
    print(orcount)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
