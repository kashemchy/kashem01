math = float(input("Enter your Math marks: "))
science = float(input("Enter your Math marks: "))
english = float(input("Enter your Math marks: "))


total = math + science + english;

if (math < 0 or math > 100) or (science < 0 or science > 100) or (english < 0 or english > 100):
    print("invalide marks")
else:
    total = math + science + english
    average = total / 3


    print("toatal: ", total)
    print("avarage: ", average)

    if math < 40 or science < 40 or english < 40:
        print("Grade F")
        if math > 40:
            print("Needs more pracitce")
        if english > 40:
            print("Needs E more pracitce")
        if science > 40:
            print("Needs  S more pracitce")
    elif average >= 80:
        print("Grade A+")
    elif average >= 70:
        print("Grade A")
    elif average >= 60:
            print("Grade B")
    elif average >= 50:
        print("Grade C")
    elif average >= 50:
        print("Grade D")
    else:
        print("Grade Pass")
if math >= 90 and english >= 90 and science >= 90:
    print("Execellent! Greate job in every subject")


age = int(input("Age: "))

if age < 0:
    print("Age cannot be negative. Please try again!")
elif age <=12:
    print("Pichi")
elif age <= 19:
    print("Teenager")
    school = input("Are you in school? (Yes/No)")

    if school.lower() == "yes":
        print("Great! Keep Studing.")
    else:
        print("Try to go back to school")
elif age <= 59:
    print("Adult")
    nid = input("Do you have an NID? (Yes / No)")
    if age >= 18 and nid.lower() == "yes":
        print("you can Vote!")
    else:
        print("YOu cannot Vote!")
else: 
    print("Catagory: Senior citizen")
    print("Enjoy your Special benefits!")






















