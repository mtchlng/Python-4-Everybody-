fname = input("Enter file: ")
if len(fname) < 1: fname = "/Users/langework/Desktop/py4e/downloadz/mbox.txt"
try: fhand = open(fname)
except:
    print("Error ", fname)
    quit()

import re
lst = []
for line in fhand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9]+)', line)
    if len(x)!=1: continue
    x = int(x[0])
    lst.append(x)
    print(lst)

avg= sum(lst)/len(lst)
print(avg)
