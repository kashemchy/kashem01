# ============================================================
#  Live Class 05  |  Example 05
#  Truthy and Falsy - empty means "no"
# ============================================================
#  Story:
#  Pick up your tiffin box and shake it. If you hear nothing,
#  you know it is empty. Python thinks the very same way.
#
#  Something empty means "no"        ->  Falsy
#  Something with stuff in it means "yes"  ->  Truthy
#
#  There is a small tool called bool() that takes anything and
#  tells you whether Python reads it as True or False.
#  Let's look.
# ============================================================

print("--- FALSY: Python reads these as False ---")
print("bool(0)      =", bool(0))
print("bool(0.0)    =", bool(0.0))
print('bool("")     =', bool(""))
print("bool(None)   =", bool(None))

print("--- TRUTHY: Python reads these as True ---")
print("bool(7)      =", bool(7))
print("bool(-3)     =", bool(-3))
print('bool("hi")   =', bool("hi"))
print('bool("0")    =', bool("0"))

# ============================================================
#  Expected Output:
#
#  --- FALSY: Python reads these as False ---
#  bool(0)      = False
#  bool(0.0)    = False
#  bool("")     = False
#  bool(None)   = False
#  --- TRUTHY: Python reads these as True ---
#  bool(7)      = True
#  bool(-3)     = True
#  bool("hi")   = True
#  bool("0")    = True
# ============================================================
#  Which line is the most interesting?  ->  The last one!
#  "0" has quotation marks around it, so it is not the number
#  zero - it is a piece of text, and that text is not empty.
#  So it is Truthy.
#
#  An easy way to remember it:
#  Empty number, empty text, and None - all false.
#  Everything else is true.
# ============================================================
