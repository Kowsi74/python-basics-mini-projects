marks = int(input())
age = int(input())

if age < 18 or marks < 50 :
    print("NOT ELIGIBLE")
elif marks >= 90:
    print("TOP GRADE")
elif marks >= 75 and age >= 18 :
    print("GRADE B")
else:
    print("GRADE C")