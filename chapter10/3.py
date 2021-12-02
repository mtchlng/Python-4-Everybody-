fname = input("Enter file: ")
if len(fname) < 1: fname = "/Users/langework/Desktop/py4e/downloadz/mbox-short.txt"
try: fhand = open(fname)
except:
    print("Error ", fname)
    quit()

letterz = dict()
i = 0
for line in fhand:
    #Below 4 lines can compress to the hashed out code following
    string = str(line)
    result = ''.join(filter(str.isalpha, string))
    lowresult = result.lower()
    characters = list(lowresult)
    #characters = list((''.join(filter(str.isalpha, str(line)))).lower())
    while i < len(characters):
        letterz[characters[i]] = letterz.get(characters[i], 0) + 1
        i += 1

#To print by alphabetical order
letterzsorted = sorted(letterz.items())
for k,v in letterzsorted:
    print(k,v,)

#Newline to separate two results
print("\n")

#To print by order of value
letterzsortedalpha = sorted([(v,k) for k,v in letterz.items()],reverse=True)
for k,v in letterzsortedalpha:
    print(v,k)
