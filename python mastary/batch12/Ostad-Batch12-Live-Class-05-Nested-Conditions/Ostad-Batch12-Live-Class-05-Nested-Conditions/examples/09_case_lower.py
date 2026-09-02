# ============================================================
#  Live Class 05  |  Example 09
#  "Yes" and "yes" - two different things to Python
# ============================================================
#  This file will show you a hidden mistake.
#
#  You cannot decide how the user will type. Some will write yes,
#  some will write Yes, some will write YES.
#  To Python, a capital Y and a small y are not the same.
#
#  The fix: .lower() - it turns any text into small letters.
#  Run it once right before you compare, and the trouble is over.
#
#  Below are two tests of the same question - one without .lower()
#  and one with it. Type "Yes" and watch the difference.
# ============================================================

answer = input("Do you like ice cream? (Yes/No): ")

print("DEBUG: you typed ->", answer)

if answer == "yes":
    print("Test 1 (no .lower()): Yummy!")
else:
    print("Test 1 (no .lower()): Oh, okay.")

if answer.lower() == "yes":
    print("Test 2 (with .lower()): Yummy!")
else:
    print("Test 2 (with .lower()): Oh, okay.")

# ============================================================
#  Sample Run  (type "Yes" - with a capital Y):
#
#  Do you like ice cream? (Yes/No): Yes
#  DEBUG: you typed -> Yes
#  Test 1 (no .lower()): Oh, okay.
#  Test 2 (with .lower()): Yummy!
# ============================================================
#  Test 1 gave the wrong answer. And yet no red text appeared,
#  no error came up, the program ran perfectly happily.
#
#  This kind of mistake is called a silent bug.
#  Python will not point it out - you have to catch it by testing.
#  That is why every program must be run with a few different
#  inputs before you trust it.
# ============================================================
#  Try it yourself:
#  1) Type "YES" and run it. Which test stays correct?
#  2) Type "yes" and run it. Now both are correct - can you say why?
# ============================================================
