"""
Example 12: continue - skip just this one iteration
Live Class 08 - For Loop, range(), Loop Nesting

continue skips the rest of the CURRENT iteration's body and jumps to the
next iteration. Unlike break, the loop keeps running.
"""

numbers = list(range(1, 11))

for num in numbers:
    if num % 2 == 0:
        continue
    print(num, end=" ")
print()

# Expected Output:
# 1 3 5 7 9
