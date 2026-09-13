#Problem 1: Simple Function
# Write a Python program that:
# ● Create a function named greet().
# ● The function takes a person's name as a parameter.
# ● Print a greeting message using the name.
# ● Call the function with any name.

def greet(name):
    print(f"Hello {name}, How are you?")

#greet(input("Name Here: "))
greetings = greet(input("Name Here: "))



# Problem 2: Simple File Writing
# Write a Python program that:
# ● Ask the user to enter their name.
# ● Open a file named name.txt.
# ● Write the name into the file.
# ● Close the file.


# your_name = input("Your name here: ")

name = input("Enter your name: ")

# file = open("name.txt", "w")
# file.write(name)
# file.close()

# print("Name saved successfully.")


file = open("name.txt", "w")
file.write(name)
file.close()
print("Name saved successfully")





