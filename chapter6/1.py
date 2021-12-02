#My answer:
index = -1
x = "string"
while index < len(x):
    letter = x [index]
    print (index, letter)
    index = index-1


#Correct Answer:
x = "string"
index = len(x)-1
while index >= 0:
    letter= x[index]
    print(index, letter)
    index=index-1
