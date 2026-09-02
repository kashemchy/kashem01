# ticket checker
ticket = "yes"
tick = input("enter Y/N: ")
age = int(input("Your age"))

if tick == "yes":
    print("ticket is ok ! get in")

    if age<10:
        print("You will get baloon")

    else:
        print("enjoy the zoo!")

else: 
    print("Please buy a ticket")
# --------------------------------------------------

age = 10
money = 500
print("--- Version 1: the second if is INSIDE the first one ---")
if age >= 18:
    print("You are an adult.")
    if money >= 100:
        print("You can buy the ticket.")
print("--- Version 2: the second if is OUTSIDE ---")
if age >= 18:
    print("You are an adult.")
if money >= 100:
    print("You can buy the ticket.")






