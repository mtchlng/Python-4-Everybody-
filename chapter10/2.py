fname = input("Enter file: ")
if len(fname) < 1: fname = "/Users/langework/Desktop/py4e/downloadz/mbox-short.txt"
try: fhand = open(fname)
except:
    print("Error ", fname)
    quit()

hourcounts = dict()
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != "From": continue
    else:
        t = str(words[5])
        hr = t.split(":")
        hourcounts[hr[0]] = hourcounts.get(hr[0], 0) + 1

hoursort = sorted(hourcounts.items())
for k,v in hoursort:
    print(k,v)
