"""
Example 5: id() - where a variable actually lives
Live Class 02 - print(), input(), Variables, Data Types (Batch 12)

THE WRONG PICTURE (what most beginners imagine)
    A variable is a box. age = 25 puts 25 inside a box labelled age.

THE RIGHT PICTURE
    The value sits somewhere in memory. The variable is only a NAME TAG
    tied to it with a string. age = 25 ties the tag "age" to the value 25.
    Change the value and the tag simply gets moved to a different value -
    the old value is not edited.

WHAT id() IS
    id(x) returns the address-like number of the value x is tied to. You
    will never use id() in a real program. It is used here because it is
    the only way to SEE that the picture above is true.

    Every run gives different numbers. Do not compare your numbers with
    the ones in the Expected Output - compare them with each other, within
    a single run.

HOW TO RUN
    Terminal :  python example_05_id_and_memory.py
"""

# ----- 1) A name tied to a value -----
city = "Dhaka"
print("city =", city, " id =", id(city))

# ----- 2) Reassignment moves the TAG, it does not edit the value -----
# "Dhaka" itself is untouched. The tag city now points at "Chattogram".
city = "Chattogram"
print("city =", city, " id =", id(city), " <- a different id")

# ----- 3) Two names can point to the SAME value -----
x = 1000
y = x
print("x id =", id(x))
print("y id =", id(y), " <- the same number as x")
print("is x the same object as y?", x is y)

# ----- 4) Changing one of them does not touch the other -----
x = 2000
print("after x = 2000 ->  x =", x, " y =", y)

# ----- 5) Numbers are immutable: maths builds a NEW value -----
counter = 5
print("counter =", counter, " id =", id(counter))
counter = counter + 1
print("counter =", counter, " id =", id(counter), " <- new value, new id")

# ----- 6) Two variables in one line, and the swap trick -----
a, b = 10, 20
print("a =", a, " b =", b)
a, b = b, a
print("after swap -> a =", a, " b =", b)

# Expected Output (the id numbers WILL be different on your machine):
# city = Dhaka  id = 2158921477616
# city = Chattogram  id = 2158921478576  <- a different id
# x id = 2158921355984
# y id = 2158921355984  <- the same number as x
# is x the same object as y? True
# after x = 2000 ->  x = 2000  y = 1000
# counter = 5  id = 140708744663752
# counter = 6  id = 140708744663784  <- new value, new id
# a = 10  b = 20
# after swap -> a = 20  b = 10
