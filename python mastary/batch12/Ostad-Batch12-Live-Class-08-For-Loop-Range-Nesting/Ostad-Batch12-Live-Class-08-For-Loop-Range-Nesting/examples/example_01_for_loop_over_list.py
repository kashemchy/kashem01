"""
Example 01: for-each over a list
Live Class 08 - For Loop, range(), Loop Nesting

Python's for loop is a "for-each" loop, NOT a C/Java-style counter loop.
It walks through every item of an iterable (here, a list) one by one.
"""

fruits = ["mango", "jackfruit", "litchi"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Expected Output:
# Fruit: mango
# Fruit: jackfruit
# Fruit: litchi
