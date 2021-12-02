count = 0
sum = 0
fname = input("Enter file name: ")
fhand = open (fname)
for line in fhand :
    line=line.rstrip()
    if line.startswith("X-DSPAM-Confidence: "):
        count = count + 1
        number = float(line[len("X-DSPAM-Confidence: ")-1: ])
        print(number)
        #Can the previous 2 lines be combined?
        sum = sum + number

average = sum / count
print(count, sum, average)



fname = open ("/Users/langework/Desktop/py4e/downloadz/mbox-short.txt")
try:
    fhand = open("fname")
except:
    print('File cannot be opened: ', fname)
    quit()
if fname == "na na boo boo":
    print("Fuck yourself bro")
    quit()
