# ============================================================
#  Live Class 05  |  Example 06
#  if name: - a condition with no comparison at all!
# ============================================================
#  We used to write:      if name != "":
#  Now we can just write:  if name:
#
#  Both mean the same thing - "is name not empty?"
#  But the second one is easier to read and shorter to type.
#
#  It works because of what you learned in the last file:
#  empty text "" is Falsy, and text with something in it is Truthy.
# ============================================================

name = input("What is your name? ")

if name:
    print("Hello,", name)
else:
    print("You did not write anything!")

# ============================================================
#  Sample Run 1  (type a name):
#
#  What is your name? Rafi
#  Hello, Rafi
#
#  Sample Run 2  (type nothing, just press Enter):
#
#  What is your name?
#  You did not write anything!
# ============================================================
#  Try it yourself:
#  1) In Run 2, what was actually inside name?  ->  ""  (empty text)
#  2) Press the space bar once, then Enter. What happens now?
#     Here is the fun part - a space is a character too!
#     So the text is not empty, and you get a greeting.
# ============================================================
