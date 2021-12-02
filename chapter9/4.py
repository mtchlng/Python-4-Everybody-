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
        addresscounts[words[1]] = addresscounts.get(words[1],0)+1
        #if words[1] not in addresscounts:
        #    addresscounts[words[1]]=1
        #else: addresscounts[words[1]]+=1

largest = None
largestaddress = None
for keyz in addresscounts:
    if largest is None or addresscounts[keyz]>largest:
        largest =  addresscounts[keyz]
        largestaddress = keyz
    else: continue
print("The highest mail count was ", largest, " which was from ", largestaddress)

#    x = x.rstrip()
#    x = x.translate(x.maketrans('','',string.punctuation))
#    x = x.lower()
