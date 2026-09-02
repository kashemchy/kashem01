# ============================================================
#  Live Class 05  |  Example 03
#  How many spaces - that decides everything
# ============================================================
#  The same four lines. Only the spacing has moved.
#  And that alone makes the program give two different answers!
#
#  In Version 1 the second if is INSIDE the first one (indented).
#  In Version 2 the second if is OUTSIDE (not indented).
#
#  The age below is 10, so the first condition (age >= 18) is false.
#  In Version 1 nothing inside it will run at all.
#  In Version 2 the second if stands on its own, so it still runs.
# ============================================================

age = 10
money = 500

print("--- Version 1: the second if is INSIDE the first one ---")

if age >= 18:
    print("You are an adult.")
    if money >= 100:
        print("You can buy the ticket.")

print("--- Version 2: the second if is OUTSIDE ---")

if age >= 18:
    print("You are an adult.")
if money >= 100:
    print("You can buy the ticket.")

# ============================================================
#  Expected Output:
#
#  --- Version 1: the second if is INSIDE the first one ---
#  --- Version 2: the second if is OUTSIDE ---
#  You can buy the ticket.
# ============================================================
#  Try it yourself:
#  1) Set age = 20 and run it. Do both versions give the same
#     answer now?
#  2) There is only one lesson here, and it is this:
#     in Python, spaces are not just for looking neat.
#     Spaces are what tell Python which line belongs inside what.
# ============================================================
