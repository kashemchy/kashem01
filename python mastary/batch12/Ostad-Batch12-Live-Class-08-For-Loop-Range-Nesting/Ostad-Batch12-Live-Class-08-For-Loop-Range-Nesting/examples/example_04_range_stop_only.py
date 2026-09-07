"""
Example 04: range(stop)
Live Class 08 - For Loop, range(), Loop Nesting

range(stop) -> 0, 1, ..., stop-1
stop is always EXCLUSIVE - the classic off-by-one trap.
"""

for i in range(5):
    print(i, end=" ")
print()

# Expected Output:
# 0 1 2 3 4
