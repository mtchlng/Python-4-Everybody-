import string
fname = input("Enter file: ")
try: fhand=open(fname)
except:
    print("File error: ", fname)
    exit()

counts = dict()
for x in fhand:
    x = x.rstrip()
    x = x.translate(x.maketrans('','',string.punctuation))
    x = x.lower()
    words = x.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1
print(counts)
