# ============================================================
#  Live Class 05  |  Example 07
#  Both ideas together - a tiny Login
# ============================================================
#  This file uses both of today's ideas at the same time:
#
#  The outer if  ->  Truthy/Falsy   (did they type a name at all?)
#  The inner if  ->  a normal check (did the password match?)
#
#  Notice the order: if there is no name, there is no point asking
#  for a password. That is why the password line sits INSIDE the
#  outer if.
# ============================================================

username = input("Username: ")

if username:
    password = input("Password: ")

    if password == "1234":
        print("Login successful! Welcome,", username)
    else:
        print("Wrong password!")

else:
    print("Username cannot be empty.")

# ============================================================
#  Sample Run 1  (name rafi, password 1234):
#
#  Username: rafi
#  Password: 1234
#  Login successful! Welcome, rafi
#
#  Sample Run 2  (name rafi, password abcd):
#
#  Username: rafi
#  Password: abcd
#  Wrong password!
#
#  Sample Run 3  (type nothing, just press Enter):
#
#  Username:
#  Username cannot be empty.
# ============================================================
#  Try it yourself:
#  1) In Run 3 the password was never asked for. Why?
#  2) Replace "1234" with a password of your own.
#  3) Harder question: if you wanted to tell the user how many
#     tries they have left, what would you need?
#     (The answer is in Module 3 - a loop!)
# ============================================================
