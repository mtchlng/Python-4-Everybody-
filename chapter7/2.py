count = 0
sum = 0
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()
if fname == "na na boo boo":
    print("Fuck yourself bro")
    quit()


for line in fhand :
    line=line.rstrip()
    if line.startswith("X-DSPAM-Confidence: "):
        count = count + 1
        number = float(line[len("X-DSPAM-Confidence: ")-1: ])
        print(number)
        sum = sum + number

average = sum / count
print("There are ", count, " lines, the sum is ", sum, ", and the average is ", average, ".")


#/Users/langework/Desktop/py4e/downloadz/mbox.txt
#/Users/langework/Desktop/py4e/downloadz/mbox-short.txt
