# Step 2: Program Introduction

print("=======================================")

print("Welcome to Smart Daily Helper Toolkit")

print("=======================================")



# Step 3: Create a Menu


print("Choose a problem to solve:")

print("1. Shopping Budget Checker")
print("2. Electricity Bill Category")
print("3. Student Result & Grade Checker")
print("4. Bus Fare Calculator")
print("5. Exit")

choice = input("Enter your choice: ")

print("You selected:", choice)


# #Step 4: Shopping Budget Checker

your_budget = int(input("Enter your Budget: "))
product_price = int(input("Enter Product Price: "))

if product_price <= your_budget:
    if product_price < your_budget:
         budget_calculate = your_budget -product_price
         print(f"Your can buy this product. you have left {budget_calculate}. you can purchase more")
    elif product_price == your_budget:
             print("Congratulations! you can purchase this product. But If you purchase this product then you will have nothing left based on your budget")
   
elif product_price > your_budget:
    budget_calculate = product_price - your_budget
    print(f"You cannot buy this product. you need {budget_calculate} more")
else: 
      print("Come again for new product")


Step 5: Electricity Bill Category

electricity_units_used = int(input("Enter electricity units used: "))

if electricity_units_used > 0 and electricity_units_used <= 100:
      print("Result: Low Usage")
elif electricity_units_used < 0:
      print("Pleae enter valide Units which you used")
elif electricity_units_used >= 101 and electricity_units_used <= 300:
      print("Result: Mediul Usage")
else:
      print("Result: High Usage")


# Step 6: Student Result & Grade Checker
python_marks = float(input("Enter your Python marks: "))
english_marks = float(input("Enter your English marks: "))
math_marks = float(input("Enter your Math marks: "))


total_marks = python_marks + english_marks + math_marks
avarage_marks = total_marks / 3

print(f"Total: {total_marks}")
print(f"Avarage: {avarage_marks:.2f}")

if avarage_marks >= 80 and avarage_marks <= 100:
    print(f"Grade A+")
elif avarage_marks >= 70 and avarage_marks <= 79:
    print("Grade A")
elif avarage_marks >= 60 and avarage_marks <= 69:
    print("Grade B")
elif avarage_marks >= 50 and avarage_marks <= 59:
    print("Grade C")
elif avarage_marks < 50 and avarage_marks > 40:
    print("Grade F")
else:
    if avarage_marks < 40:
        print("You need to improve your Performance")


# Step 7: Bus Fare Calculator

age = int(input("Enter your age: "))
bus_fare = 100

half_fare = bus_fare * 50 /100

if age < 5:
    print ("Bus Fare is Free")
elif age > 5 and age < 12 :
    print(f"Bus Fare is {bus_fare * 50 /100}")
elif age > 13 and age < 59 :
    print(f"Bus Fare is {bus_fare}")
else: 
    print(f"Bus Fare is Free")

# Step 8: Repeat the Program Using a Loop

while True:

    print("Choose a problem to solve:")
    print("1. Shopping Budget Checker")
    print("2. Electricity Bill Category")
    print("3. Student Result & Grade Checker")
    print("4. Bus Fare Calculator")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Shopping Budget Checker")

    elif choice == "2":
        print("Electricity Bill Category")

    elif choice == "3":
        print("Student Result & Grade Checker")

    elif choice == "4":
        print("Bus Fare Calculator")
    

    elif choice == "5":
        break
    elif choice == "6":
                print("Simple Discount Calculator")

    else:
        print("Invalid choice")

    another = input("Do you want to solve another problem? (yes/no): ")

    if another == "no":
        break
    elif another != "yes" and another != "no" :
            print ("Invalid input")


print("========================================")
print("Thank you for using Smart Daily Helper Toolkit!")
print("========================================")

#  Step 10: Debugging Practice

age = input("Enter age: ")

calculate_age = age + 5

print(calculate_age)

error :  TypeError: can only concatenate str (not "int") to str

solution : 
age = int(input("Enter age: "))

# calculate_age = age + 5

# print(calculate_age)


# Error 2: Missing Colon
# if agess >= 18

#     print("Eligible")
#  SyntaxError: expected ':'

if age >= 18:
    print("Eligible")

#Error 3: Wrong Indentation

if age >= 18:
print("Eligible")

# IndentationError: expected an indented block after 'if' statement on line 175
if age >= 18:
    print("Eligible")




if choice == "6":
    print("Simple Discount Calculator")

    price = float(input("Enter product price: "))

    if price >= 5000:
        discount = price * 20 / 100

    elif price >= 3000:
        discount = price * 10 / 100

    elif price >= 1000:
        discount = price * 5 / 100

    else:
        discount = 0

    final_price = price - discount

    print(f"Original Price: {price:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"Final Price: {final_price:.2f}")



