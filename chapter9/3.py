fname = input("Enter file: ")
try: fhand=open(fname)
except:
    print("File error: ", fname)
    exit()

addresscounts = dict()
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != "From":
        continue
    else:
        if words[1] not in addresscounts:
            addresscounts[words[1]]=1
        else: addresscounts[words[1]]+=1

print(addresscounts)

#    x = x.rstrip()
#    x = x.translate(x.maketrans('','',string.punctuation))
#    x = x.lower()
