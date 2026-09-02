# Lab Assignment - 1 (Basics) - Python Version

> Live Class 03 - Practice Session ব্যবহারের জন্য। মূল lab sheet-টি C ভাষায় লেখা ছিল; এখানে প্রতিটি প্রশ্ন **Python-এ** রূপান্তর করে সমাধানসহ দেওয়া হলো। প্রতিটি সমাধান শুধুমাত্র এখন পর্যন্ত শেখা concept (print, input, variable, type conversion, basic expression, ord()/chr(), string method) দিয়ে লেখা - কোনো if/loop/function লাগেনি, কারণ প্রতিটি সমস্যাই straight-line input → process → output প্যাটার্নে সমাধানযোগ্য।
>
> সব কোড রান করে output verify করা হয়েছে।

---

### 1. Write a Python program that will print your name.

```python
print("Abed")
```

**Output:**
```text
Abed
```

---

### 2. Write a Python program that will print your name, your father's and mother's name in three separate lines.

```python
print("Abed")
print("Father: Mahbubur Rahman")
print("Mother: Most. Rawshan Ara Begum")
```

**Output:**
```text
Abed
Father: Mahbubur Rahman
Mother: Most. Rawshan Ara Begum
```

---

### 3. Write a Python program that will print the sum of two variables a and b; where a = 10 and b = 20.

```python
a = 10
b = 20
print("Sum:", a + b)
```

**Output:**
```text
Sum: 30
```

---

### 4. Write a Python program to calculate the sum of two integer numbers (given by the user) and print it.

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)
```

**Output (example):**
```text
Enter first number: 15
Enter second number: 27
Sum: 42
```

---

### 5. Write a Python program that will take three numbers from the user and find their average.

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("Average:", average)
```

**Output (example):**
```text
Enter first number: 10
Enter second number: 20
Enter third number: 30
Average: 20.0
```

---

### 6. Write a Python program that will take three integers as input from the user and print their average. (Use type-cast to get the proper result)

```python
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))
average = float(num1 + num2 + num3) / 3
print("Average:", average)
```

**Output (example):**
```text
Enter first integer: 10
Enter second integer: 20
Enter third integer: 21
Average: 17.0
```

> Note: C-তে int/int সবসময় int দেয় বলে explicit `(float)` cast ছাড়া average ভুল আসত। Python-এ `/` এমনিতেই float ফেরত দেয়, তবুও `float(...)` দিয়ে cast লেখা হলো যাতে "কেন cast লাগে" ধারণাটা স্পষ্ট থাকে।

---

### 7. Write a Python program to convert a Km value into a meter value.

```python
km = float(input("Enter distance in Km: "))
meter = km * 1000
print("Meter:", meter)
```

**Output (example):**
```text
Enter distance in Km: 5.5
Meter: 5500.0
```

---

### 8. Write a Python program to convert a Celsius value into a Fahrenheit value. (Formula: F = C * 9/5 + 32)

```python
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print("Fahrenheit:", fahrenheit)
```

**Output (example):**
```text
Enter temperature in Celsius: 37
Fahrenheit: 98.6
```

---

### 9. Write a Python program to interchange the values of two numbers using a third variable.

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))

temp = a
a = b
b = temp

print("After swap: a =", a, " b =", b)
```

**Output (example):**
```text
Enter a: 5
Enter b: 9
After swap: a = 9  b = 5
```

---

### 10. Write a Python program to interchange the values of two numbers without using a third variable.

**Method 1: C-style (arithmetic trick)**

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a = a + b
b = a - b
a = a - b

print("After swap: a =", a, " b =", b)
```

**Output (example):**
```text
Enter a: 5
Enter b: 9
After swap: a = 9  b = 5
```

> এটি C-তে ব্যবহৃত classic arithmetic trick - `a`-তে দুইজনের যোগফল রেখে, তারপর বিয়োগ করে করে আসল মান আলাদা করে ফেলা হয়েছে। ধাপে ধাপে: `a = 5+9=14` → `b = 14-9=5` → `a = 14-5=9`।

**Method 2: Pythonic (tuple unpacking)**

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print("After swap: a =", a, " b =", b)
```

**Output (example):**
```text
Enter a: 5
Enter b: 9
After swap: a = 9  b = 5
```

> Python-এ extra variable ছাড়া swap আরও সহজে করা যায় tuple unpacking দিয়ে - কোনো arithmetic লাগে না, এবং খুব বড় সংখ্যায় overflow-এর ঝুঁকিও নেই। C-তে এই সুবিধা নেই বলেই ওখানে arithmetic trick ব্যবহার করতে হয়।

---

### 11. Write a Python program to input two numbers and print their quotient and remainder.

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))

quotient = a // b
remainder = a % b

print("Quotient:", quotient)
print("Remainder:", remainder)
```

**Output (example):**
```text
Enter a: 17
Enter b: 5
Quotient: 3
Remainder: 2
```

---

### ASCII Number কী?

**ASCII (American Standard Code for Information Interchange)** হলো একটি standard যেখানে প্রতিটি character (letter, digit, symbol)-কে একটি নির্দিষ্ট **সংখ্যা (0-127)** দিয়ে represent করা হয় - কারণ কম্পিউটার আসলে শুধু সংখ্যা বোঝে, অক্ষর নয়। যেমন `'A'` মানে সংখ্যা `65`, `'a'` মানে `97`, `'0'` মানে `48`।

| Range | কী |
|---|---|
| 48-57 | সংখ্যা `'0'` - `'9'` |
| 65-90 | Capital letter `'A'` - `'Z'` |
| 97-122 | Small letter `'a'` - `'z'` |

লক্ষ্য করুন: প্রতিটি capital letter-এর ASCII value তার সংশ্লিষ্ট small letter থেকে ঠিক **৩২ কম** (`'A'`=65, `'a'`=97, পার্থক্য 32) - এই প্যাটার্নটাই Q16, Q17-এ ব্যবহার করা হয়েছে।

Python-এ দুইটি built-in function দিয়ে এই রূপান্তর করা যায়:
* **`ord(character)`** - character থেকে তার ASCII (Unicode code point) সংখ্যা বের করে।
* **`chr(number)`** - সংখ্যা থেকে তার character ফেরত দেয় (ঠিক `ord()`-এর উল্টো)।

---

### 12. Write a Python program to accept any character from the user and display its ASCII number on screen.

```python
ch = input("Enter a character: ")
print("ASCII value:", ord(ch))
```

**Output (example):**
```text
Enter a character: A
ASCII value: 65
```

---

### 13. Write a Python program to input any ASCII number and display the appropriate character on screen.

```python
code = int(input("Enter an ASCII number: "))
print("Character:", chr(code))
```

**Output (example):**
```text
Enter an ASCII number: 65
Character: A
```

---

### 14. Write a Python program to input any capital letter and display it in small letter.

```python
ch = input("Enter a capital letter: ")
print("Small letter:", ch.lower())
```

**Output (example):**
```text
Enter a capital letter: A
Small letter: a
```

---

### 15. Write a Python program to input any small letter and display it in capital letter.

```python
ch = input("Enter a small letter: ")
print("Capital letter:", ch.upper())
```

**Output (example):**
```text
Enter a small letter: a
Capital letter: A
```

---

### 16. Write a Python program to input any capital letter and display it in small letter. (Without using the `lower()` method)

```python
ch = input("Enter a capital letter: ")
small_ch = chr(ord(ch) + 32)
print("Small letter:", small_ch)
```

**Output (example):**
```text
Enter a capital letter: A
Small letter: a
```

> ASCII-তে capital ও small letter-এর মধ্যে সবসময় ৩২-এর পার্থক্য থাকে, তাই `ord()` দিয়ে সংখ্যায় নিয়ে `+ 32` করে `chr()` দিয়ে আবার character-এ ফেরত আনা হলো।

---

### 17. Write a Python program to input any small letter and display it in capital letter. (Without using the `upper()` method)

```python
ch = input("Enter a small letter: ")
capital_ch = chr(ord(ch) - 32)
print("Capital letter:", capital_ch)
```

**Output (example):**
```text
Enter a small letter: a
Capital letter: A
```

---

### 18. Write a Python program to input the number of days from the user and convert it into years, months and days.

```python
total_days = int(input("Enter number of days: "))

years = total_days // 365
remaining_after_years = total_days % 365
months = remaining_after_years // 30
days = remaining_after_years % 30

print("Years:", years)
print("Months:", months)
print("Days:", days)
```

**Output (example):**
```text
Enter number of days: 400
Years: 1
Months: 1
Days: 5
```

---

### 19. Write a Python program to input a three-digit number from the user and calculate the sum of the first and last digits. (Hint: Input: 358, Output: 11)

```python
number = int(input("Enter a three-digit number: "))

first_digit = number // 100
last_digit = number % 10

print("Sum of first and last digit:", first_digit + last_digit)
```

**Output (example):**
```text
Enter a three-digit number: 358
Sum of first and last digit: 11
```

---

### 20. Write a Python program to input a three-digit number from the user and display the square of the first and last digits. (Hint: Input: 358, Output: Square of 3 is 9 and Square of 8 is 64)

```python
number = int(input("Enter a three-digit number: "))

first_digit = number // 100
last_digit = number % 10

print(f"Square of {first_digit} is {first_digit ** 2} and Square of {last_digit} is {last_digit ** 2}")
```

**Output (example):**
```text
Enter a three-digit number: 358
Square of 3 is 9 and Square of 8 is 64
```

---

### 21. Write a Python program to input a two-digit number from the user and display it with digits reversed. (Hint: Input: 32, Output: 23)

```python
number = int(input("Enter a two-digit number: "))

last_digit = number % 10
first_digit = number // 10
reversed_number = last_digit * 10 + first_digit

print("Reversed number:", reversed_number)
```

**Output (example):**
```text
Enter a two-digit number: 32
Reversed number: 23
```

---

### 22. Write a Python program to find the quotient and remainder of two numbers. (Without using the modulus `%` operator)

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))

quotient = a // b
remainder = a - (quotient * b)

print("Quotient:", quotient)
print("Remainder:", remainder)
```

**Output (example):**
```text
Enter a: 17
Enter b: 5
Quotient: 3
Remainder: 2
```

---

## Concepts Used (recap)

* `print()`, `input()` - output ও input নেওয়া
* `int()`, `float()` - type conversion/cast
* Arithmetic operators - `+ - * / // % **`
* `ord()` / `chr()` - character ↔ ASCII number রূপান্তর
* `.upper()` / `.lower()` - string case রূপান্তর (built-in method হিসেবে; ম্যানুয়ালি ASCII arithmetic দিয়েও দেখানো হয়েছে)
* Tuple unpacking (`a, b = b, a`) - extra variable ছাড়া swap

কোনো `if`/`for`/`while`/`def` লাগেনি - প্রতিটি সমস্যা একটি সরল **input → process → output** script দিয়েই সমাধান করা গেছে।
