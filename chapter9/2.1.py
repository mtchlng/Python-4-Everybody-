fname = input("Enter file: ")
try: fhand=open(fname)
except:
    print("File error: ", fname)
    exit()

daycounts = dict()
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != "From":
        continue
    else:
        if words[2] not in daycounts:
            daycounts[words[2]]=1
        else: daycounts[words[2]]+=1

print(daycounts)

#    x = x.rstrip()
#    x = x.translate(x.maketrans('','',string.punctuation))
#    x = x.lower()
