"""
Example 4: type conversion - turning text into a number and back
Live Class 02 - print(), input(), Variables, Data Types (Batch 12)

THE PROBLEM THIS SOLVES
    input() always hands back text. Text cannot be added, multiplied or
    compared like a number. So before doing maths on an answer, you convert
    it yourself. That is all "type conversion" means.

THE THREE CONVERTERS YOU NEED TODAY
    int("25")     -> 25       text  to whole number
    float("99.5") -> 99.5     text  to decimal number
    str(100)      -> "100"    number to text

WHEN A CONVERSION FAILS
    int() is strict. It converts text that contains ONLY a whole number.
        int("25")       -> works
        int(" 25 ")     -> works, spaces around it are ignored
        int("25 years") -> ValueError, there is a word inside
        int("9.5")      -> ValueError, that is a float, not an int
    Those failures are shown for real in example_07.

HOW TO RUN
    Terminal :  python example_04_type_conversion.py
"""

# ----- 1) The core problem, without any input() in the way -----
age_text = "25"                     # pretend this came from input()
print("age_text        =", age_text, type(age_text))
print("age_text + age_text =", age_text + age_text)      # joining, not adding

# ----- 2) The fix: convert once, then use the number -----
age = int(age_text)
print("age             =", age, type(age))
print("age + age       =", age + age)                    # real addition

# ----- 3) text to float, for anything with a decimal point -----
price_text = "99.5"
price = float(price_text)
print("price           =", price, type(price))
print("price for 3     =", price * 3)

# ----- 4) number to text, with str() -----
roll = 101
roll_text = str(roll)
print("roll_text       =", roll_text, type(roll_text))
print("Roll joined     :", "Roll-" + roll_text)          # only text joins text

# ----- 5) int() on a float THROWS AWAY the decimal part -----
# It does not round. 9.99 becomes 9, not 10.
print("int(9.99)       =", int(9.99))
print("float(9)        =", float(9))

# ----- 6) The usual shortcut: convert straight around the input -----
# Same as example 02, just written in one line instead of two.
# (Commented out so this file runs without stopping to ask.)
# marks = int(input("Enter your marks: "))

# ----- 7) True and False are numbers underneath -----
print("int(True)       =", int(True), " int(False) =", int(False))

# Expected Output:
# age_text        = 25 <class 'str'>
# age_text + age_text = 2525
# age             = 25 <class 'int'>
# age + age       = 50
# price           = 99.5 <class 'float'>
# price for 3     = 298.5
# roll_text       = 101 <class 'str'>
# Roll joined     : Roll-101
# int(9.99)       = 9
# float(9)        = 9.0
# int(True)       = 1  int(False) = 0
