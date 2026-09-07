#1  Takes a student's name as input.

name =input("Student Name here: ")

#2 Takes marks for 3 subjects

bangla = 75
eng = 78
math = 84

#Calculates:

total_marks = bangla + eng + math
average_marks = total_marks / 3

print("Total Marks Here: ", total_marks)
print("Average Marks Here: ", average_marks)

#4 Determines the grade using:

if total_marks >= 80 and total_marks <= 100:
    print("Grade: A+")
elif total_marks >= 70:
    print("Grade: A")
elif total_marks >= 60:
    print("Grade: B")
elif total_marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# 2: Simple Shopping Cart
customer_name = input("Write your name here: ")
product_name = input("Write product 1 name here: ")
product_price1 = float(input("Write product 1 price here: "))
product_name = input("Write product 2 name here: ")
product_price2 = float(input("Write product 2 price here: "))
product_name = input("Write product 3 name here: ")
product_price3 = float(input("Write product 3 price here: "))

subtotal = product_price1 + product_price2 + product_price3
print(f"Subtotal: {subtotal}")
if subtotal >= 5000:
    discount = subtotal * 0.20
    print(f"discount: {discount}")
elif subtotal >= 3000:
    discount = subtotal * 0.10
    print(f"discount: {discount}")
elif subtotal >= 1000:
    discount = subtotal * 0.05
    print(f"discount: {discount}")
else:
    print(f"No discount")


final_total = subtotal - discount

print(f"Final total: {final_total}")