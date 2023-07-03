marks = int(input("Enter your marks: "))

if 100 >= marks >= 80:
    print(f"Your {marks} is a grade A")

elif 80 > marks >= 65:
    print(f"Your {marks} is a grade B")

elif 65 > marks >= 50:
    print(f"Your {marks} is a grade C")

elif 50 > marks >= 40:
    print(f"Your {marks} is a grade D")

elif 40 > marks >= 0:
    print(f"Your {marks} is a Fail")

else:
    print(f"Your {marks} is invalid")
