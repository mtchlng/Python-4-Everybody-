fname = input("Enter file: ")
if len(fname) < 1: fname = "/Users/langework/Desktop/py4e/downloadz/mbox-short.txt"
try: fhand = open(fname)
except:
    print("Error ", fname)
    quit()

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
import re
hourcounts = dict()
for line in fhand:
    line = line.rstrip()
#The following code successfully pulls the lines i want
#    if re.search('^From .*([0-9][0-9]):', line): print(line)
    hour = re.findall('^From .* ([0-9][0-9]):', line)
    if len(hour)!=1:continue
    hourstring = str(hour[0])
    hourcounts[hourstring] = hourcounts.get(hourstring,0)+1

hoursort = sorted(hourcounts.items())
for k,v in hoursort:
    print(k,v)
