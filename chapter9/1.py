fhand = open('/Users/langework/Desktop/py4e/downloadz/mbox.txt')
mydict = dict()
for line in fhand:
    words = line.split()
    for word in words:
        mydict[word]= None #Adds the word to the dictionary. Duplicates are replaced.

if 'All' in mydict: print("yes dingus")
else: print("nah buddy")


#Good for finding full isolated words
#Extremely limited search function. Can NOT find:
#parts of words, words combined with periods/commas/backslashes etc.
