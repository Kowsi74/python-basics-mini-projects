# Student Eligibility & Grade Checker
# This program takes student details, checks eligibility, and assigns grades

# Number of students to enter
num_students = int(input("Enter number of students: "))

# Counters for grades
count_top = 0
count_B = 0
count_C = 0
count_not_eligible = 0

for i in range(num_students):
    print(f"\n--- Student {i+1} ---")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))

    # Check eligibility
    if age < 18 or marks < 50:
        print(f"{name}: NOT ELIGIBLE")
        count_not_eligible += 1
    elif marks >= 90:
        print(f"{name}: TOP GRADE")
        count_top += 1
    elif marks >= 75 and age >= 18:
        print(f"{name}: GRADE B")
        count_B += 1
    else:
        print(f"{name}: GRADE C")
        count_C += 1

# Summary report
print("\n--- Summary ---")
print(f"Top Grade students: {count_top}")
print(f"Grade B students: {count_B}")
print(f"Grade C students: {count_C}")
print(f"Not Eligible students: {count_not_eligible}")
