
# 1) --------------------------------

rain = "yes"
rains = input("rain yes or not: ")

if rains == "yes" or rains == "no":
    if rain=="yes":
        print("Take an Umbrella")

    else:
        print("You can go outside without umbrella")
else:
    print("Check the details")

# 2)---------------------------------


ticket = input("Enter ticket number:")
age = int(input("Ener your age: "))

if ticket == "12":
    print ("Ticket is ok come in!")

    if age >= 10:
        print("you will not get any ballon")
    else:
        print("you will get ballon")
else: 
    print("need to buy ticket")


# 3) --------------------------------------------

ages = int(input("Enter your age: "))
money = 500

print(" Version 1: the second if is INSIDE the first one")

if ages >= 10:
    print("you are an adult")
    if money >= 300:
        print("you can buy a ticket")

print(" Version 2: the second if is OUTSIDE")
if ages >= 10:
    print("you are an adult")
if money >= 100:
    print("you can buy a tickets")

# 4) ---------------------------------------

if ages >= 18:
    nid = input("Do you have an NID?  (Yes/No): ")
    if nid == "yes":
        print("you can Vote")
    else: 
        print("Get you NId first, then you can Vote.")
else:
    print("You are not 18, wait for few days!")


# 5)----------------------------

username = input("Enter username: ")

if username:
    password = input(("Password"))

    if password == "123":
        print("Login Successful: welcome", username)
    else:
        print("wrong Password")
else:
    print("username Cannot be empty")


# 5) -----------------------------------------------

namess = input("What is your name?")

if namess:
    print("hello", namess)
    print(f"hello {namess}")

else: 
    print("you did not write your name!")




















