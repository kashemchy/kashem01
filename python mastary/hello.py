# print("Assalamu Alaikum")
# print("My name is", "kashem!")
# print("I am", 22, "years old")
# print("2026","Aug", "20", sep="-")
# print("2026","Aug", "20", sep="===")
# print("2026","Aug", "20", sep="@")
# print("Loading")
# print(".")
# print(".")
# print(".",end="1")
# print("load ne",end="1")
# print(".",end=".")
# print()  
# print("Total Cost:",1+2+3)
# print("Total Cost:","1+2+3")
# print("Total Cost:","1+2*3")

# name = input("Enter your name:")
# print(name)

# age_text = input("Enter your age:")
# print("your age:",type(age_text))
# print("your age:",age_text)

# city = "Syhet"
# print("city", city, "ID = ", id(city))


# ====================================================================

# print("My name is kashem","chowdhry", end=".", sep="-")
# print("loading", end="--------")
# print(type("25"))
# print(type(25))

# age_text = input("how old are you? ")
# print("Your Age:", age_text)
# print("Whta is the type of this text:", type(age_text))
# print("age_text + age_text :", age_text + age_text)

# name = " kashem Chowdhury"
# age = 25
# height = 5.6
# is_student = True

# print("type(name) =", type(name))
# print("My name is: ",name)
# ----------------------------------------------------------------------

price = {float(input("Price: "))}
quantity = {int(input("Quantity: "))}

# total = price * quantity

# print(f"Total: {total:.2f}")

# -------------------------------------------------
name = input("Enter Your name: ")
age = int(input("Your age: "))
city = input("Enter your City : ")
next_year = age + 1
next_after_five_years = age + 5


print("\n ------------Personal Information-----------\n")
print(f"Name : {name}")
print(f"age : {age}")
print(f"city : {city}")
print(f"Next year: {next_year}")
print(f"After Five years: {next_after_five_years}")


# -------------------------------------------------

num1 = float(input("Enter first Number: "))
num2 = float(input("Enter your Number: "))

add = num1 + num2
sub = num1 - num2
multi = num1 * num2
divi = num1/+ num2

print("\n----------Calculator-----------\n")

print(f"Adittion : {add}")
print(f"Subtraction : {sub}")
print(f"Multiplication : {multi}")
print(f"Division : {divi}")



# -------------------------------------------------------

math = float(input("Math Marks: "))
science = float(input("Science Marks: "))
english = float(input("Esnglish Marks: "))

total = math + science + english
avarage = total / 3

print("\n----------Result---------\n")

print(f"Total: {total}")
print(f"Avarage: {avarage:.2f}")


# -------------------------------------------------------

product = input("Product name: ")
price = float(input("Price name: "))
quantity = int(input("Quantity name: "))


subtotal = price * quantity
vat = subtotal * 0.15
total = subtotal + vat

print("\n------- Shopping Bill ---------\n")

print(f"Product : {product}")
print(f"Price : {price:.2f}")
print(f"Quantity : {quantity}")
print(f"Subtotal : {subtotal}")
print(f"Vat : {vat}")
print(f"Total : {total}")


# ---------------------------------------------------------

celsius = float(input("Enter temperature in Celsius: "))
fahrenhite = (celsius * 9 / 5) + 32

print(f"{celsius}c = {fahrenhite:.2f}f")

# ------------------------------------------------------

monthly_salary = float(input("Enter your Monthly salary: "))

yearly_salary = monthly_salary * 12
bonus = yearly_salary * 0.10
total = monthly_salary + bonus

print("\n----------Salary Information----------\n")

print(f"MOnthly Salary : {monthly_salary:.2f}")
print(f"Yearly Salary : {yearly_salary:.2f}")
print(f"Bonus : {bonus:.2f}")
print(f"Total : {total:.2f}")

# --------------------------------------------

weight = float(input("Enter your Weight (kg): "))
height = float(input("Enter your height (m): "))


bmi = weight / (height ** 2)

print(f"Your Bmi: {bmi:.2f}")


# --------------------------------------------------

food_price = float(input("Enter Food Price: "))
quantitys = int(input("quantity: "))

subs = food_price * quantity
vats = subs * 0.15
service_charge = subs * 0.05
totals = subs + vats + service_charge


print("\n------ Restaurant bill --------\n")

print(f"Subtotal : {subs:.2f}")
print(f"VAT : {vats:.2f}")
print(f"Service Charge : {service_charge:.2f}")
print(f"Total : {totals:.2f}")


# -----------------------------------------------------------


ages = int(input("Enter your age: "))

if age >= 20:
    print("you can go ourside")
else:
    print("you cannot")


# if condition:
#     body
# else: 
#     body


nums = int(input("Enter number: "))

if nums % 2 == 0:
    print("This is even")
else:
    print("This is Odd")


pin = int(input("Enter pin: "))

if pin == 123456789:
    print("Access!")
else:
    print("Denied!")




marks = int(input("Marks: "))

if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("-A")
elif marks >= 50:
    print("B")
elif marks >= 40:
    print("C")
else:
    print("F")


a = int(input("Number 1: "))
b = int(input("Number 2: "))

print(f"{a} > {b} ->", a > b)
print(f"{a} >= {b} ->", a >= b)
print(f"{a} < {b} ->", a < b)
print(f"{a} <= {b} ->", a <= b)
print(f"{a} == {b} ->", a == b)
print(f"{a} != {b} ->", a != b)


year = int(input("Year : "))

if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
    print("leap Year")
else:
    print("Nota Leap year")


# if pin == 123456789:
#     print("Access!")
# elif chondition:

# else:
#     print("Denied!")



# produch = input("Inter your Porduct name: ")
# price = float(input("Enter Price: "))
# Qualntity = int(input("Enter quantity: "))

# subtotal = price * Qualntity

# vat = subtotal * 0.15

# total = subtotal + vat

# print(f"Product: {produch}")
# print(f"Price: {price:.2f}")
# print(f"Quantity: {Qualntity}")
# print(f"Subtotal: {subtotal}")
# print(f"VAT: {vat:.2f}")
# print(f"Total: {total}")




# Weight = float(input("Enter Weight: "))
# height = float(input("Enter Height: "))

# bmi = Weight / (height ** 2)

# print(f"BMI : {bmi:.2f}")


















