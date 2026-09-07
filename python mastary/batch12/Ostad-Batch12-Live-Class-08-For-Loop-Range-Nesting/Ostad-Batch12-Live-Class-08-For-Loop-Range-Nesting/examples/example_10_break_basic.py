"""
Example 10: break - stop the loop immediately
Live Class 08 - For Loop, range(), Loop Nesting

break exits the nearest enclosing loop right away, skipping any
remaining items - useful once you've found what you were looking for.
"""

numbers = [4, 9, 15, 22, 30, 7]
target = 22

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
    print(f"Checking {num}...")

# Expected Output:
# Checking 4...
# Checking 9...
# Checking 15...
# Found 22!
