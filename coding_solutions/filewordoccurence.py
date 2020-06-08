import string
fname=input("Enter file name:")
try:
    fhand=open(fname)
except:
    print("File cannot be opened")
    exit() 
 
d=dict()
for line in fhand:
    line=line.rstrip()
    line=line.translate(line.maketrans('','',string.punctuation))
    line=line.lower()
    for word in line.split():
        d[word]=d.get(word,0)+1
print(d) 