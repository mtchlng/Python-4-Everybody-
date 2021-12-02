fhand = open('/Users/langework/Desktop/py4e/downloadz/mbox-short.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    line = line.split()
    if len(line)==0 : continue
    if line[0] != "From": continue
    print(line[1])
    count = count + 1
print(count)
