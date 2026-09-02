"""
Example 1: print() from zero - showing things on the screen
Live Class 02 - print(), input(), Variables, Data Types (Batch 12)

WHAT THIS FILE IS
    Last class print() was used to show one line of text. That is about 20%
    of what print() can do. This file covers the rest of the everyday 80%.

THE THREE THINGS TO NOTICE
    1. a comma between two values -> Python puts ONE SPACE between them
    2. sep="..."  -> changes that space to whatever you want
    3. end="..."  -> changes what happens AFTER the line (default: go to
                     the next line)

WHY IT MATTERS
    Almost every program you write for the next six months ends with a
    print(). If the output looks wrong, it is usually not your logic that is
    broken - it is one of these three things.

HOW TO RUN
    Terminal :  python example_01_print_basics.py
    VS Code  :  Run button (top right)  /  Ctrl + F5
    PyCharm  :  green Run arrow next to the file
"""

# ----- 1) One value at a time -----
print("Assalamu Alaikum")
print("Welcome to Live Class 02")

# ----- 2) Many values in one print() - comma adds a space for you -----
print("My name is", "Rahim")
print("I am", 25, "years old")

# ----- 3) Text and numbers behave differently -----
# Notice: "25" with quotes is text, 25 without quotes is a number.
print("25")
print(25)

# ----- 4) sep= decides what goes BETWEEN the values -----
print("2026", "08", "20", sep="-")
print("rahim", "gmail.com", sep="@")
print("a", "b", "c", sep=" -> ")

# ----- 5) end= decides what comes AFTER the line -----
# Default is a newline. Making it "" keeps the next print on the same line.
print("Loading", end="")
print(".", end="")
print(".", end="")
print(".")

# ----- 6) An empty print() leaves a blank line -----
print()
print("This line came after a blank line.")

# ----- 7) A number can be calculated right inside print() -----
print("Total marks:", 40 + 35 + 25)

# Expected Output:
# Assalamu Alaikum
# Welcome to Live Class 02
# My name is Rahim
# I am 25 years old
# 25
# 25
# 2026-08-20
# rahim@gmail.com
# a -> b -> c
# Loading...
#
# This line came after a blank line.
# Total marks: 100
