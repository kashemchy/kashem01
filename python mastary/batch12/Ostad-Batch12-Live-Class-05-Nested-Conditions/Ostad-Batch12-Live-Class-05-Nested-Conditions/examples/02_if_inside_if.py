# ============================================================
#  Live Class 05  |  Example 02
#  An if inside an if - your first Nested Condition
# ============================================================
#  Story:
#  You are standing at the zoo gate. The gatekeeper asks first:
#  "Do you have a ticket?" If you don't, the conversation ends
#  right there - you are not going in.
#
#  Only if you DO have a ticket does he ask the second question:
#  "How old are you? Under 10 gets a free balloon!"
#
#  Notice that the second question depends on the answer to the
#  first one. That is a Nested Condition - an if inside an if.
# ============================================================

ticket = "yes"
age = 8

if ticket == "yes":                        # outer question
    print("Ticket OK. Come in!")

    if age < 10:                           # inner question
        print("You get a free balloon!")
    else:
        print("Enjoy the zoo!")

else:
    print("Please buy a ticket first.")

# ============================================================
#  Expected Output:
#
#  Ticket OK. Come in!
#  You get a free balloon!
# ============================================================
#  Try it yourself:
#  1) Set ticket = "no" and run it. Does the balloon line appear?
#     It does not - the answer to the outer question was "no",
#     so Python never even asked the inner question.
#  2) Set age = 15 and run it. Which line appears now?
# ============================================================
