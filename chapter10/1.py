fname = input("Enter file: ")
if len(fname)<1: fname='/Users/langework/Desktop/py4e/downloadz/mbox-short.txt'
try: fhand = open(fname)
except:
    print("File error: ", fname)
    exit()

mailcounts = dict()
for line in fhand:
    words = line.split()
    if len(words)<3 or words[0]!= "From":
        continue
    else: mailcounts[words[1]]=mailcounts.get(words[1], 0)+1

sortedmailcounts = sorted([(v,k) for k,v in mailcounts.items()],reverse=True)
print(sortedmailcounts[0])
