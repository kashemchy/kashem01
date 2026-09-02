# Live Class 03: Practice & Debugging

> **Batch:** Mastering Python: From Zero to Hero (Batch 12)  
> **Module:** Module 1 - Getting Started with Python & Programming World  
> **Live Class:** 03 of 03  
> **Duration:** ৯০ মিনিট  
> **Prerequisite:** Live Class 02 - `print()`, `input()`, Variables, Data Types, Type Conversion, Operators ও f-string

---

## Class Overview

আজকের ক্লাসে নতুন কোনো বড় topic যোগ করা হবে না।

Live Class 02-তে শেখা concept-গুলোকে ব্যবহার করে আমরা **নিজে হাতে ছোট ছোট program লিখব**, problem solve করব এবং common error/debugging practice করব।

আজকের মূল pattern:

```text
INPUT → PROCESS → OUTPUT
```

Class 02-তে এই pattern-এর concept শেখা হয়েছে। আজ সেটাই practice করা হবে।

---

# Learning Objectives

এই ক্লাস শেষে students পারবে:

- `input()` ব্যবহার করে user-এর কাছ থেকে data নিতে
- প্রয়োজন অনুযায়ী `int()` ও `float()` ব্যবহার করতে
- variable ব্যবহার করে data process করতে
- arithmetic operator দিয়ে calculation করতে
- f-string দিয়ে সুন্দর output তৈরি করতে
- ছোট real-life problem-কে INPUT → PROCESS → OUTPUT এ ভাঙতে
- common `SyntaxError`, `TypeError`, `ValueError`, `NameError` চিনতে
- error message পড়ে basic debugging করতে
- নিজে হাতে একটি ছোট complete program লিখতে

> **আজ `if`, `elif`, `else` লাগবে না।**  
> Condition বা decision-making পরের Module-এর topic।

---

# 1. Quick Revision

## `print()`

```python
print("Hello")
print("Name:", "Rahim")
```

## `input()`

```python
name = input("Enter your name: ")
```

মনে রাখবেন:

```text
input() → সবসময় str
```

## Type Conversion

```python
age = int(input("Enter your age: "))
price = float(input("Enter price: "))
```

## Variable

```python
price = 500
quantity = 3
```

## Arithmetic Operators

```text
+    Addition
-    Subtraction
*    Multiplication
/    Division
//   Floor Division
%    Remainder
**   Power
```

## f-string

```python
name = "Rahim"
age = 25

print(f"My name is {name}. I am {age} years old.")
```

---

# 2. The Basic Programming Pattern

যেকোনো beginner-level problem দেখলে আগে তিনটি প্রশ্ন করুন।

### INPUT

কী কী data লাগবে?

### PROCESS

Data নিয়ে কী calculation করতে হবে?

### OUTPUT

শেষে কী result দেখাতে হবে?

---

## Example

Problem:

> একটি product-এর total price বের করতে হবে।

### চিন্তা

```text
INPUT
price
quantity

PROCESS
price × quantity

OUTPUT
total
```

### Code

```python
price = float(input("Price: "))
quantity = int(input("Quantity: "))

total = price * quantity

print(f"Total: {total:.2f}")
```

---

# 3. Example: Personal Information

## Problem

User-এর কাছ থেকে:

- Name
- Age
- City

নিয়ে সুন্দরভাবে print করতে হবে।

## Code

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("\n----- Personal Information -----")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"City : {city}")
```

## Example Output

```text
Enter your name: Rahim
Enter your age: 22
Enter your city: Dhaka

----- Personal Information -----
Name : Rahim
Age  : 22
City : Dhaka
```

**Python file:** `examples/example_01_profile.py`

---

# 4. Example: Age Calculator

## Problem

Current age input নিয়ে:

- Current age
- Next year's age
- 5 years পরে age

দেখাতে হবে।

## Code

```python
age = int(input("Enter your age: "))

next_year = age + 1
after_five_years = age + 5

print(f"Current age   : {age}")
print(f"Next year     : {next_year}")
print(f"After 5 years : {after_five_years}")
```

## Example Output

```text
Enter your age: 25

Current age   : 25
Next year     : 26
After 5 years : 30
```

**Python file:** `examples/example_02_age_calculator.py`

---

# 5. Example: Basic Calculator

## Problem

দুটি number input নিয়ে:

- Addition
- Subtraction
- Multiplication
- Division

calculate করতে হবে।

## Code

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print("\n----- Calculator -----")
print(f"Addition       : {addition}")
print(f"Subtraction    : {subtraction}")
print(f"Multiplication : {multiplication}")
print(f"Division       : {division}")
```

## Example Output

```text
Enter first number: 20
Enter second number: 5

----- Calculator -----
Addition       : 25.0
Subtraction    : 15.0
Multiplication : 100.0
Division       : 4.0
```

**Python file:** `examples/example_03_calculator.py`

---

# 6. Example: Student Marks Calculator

## Problem

তিনটি subject-এর marks input নিয়ে:

- Total
- Average

calculate করতে হবে।

## Code

```python
bangla = float(input("Bangla marks: "))
english = float(input("English marks: "))
math = float(input("Math marks: "))

total = bangla + english + math
average = total / 3

print("\n----- Result -----")
print(f"Total   : {total}")
print(f"Average : {average:.2f}")
```

## Example Output

```text
Bangla marks: 80
English marks: 75
Math marks: 90

----- Result -----
Total   : 245.0
Average : 81.67
```

**Python file:** `examples/example_04_marks_calculator.py`

> এখানে Grade বা Pass/Fail বের করা হচ্ছে না। কারণ তার জন্য condition দরকার, যা এখনো শেখানো হয়নি।

---

# 7. Example: Shopping Bill

এটি একটি গুরুত্বপূর্ণ real-life example।

## Problem

Input:

- Product name
- Price
- Quantity

Process:

- Subtotal
- 15% VAT
- Final total

## Code

```python
product = input("Product name: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))

subtotal = price * quantity
vat = subtotal * 0.15
total = subtotal + vat

print("\n----- Shopping Bill -----")
print(f"Product  : {product}")
print(f"Price    : {price:.2f}")
print(f"Quantity : {quantity}")
print(f"Subtotal : {subtotal:.2f}")
print(f"VAT      : {vat:.2f}")
print(f"Total    : {total:.2f}")
```

## Example Output

```text
Product name: Keyboard
Price: 1500
Quantity: 2

----- Shopping Bill -----
Product  : Keyboard
Price    : 1500.00
Quantity : 2
Subtotal : 3000.00
VAT      : 450.00
Total    : 3450.00
```

**Python file:** `examples/example_05_shopping_bill.py`

---

# 8. Example: Temperature Converter

## Problem

Celsius input নিয়ে Fahrenheit বের করতে হবে।

Formula:

```text
Fahrenheit = (Celsius × 9 / 5) + 32
```

## Code

```python
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C = {fahrenheit:.2f}°F")
```

## Example Output

```text
Enter temperature in Celsius: 30

30.0°C = 86.00°F
```

**Python file:** `examples/example_06_temperature_converter.py`

### Practice

এবার Fahrenheit থেকে Celsius বের করার code নিজে লিখুন।

Formula:

```text
Celsius = (Fahrenheit - 32) × 5 / 9
```

---

# 9. Example: Salary Calculator

## Problem

Monthly salary input নিয়ে:

- Yearly salary
- 10% bonus
- Salary + bonus

calculate করতে হবে।

## Code

```python
monthly_salary = float(input("Enter monthly salary: "))

yearly_salary = monthly_salary * 12
bonus = yearly_salary * 0.10
total = yearly_salary + bonus

print("\n----- Salary Information -----")
print(f"Monthly Salary : {monthly_salary:,.2f}")
print(f"Yearly Salary  : {yearly_salary:,.2f}")
print(f"Bonus          : {bonus:,.2f}")
print(f"Total          : {total:,.2f}")
```

## Example Output

```text
Enter monthly salary: 45000

----- Salary Information -----
Monthly Salary : 45,000.00
Yearly Salary  : 540,000.00
Bonus          : 54,000.00
Total          : 594,000.00
```

**Python file:** `examples/example_07_salary_calculator.py`

---

# 10. Example: BMI Calculator

আজ BMI-এর category বের করব না।

শুধু calculation practice করব।

## Formula

```text
BMI = weight / (height ** 2)
```

## Code

```python
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

print(f"Your BMI: {bmi:.2f}")
```

**Python file:** `examples/example_08_bmi_calculator.py`

---

# 11. Example: Restaurant Bill

আরেকটি real-life calculation problem।

## Problem

Input:

- Food price
- Quantity

Calculate:

- Subtotal
- 15% VAT
- 5% Service Charge
- Final Total

## Code

```python
food_price = float(input("Food price: "))
quantity = int(input("Quantity: "))

subtotal = food_price * quantity
vat = subtotal * 0.15
service_charge = subtotal * 0.05
total = subtotal + vat + service_charge

print("\n----- Restaurant Bill -----")
print(f"Subtotal     : {subtotal:.2f}")
print(f"VAT (15%)    : {vat:.2f}")
print(f"Service (5%) : {service_charge:.2f}")
print(f"Final Total  : {total:.2f}")
```

**Python file:** `examples/example_09_restaurant_bill.py`

---

# 12. Example: Student Report

এবার কয়েকটি concept একসাথে ব্যবহার করি।

## Code

```python
name = input("Student name: ")
student_id = input("Student ID: ")

bangla = float(input("Bangla marks: "))
english = float(input("English marks: "))
math = float(input("Math marks: "))

total = bangla + english + math
average = total / 3

print("\n----- Student Report -----")
print(f"Name    : {name}")
print(f"ID      : {student_id}")
print(f"Bangla  : {bangla}")
print(f"English : {english}")
print(f"Math    : {math}")
print(f"Total   : {total}")
print(f"Average : {average:.2f}")
```

## Example Output

```text
----- Student Report -----

Name    : Rahim
ID      : 1025
Bangla  : 80.0
English : 75.0
Math    : 90.0
Total   : 245.0
Average : 81.67
```

**Python file:** `examples/example_10_student_report.py`

---

# 13. Debugging Practice

Programming করার সময় error হওয়া normal।

আজ আমরা error দেখে panic না করে error message পড়ব।

## Golden Rule

> **Traceback-এর শেষ লাইন আগে পড়ুন।**

---

# 14. TypeError

## Wrong Code

```python
age = input("Enter your age: ")

print(age + 5)
```

User:

```text
25
```

সমস্যা:

```text
age → "25" → str
5   → int
```

তাই:

```python
"25" + 5
```

করা যায় না।

## Correct Code

```python
age = int(input("Enter your age: "))

print(age + 5)
```

**Python file:** `examples/example_11_debugging_type_error.py`

---

# 15. ValueError

## Wrong Example

```python
age = int("twenty")
```

Python `"twenty"`-কে integer বানাতে পারবে না।

তাই:

```text
ValueError
```

হবে।

আরেকটি example:

```python
price = int("99.5")
```

এটিও `ValueError`।

কারণ `"99.5"` integer format নয়।

সঠিক:

```python
price = float("99.5")
```

**Python file:** `examples/example_12_debugging_value_error.py`

---

# 16. NameError

## Wrong Code

```python
total = 1500

print(totl)
```

আমরা variable বানিয়েছি:

```python
total
```

কিন্তু ব্যবহার করেছি:

```python
totl
```

## Correct Code

```python
total = 1500

print(total)
```

**Python file:** `examples/example_13_debugging_name_error.py`

---

# 17. SyntaxError

## Wrong Code

```python
name = input("Enter your name: "
```

Opening bracket আছে:

```python
(
```

কিন্তু closing bracket নেই:

```python
)
```

## Correct Code

```python
name = input("Enter your name: ")
```

**Python file:** `examples/example_14_debugging_syntax_error.py`

---

# 18. Error না হলেও Wrong Result

সব ভুল error দেয় না।

Example:

```python
marks = input("Enter marks: ")

print(marks * 3)
```

Input:

```text
50
```

Output:

```text
505050
```

কিন্তু আমরা হয়তো চেয়েছিলাম:

```text
150
```

কারণ:

```python
"50" * 3
```

মানে text তিনবার repeat করা।

Correct:

```python
marks = int(input("Enter marks: "))

print(marks * 3)
```

Output:

```text
150
```

এখান থেকে গুরুত্বপূর্ণ lesson:

> **Program run করলেই program correct হবে না।**

---

# 19. Live Practice

এখন students নিজেরা code লিখবেন।

## Practice 01

Name, age এবং city input নিয়ে Profile Card তৈরি করুন।

---

## Practice 02

দুটি number input নিয়ে:

- Sum
- Difference
- Product
- Average

দেখান।

---

## Practice 03

একটি number input নিয়ে:

- Square
- Cube

দেখান।

Example:

```text
Input: 5

Square: 25
Cube  : 125
```

---

## Practice 04

একটি product-এর:

- Price
- Quantity

নিয়ে total price বের করুন।

---

## Practice 05

Celsius input নিয়ে Fahrenheit বের করুন।

---

## Practice 06

Monthly salary input নিয়ে yearly salary বের করুন।

---

# 20. Challenge

একটি restaurant bill program তৈরি করুন।

Input:

```text
Food price
Quantity
```

Process:

```text
Subtotal
VAT = 15%
Service Charge = 5%
```

Output:

```text
Subtotal
VAT
Service Charge
Final Total
```

**কোনো `if`, `elif`, `else` ব্যবহার করা যাবে না।**

---

# 21. Problem Solving Technique

Problem দেখেই code লেখা শুরু করবেন না।

প্রথমে লিখুন:

```text
INPUT
↓
PROCESS
↓
OUTPUT
```

### Example

Problem:

> একজন student-এর 3টি subject-এর average বের করতে হবে।

### Step 1: INPUT

```text
Bangla
English
Math
```

### Step 2: PROCESS

```text
Total = Bangla + English + Math

Average = Total / 3
```

### Step 3: OUTPUT

```text
Total
Average
```

তারপর code লিখুন।

এভাবেই বড় problem-কে ছোট ছোট অংশে ভাঙতে হয়।

---

# 22. Homework

## Homework 01: Profile Card

নিজের:

- Name
- Age
- City
- Profession

দিয়ে Profile Card তৈরি করুন।

---

## Homework 02: Calculator

দুটি number নিয়ে:

- Addition
- Subtraction
- Multiplication
- Division
- Remainder

calculate করুন।

---

## Homework 03: Shopping Bill

Input:

- Product name
- Price
- Quantity

Output:

- Subtotal
- VAT 15%
- Final Total

---

## Homework 04: Temperature Converter

Celsius → Fahrenheit

এবং

Fahrenheit → Celsius

দুটো conversion করুন।

---

## Homework 05: BMI Calculator

Weight ও Height input নিয়ে BMI calculate করুন।

---

## Homework 06: Student Report

Input:

- Student name
- Student ID
- Bangla marks
- English marks
- Math marks

Output:

- Total
- Average

---

## Homework 07: Debugging

নিজে তিনটি error তৈরি করুন:

```text
SyntaxError
TypeError
ValueError
```

তারপর প্রতিটির কারণ লিখে ঠিক করুন।

---

# 23. Class Summary

আজকের সবচেয়ে গুরুত্বপূর্ণ বিষয়গুলো:

1. `input()` দিয়ে data নেওয়া যায়।
2. `input()` সবসময় `str` return করে।
3. Calculation-এর আগে প্রয়োজন অনুযায়ী `int()` বা `float()` করতে হয়।
4. Variable data store/reference করার জন্য ব্যবহার হয়।
5. Arithmetic operator দিয়ে calculation করা যায়।
6. f-string দিয়ে output সুন্দরভাবে format করা যায়।
7. Basic program-এর common pattern:

```text
INPUT → PROCESS → OUTPUT
```

8. Error হওয়া programming-এর normal অংশ।
9. Traceback-এর শেষ লাইন আগে পড়তে হবে।
10. Program run করলেই result correct হবে এমন নয়।
11. Problem solve করার আগে problem-টাকে ছোট অংশে ভাঙতে হবে।
12. আজকের practice-এ **`if`, `elif`, `else` লাগবে না।**

---

# Next Module

পরের Module-এ আমরা নতুন একটি গুরুত্বপূর্ণ concept শুরু করব:

**Logic & Condition Building**

সেখানে `if`, `elif`, `else`, comparison এবং logical thinking নিয়ে কাজ করা হবে।

আজকের লক্ষ্য:

> **Concept মুখস্থ করা নয়, নিজে হাতে code লিখে problem solve করার confidence তৈরি করা।**
