min = None
max = None
while True:
    x = input('Enter number > ')
    if x == 'done' :
        break
    try:
        floatx = float(x)
        if min is None:
            min = floatx
        if floatx < min:
            min = floatx
        if max is None:
            max = floatx
        if floatx > max:
            max = floatx
        continue
    except:
        print("Error: Not a valid number dingus")
        continue

print('Smallest is ',min, 'Largest is ',max)
