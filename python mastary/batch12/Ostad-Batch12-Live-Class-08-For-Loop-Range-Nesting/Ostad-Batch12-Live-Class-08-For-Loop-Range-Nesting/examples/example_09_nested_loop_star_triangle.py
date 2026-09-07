"""
Example 09: Nested loop - star triangle pattern
Live Class 08 - For Loop, range(), Loop Nesting

The outer loop picks the row number; the row number itself decides how
much work happens inside that row (here, how many stars to print).
"""

for row in range(1, 6):
    print("*" * row)

# Expected Output:
# *
# **
# ***
# ****
# *****
