# ============================================================
#  Live Class 05  |  Example 08
#  Debugging - seeing what your code is actually thinking
# ============================================================
#  When your code goes wrong, there is no need to get upset and
#  close the window. There is a simple trick - drop a print()
#  wherever you are suspicious, and ask it:
#  "what is inside this right now?"
#
#  Put type() next to it as well. Because 10 and "10" look exactly
#  the same on the screen, but to Python one is a number and the
#  other is text. That mix-up is the most common mistake of all.
#
#  When you are done, delete the DEBUG lines.
#  They are for you, not for the person using your program.
# ============================================================

number = input("Type a number: ")

print("DEBUG 1:", number, type(number))       # what came from input()

number = int(number)                          # turn the text into a number

print("DEBUG 2:", number, type(number))       # what it became

if number == 10:
    print("Yes, it is 10!")
else:
    print("No, it is not 10.")

# ============================================================
#  Sample Run 1  (type 10):
#
#  Type a number: 10
#  DEBUG 1: 10 <class 'str'>
#  DEBUG 2: 10 <class 'int'>
#  Yes, it is 10!
#
#  Sample Run 2  (type 7):
#
#  Type a number: 7
#  DEBUG 1: 7 <class 'str'>
#  DEBUG 2: 7 <class 'int'>
#  No, it is not 10.
# ============================================================
#  Both DEBUG lines show the same number - 10 and 10.
#  But the words beside them are different:
#
#     <class 'str'>  means  text
#     <class 'int'>  means  number
#
#  Those words beside it are the real news. That is what type() shows.
# ============================================================
