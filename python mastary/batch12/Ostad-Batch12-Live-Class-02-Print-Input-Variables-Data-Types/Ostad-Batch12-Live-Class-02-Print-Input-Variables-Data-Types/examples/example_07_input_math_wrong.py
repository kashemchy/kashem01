"""
Example 7: the four errors of Live Class 02 (deliberately wrong)
Live Class 02 - print(), input(), Variables, Data Types (Batch 12)

WHY THIS FILE EXISTS
    Every one of these four errors comes from the same single fact:
    input() hands back TEXT, and text does not behave like a number.
    Meet them here on purpose, so they are not a surprise at 1 a.m.

HOW TO READ THIS FILE
    A broken line cannot sit inside a working file, so each mistake is kept
    as a comment together with the REAL message Python printed when it was
    actually run, and the correct line right underneath it.

    Try it yourself: copy a WRONG line into a new file, run it, and see the
    same message with your own eyes.

HOW TO READ ANY ERROR MESSAGE - three things, always in this order
    1. the LAST line   -> the error type and what went wrong
    2. the line number -> where Python stopped
    3. the ^ marker    -> which character it was looking at
"""

# ----- 1) Doing maths on an answer that was never converted -----
# WRONG:
#   age = input("Your age: ")     # the user types 25
#   print(age + 10)
#
#   Traceback (most recent call last):
#     File "example.py", line 2, in <module>
#       print(age + 10)
#             ~~~~^~~~
#   TypeError: can only concatenate str (not "int") to str
#
# Read it as: "you asked me to join text with a number, and I cannot."
# The fix is int() around the input, not a different + sign.
age_text = "25"
age = int(age_text)
print("age + 10 =", age + 10)

# ----- 2) int() on text that has a word in it -----
# WRONG:  age = int("25 years")
#
#   Traceback (most recent call last):
#     File "example.py", line 1, in <module>
#       age = int("25 years")
#   ValueError: invalid literal for int() with base 10: '25 years'
#
# "invalid literal" means: the text is not a clean whole number.
# int() converts "25", never "25 years", "25/-" or "twenty five".
age = int("25")
print("age =", age)

# ----- 3) int() on text that holds a decimal -----
# WRONG:  price = int("99.5")
#
#   ValueError: invalid literal for int() with base 10: '99.5'
#
# int() refuses "99.5" because it is not a WHOLE number.
# Use float() for anything with a decimal point. To get a whole number
# out of it, convert twice: int(float("99.5")) -> 99
price = float("99.5")
print("price =", price)

# ----- 4) Using a name Python has never seen -----
# WRONG:
#   print(totl)
#
#   NameError: name 'totl' is not defined. Did you mean: 'total'?
#
# Python does not guess. A typo in a variable name is a new, empty name.
# Notice it even suggests the one you probably meant.
total = 1500
print("total =", total)

# ----- 5) One more that is not an error at all - and that is the danger -----
# marks = input("Marks: ")   # the user types 50
# print(marks * 3)           # prints 505050, not 150 - and Python never
#                            # complains, because repeating text IS legal.
marks = int("50")
print("marks * 3 =", marks * 3)

# Expected Output:
# age + 10 = 35
# age = 25
# price = 99.5
# total = 1500
# marks * 3 = 150
