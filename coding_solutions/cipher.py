import string
S=input()
n=int(input())
l=list()
for i in range(len(S)):
    if S[i].isdigit() or S[i].isalpha():
        m=ord(S[i])+n
        if S[i].isupper():
            while m>90:
                m-=26
        elif S[i].islower():
            while m>122:
                m-=26
        else:
            while m>57:
                m-=10
        l.append(chr(m))
    else:
        l.append(S[i])
print("".join(l))