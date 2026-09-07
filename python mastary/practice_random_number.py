import random

# sectret_number = random.randint(1,50)

# print("Picked a number between 1 to 50!")

# print("The number is : ", sectret_number)

secret_number = 31

guess = int(input("Enter your Guess: "))

if guess == secret_number:
    print("correct")
elif guess < secret_number:
    print("higher! try again")
else:
    print("lower! try again")

max_attempt = 3

for attempt in range(1,max_attempt +1):
    guess = int(input(f"attempt: {attempt} Enter your Guess: "))

    if guess == secret_number:
        print("correct")
    elif guess < secret_number:
        print("higher! try again")
    else:
        print("lower! try again")
else:
    print("Guess Lower! try again!")


min_number = 1
max_number = 50
max_attempt = 5

play_again = "yes"

while play_again == "yes":
    secret_numbers = random.randint(min_number, max_number)
    print(f"I'm thinking number between {min_number} and {max_number}")
    print (f"Yu have {max_attempt} attempts. Good lucks!")

    for attempt in range(min_number,max_attempt + 1):
        guesss = int(input(f"Attemt {max_attempt}: Enter your guess:  "))

        if guess == secret_number:
            print(f"Correct! you guessed it in {attempt} attempts")
            break
        elif guess < secret_number:
            print("guess Higher number, please")
        else :
                print("guess Lower number, please")
    play_again = input("Play again? (yes/no)")
print("thanks!")


















