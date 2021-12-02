list = []
fhand = open('/Users/langework/Desktop/py4e/downloadz/romeo.txt')
for line in fhand:
    words = line.split()
    for eachword in words:
        if eachword in list: continue
        list.append(eachword)
print(sorted(list, key=str.lower))
