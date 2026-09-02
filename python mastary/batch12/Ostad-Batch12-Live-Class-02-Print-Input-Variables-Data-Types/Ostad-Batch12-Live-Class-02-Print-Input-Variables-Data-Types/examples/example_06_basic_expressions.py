"""
Example 6: writing basic expressions
Live Class 02 - print(), input(), Variables, Data Types (Batch 12)

WHAT AN EXPRESSION IS
    Anything Python can work out into a single value.
        500 * 3            -> 1500
        price * quantity   -> 1500
        total > 1000       -> True
    A statement DOES something; an expression HAS a value.

THE SEVEN ARITHMETIC OPERATORS
    +   add                 7 + 2  = 9
    -   subtract            7 - 2  = 5
    *   multiply            7 * 2  = 14
    /   divide              7 / 2  = 3.5    <- ALWAYS gives a float
    //  floor divide        7 // 2 = 3      <- throws away the fraction
    %   remainder (mod)     7 % 2  = 1      <- what is left over
    **  power               7 ** 2 = 49

THE ORDER PYTHON USES
    ** first, then * / // %, then + - , left to right.
    Brackets beat all of them - and brackets are free. Use them.

COMPARISON GIVES A bool
    >   <   >=   <=   ==   !=      each one works out to True or False.
    == compares, = assigns. Mixing them up is the classic day-two bug.

HOW TO RUN
    Terminal :  python example_06_basic_expressions.py
"""

# ----- 1) An expression built from variables -----
price = 500
quantity = 3
total = price * quantity
print("total =", total)

# ----- 2) All seven arithmetic operators on the same two numbers -----
a = 7
b = 2
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // b =", a // b)
print("a % b  =", a % b)
print("a ** b =", a ** b)

# ----- 3) / always returns a float, even when it divides evenly -----
print("10 / 2 =", 10 / 2, type(10 / 2))
print("10 // 2 =", 10 // 2, type(10 // 2))

# ----- 4) Brackets change the answer -----
print("2 + 3 * 4   =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)

# ----- 5) Comparison expressions give True or False -----
is_expensive = total > 1000
print("is_expensive =", is_expensive, type(is_expensive))
print("total == 1500 :", total == 1500)
print("total != 1500 :", total != 1500)

# ----- 6) f-string: putting values inside a sentence -----
# Write f before the quotes, then put any expression inside { }.
product = "Laptop"
print(f"{product} x {quantity} = {total} taka")

# ----- 7) Two f-string tricks worth knowing today -----
# :.2f -> exactly 2 digits after the decimal point
# :,   -> comma separator for big numbers
vat = total * 0.15
print(f"VAT       : {vat:.2f}")
print(f"Big number: {1234567:,}")

# Expected Output:
# total = 1500
# a + b  = 9
# a - b  = 5
# a * b  = 14
# a / b  = 3.5
# a // b = 3
# a % b  = 1
# a ** b = 49
# 10 / 2 = 5.0 <class 'float'>
# 10 // 2 = 5 <class 'int'>
# 2 + 3 * 4   = 14
# (2 + 3) * 4 = 20
# is_expensive = True <class 'bool'>
# total == 1500 : True
# total != 1500 : False
# Laptop x 3 = 1500 taka
# VAT       : 225.00
# Big number: 1,234,567
