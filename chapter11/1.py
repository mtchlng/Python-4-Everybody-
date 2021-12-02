fname = input("Enter file: ")
if len(fname) < 1: fname = "/Users/langework/Desktop/py4e/downloadz/mbox.txt"
try: fhand = open(fname)
except:
    print("Error ", fname)
    quit()

import re
counter = 0
x=input("Enter regex: ")
for line in fhand:
    line=line.rstrip()
    if re.search(x, line):counter+=1

print("mbox.txt had ", counter, "lines that matched ", x)
