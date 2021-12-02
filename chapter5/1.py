sum = 0
count = 0
while True:
    x = input('Enter number > ')
    if x == 'done' :
        break
    try:
        x = float(x)
        count = count + 1
        sum = sum + x
        continue
    except:
        print("Error: Not a valid number dingus")
        continue

print(count, sum, sum/count)
