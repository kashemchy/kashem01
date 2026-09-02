# Step 2: Welcome Message

print("Welcome to Smart Eligibility & Performance Checker")


# Step 3: User Input Section

name = input("Enter Your Name Here: ")
age = int(input("Enter Your Age Here: "))
exam_score =  float(input("Enter Your Exam Score(0-100): "))
monthly_income = float(input("Enter Your Monthly Income: "))

# Step 4: Age Eligibility Check

if age < 18:
    print("You are not eligible due to age restrictions.")
else:
    print("Age requirement passed.")

# Step 5: Score Evaluation (Using elif)

# score = int(input("Enter marks here: "))

if exam_score >= 90:
     print("Grade: A")
     grade = "A"
elif exam_score >= 75:
     print("Grade: B")
     grade = "B"
elif exam_score >= 60:
     print("Grade: C")
     grade = "C"
else:
     print("Grade: F")
     grade = "F"

# Step 6: Financial Support Check

# income= int(input("Income Here: "))
# score_above= int(input("Score Here: "))

if monthly_income < 20000 and exam_score >75 :
     print("Eligible for scholarship support.")
     scholarship = "Eligible"
else:
     print("Not eligible for scholarship.")
     scholarship = "Not Eligible"


# Step 7: Nested Condition (Advanced)

# age = int(input("Enter Your age Here: "))
# total_score = int(input("Enter Your Score Here: "))

if age>= 18:
    if exam_score >= 60:
      print ("You passed the program.")
    else:
      print ("You failed the program.")
else:
    print ("Program access denied.")


# Step 8: Final Summary Output

print("Name:", name)
print("Age:", age)
print("Score:", exam_score)
print("Grade:", grade)
print("Scholarship Eligibility:", scholarship)






