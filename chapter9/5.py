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
        x= words[1][words[1].find("@"):]
        addresscounts[x]=addresscounts.get(x,0)+1
        #print(x)
    #if x not in addresscounts: addresscounts[x]= 1
    #else: addresscounts[x]+=1

bignumber = None
bigmail = None
for keyz in addresscounts:
    if bignumber is None or addresscounts[keyz] > bignumber:
        bignumber = addresscounts[keyz]
        bigmail = keyz
    else: continue

print("The domain ", bigmail, "was used ", bignumber, "times")
