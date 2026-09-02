name = input("Student name: ")
student_id = input("Student ID: ")

bangla = float(input("Bangla marks: "))
english = float(input("English marks: "))
math = float(input("Math marks: "))

total = bangla + english + math
average = total / 3

print("\n----- Student Report -----")
print(f"Name    : {name}")
print(f"ID      : {student_id}")
print(f"Bangla  : {bangla}")
print(f"English : {english}")
print(f"Math    : {math}")
print(f"Total   : {total}")
print(f"Average : {average:.2f}")
