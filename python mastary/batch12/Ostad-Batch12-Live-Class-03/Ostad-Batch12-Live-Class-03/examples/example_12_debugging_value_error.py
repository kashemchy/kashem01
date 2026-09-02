# WRONG:
# age = int(input("Enter your age: "))
# If the user enters: twenty
# This causes ValueError.

# FIX:
age = int(input("Enter your age: "))
print(f"Your age is {age}")
