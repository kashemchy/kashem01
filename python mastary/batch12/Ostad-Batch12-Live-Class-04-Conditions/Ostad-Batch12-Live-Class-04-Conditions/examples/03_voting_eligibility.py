# Voting Eligibility Checker
# Concepts used: input(), int(), if-else, logical operator 'and'

age = int(input("Enter your age: "))
has_id_card = input("Do you have an NID? (yes/no): ")

if age >= 18 and has_id_card == "yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
