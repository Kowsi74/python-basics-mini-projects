name = input("Enter student name: ")

maths = float(input("Enter Maths mark: "))
python = float(input("Enter Python mark: "))
dsa = float(input("Enter DSA mark: "))
genai = float(input("Enter GenAI mark: "))

total = maths + python + dsa + genai
average = total / 4
percentage = (total / 400) * 100

print("\n--- Student Report ---")
print(f"Name       : {name}")
print(f"Total      : {total:.2f}")
print(f"Average    : {average:.2f}")
print(f"Percentage : {percentage:.2f}%")
