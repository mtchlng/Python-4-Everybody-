try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
    if hours > 40:
        pay = float((40*rate)+(hours-40)*(rate*1.5))
        print(pay)
    else:
        pay = hours*rate
        print(pay)
except:
    print("Enter a number numbnuts")
