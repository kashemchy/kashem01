# your_name = input("Your name here: ")

name = input("Enter your name: ")

file = open("name.txt", "w")
file.write(name)
file.close()

print("Name saved successfully")

