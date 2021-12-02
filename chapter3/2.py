score = float(input("Enter number between 0~1: "))
if score >= .9 and score <=1:
    print("A")
elif score >= .8 and score <=1:
    print("B")
elif score >= .7 and score <=1:
    print("C")
elif score >= .6 and score <=1:
    print("D")
elif score < .6 and score >=0:
    print("F")
elif score > 1 or score < 0:
    print("error oops")
