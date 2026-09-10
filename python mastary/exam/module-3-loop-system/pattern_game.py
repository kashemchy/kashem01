# Step 2: Start the Program

print("=================================================")
print("Welcome to Pattern Game")
print("=================================================")

# Step 3: Create a Number Pattern

number = int(input("Enter a number: "))

for i in range(1,number + 1):
    for k in range(1, i + 1):
        print(k, end="")
    print()

# Step 4: Create a Reverse Pattern
for i in range(number, 0, - 1):
    for p in range(1, i + 1):
        print(p, end="")
    print()

#  Step 5: Countdown

countdown = int(input("Enter countdown number: "))

while countdown > 0:
    print(countdown)
    countdown = countdown - 1

print("Game Started!")


#  Step 6: Star Pattern

for i in range(1, number + 1):
    for kp in range(i):
        print("*", end="")
    print()


 #Step 6: Reverse Star Pattern

for i in range(number, 0, -1):
    for w in range(1, i + 1):
        print("*", end ="")
    print()

# Step 7: Loop Challenge

count = 1

while count <= 5:
    print (count)
    count = count +1

# Why does this loop never stop?  Reason: The value of count is not changing, so the loop will run forever.


print("=================================================")
print("Thanks")
print("=================================================")

