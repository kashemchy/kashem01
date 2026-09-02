# ============================================================
#  Live Class 05  |  Example 04
#  Nested if - now we ask the user
# ============================================================
#  In the last two files we wrote the values ourselves.
#  This time we will get them from the user with input().
#
#  Two rules:
#  - Under 18, no voting. The conversation ends there.
#  - 18 or older, and only then, comes the second question:
#    do you have an NID?
#
#  Remember: whatever input() brings back is always text (a string).
#  So the age has to be turned into a number with int().
# ============================================================

age = int(input("Enter your age: "))

if age >= 18:
    nid = input("Do you have an NID? (yes/no): ")

    if nid == "yes":
        print("You can vote!")
    else:
        print("Get your NID first, then you can vote.")

else:
    print("You are not 18 yet. Wait a few more years!")

# ============================================================
#  Sample Run 1  (type 20 for age, then yes):
#
#  Enter your age: 20
#  Do you have an NID? (yes/no): yes
#  You can vote!
#
#  Sample Run 2  (type 20 for age, then no):
#
#  Enter your age: 20
#  Do you have an NID? (yes/no): no
#  Get your NID first, then you can vote.
#
#  Sample Run 3  (type 15 for age):
#
#  Enter your age: 15
#  You are not 18 yet. Wait a few more years!
# ============================================================
#  Try it yourself:
#  1) In Run 3 the NID question never appeared. Can you say why?
#  2) Type "Yes" with a capital Y for the NID answer and run it.
#     Is the answer still correct? The fix is in file 09.
# ============================================================
