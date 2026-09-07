"""
Example 03: enumerate() - index + value together
Live Class 08 - For Loop, range(), Loop Nesting

When you need a serial number alongside each item, don't build a manual
counter (i = 0; i += 1). Use enumerate() - default index starts at 0,
start=1 shifts it to 1.
"""

fruits = ["mango", "jackfruit", "litchi"]
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Expected Output:
# 1. mango
# 2. jackfruit
# 3. litchi
