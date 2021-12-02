tt = []
while True:
    x = input('Enter number or "done" to finish > ')
    if x == 'done' :
        break
    try:
        x = float(x)
        tt.append(x)
    except:
        print("Invalid input")
        continue

print('Smallest is ',min(tt), 'Largest is ',max(tt))
