"""
Example 2: input() - letting the computer ask a question
Live Class 02 - print(), input(), Variables, Data Types (Batch 12)

WHAT THIS FILE IS
    Until now the program only talked. Now it listens.

WHAT input() ACTUALLY DOES - three steps, always in this order
    1. shows the text you put inside the brackets (the "prompt")
    2. STOPS and waits until the user types something and presses Enter
    3. hands back whatever was typed, so you can keep it in a variable

THE ONE SENTENCE TO MEMORISE TODAY
    input() ALWAYS gives back text (str) - even when the user types 25.
    Python does not look at what was typed and decide it is a number.
    It is text until YOU convert it. That conversion is example 04.

WHY THE PROMPT MATTERS
    input() with no prompt shows an empty blinking cursor and the user has
    no idea what to type. Always put the question inside the brackets.

HOW TO RUN
    Terminal :  python example_02_input_basics.py
    Then type an answer and press Enter each time it stops.
"""

# ----- 1) Ask, and keep the answer in a variable -----
name = input("What is your name? ")

# ----- 2) Use the answer -----
print("Hello,", name)
print("Nice to meet you,", name)

# ----- 3) Ask for something that LOOKS like a number -----
age_text = input("How old are you? ")
print("You typed:", age_text)

# ----- 4) Proof that it is text, not a number -----
# type() reports what kind of value something is. Watch it say str.
print("The type of what you typed is:", type(age_text))

# ----- 5) The surprise this causes -----
# For text, + means "join", not "add". So "25" + "25" becomes "2525".
print("age_text + age_text =", age_text + age_text)

# Expected Output (when the user types Rahim, then 25):
# What is your name? Rahim
# Hello, Rahim
# Nice to meet you, Rahim
# How old are you? 25
# You typed: 25
# The type of what you typed is: <class 'str'>
# age_text + age_text = 2525
