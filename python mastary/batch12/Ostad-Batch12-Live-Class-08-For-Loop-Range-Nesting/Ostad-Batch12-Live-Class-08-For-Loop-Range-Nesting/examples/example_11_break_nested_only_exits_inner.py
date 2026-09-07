"""
Example 11: break only exits the NEAREST loop
Live Class 08 - For Loop, range(), Loop Nesting

A common mistake is assuming break stops every loop it is inside. It only
stops the innermost (nearest) loop - the outer loop keeps running.
"""

for row in range(1, 4):
    print(f"Row {row}:")
    for col in range(1, 6):
        if col == 3:
            break
        print(f"  col {col}")

print("Outer loop finished all 3 rows - break only stopped the inner loop each time.")

# Expected Output:
# Row 1:
#   col 1
#   col 2
# Row 2:
#   col 1
#   col 2
# Row 3:
#   col 1
#   col 2
# Outer loop finished all 3 rows - break only stopped the inner loop each time.
