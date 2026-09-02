# Step 1: Project Setup
#  Folder has been created 



# 02) Program Introduction

print("Welcome to Daily Life Tracker Program")


# Step 3: User Information Section


user_name = input("Enter Your Name : ")
available_hours = float(input("Available hours : "))
daily_budget = float(input("Your Daily Budget : "))


print(f"Your Name : {user_name}")
print(f"Available Hours : {available_hours}")
print(f"Daily Budget : {daily_budget}")


# Step 4: Daily Activity Input

studying_python = float(input("How many hours you will spend on Studying Python :  "))
practicing_coding = float(input("How many hours you will spend on Practicing coding :  "))
other_activities = float(input("How many hours you will spend on Other activities :  "))

total_activity =  studying_python + practicing_coding + other_activities

print(f"Total Activity: {total_activity}")

# Step 5: Expense Input


food_exp = float(input("Enter your Food Expense : "))
transport_exp = float(input("Enter your Transportation expense : "))
other_exp = float(input("Enter your Other expense : "))


calculate =  food_exp + transport_exp + other_exp

print(f"Total Expense : {calculate:.2f}")


# Step 6: Time Planning Check (optional) 
# Compare:

# Total planned hours with available hours.

# If planned hours are greater:

# Print:

# "You have planned more hours than available."

# Else:

# "Your daily plan is realistic."

planned_hours = int(input("Enter hours : "))

if planned_hours > 4:
    print("You have planned more hours than available.")
else:
    print("Your daily plan is realistic.")




# Step 7: Budget Check(optional) 


total_expenses = int(input("Total Expance: "))

if total_expenses > 1000:
    print("You have exceeded your daily budget.")
else:
    print("You are within your daily budget.")


# Step 8: Final Summary Output


users_name = input("Enter your name: ")
planned_hours = float(input("Planned hours: "))
available_hours = int(input("Available hours : "))
total_expense = int(input("Total Expance: "))
remaining_budget = int(input("Remaining budget: "))


print(f"User name : {users_name}")
print(f"Planned hours : {planned_hours}")
print(f"Available hours : {available_hours}")
print(f"Total expenses : {total_expense}")
print(f"Remaining Budget : {remaining_budget}")


#  Step 9: Debugging Practice
# Before final submission:

# ✔ Remove a quotation mark
# ✔ Remove a bracket

# Run the program and observe the error message.

# Fix the error and make the program run successfully again.

# This step is important for building real developer debugging skills.






















