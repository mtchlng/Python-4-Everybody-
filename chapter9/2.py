#This was my original attempt, which had a few logical errors.
#See 2.1 for the correct answer

fname = input("Enter file: ")
try: fhand=open(fname)
except:
    print("File error: ", fname)
    exit()

import string
daycounts = dict()
for x in fhand:
    x = x.rstrip()
    x = x.translate(x.maketrans('','',string.punctuation))
    x = x.lower()
    words = x.split()
    if len(words) < 3 or words[0] != "From":
        continue
    else:
        if words[2] not in daycounts:
            daycounts[words[2]]=1
        else: daycounts[words[2]]+=1

print(daycounts)
