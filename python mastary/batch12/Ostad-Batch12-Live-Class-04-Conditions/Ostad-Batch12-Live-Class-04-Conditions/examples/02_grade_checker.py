# Grade Checker using if-elif-else
# Concepts used: input(), int(), if-elif-else, comparison operators

marks = int(input("Enter your marks (0-100): "))

if marks >= 80:
    print("Grade: A+")
elif marks >= 60:
    print("Grade: A")
elif marks >= 40:
    print("Grade: Pass")
else:
    print("Grade: Fail")
