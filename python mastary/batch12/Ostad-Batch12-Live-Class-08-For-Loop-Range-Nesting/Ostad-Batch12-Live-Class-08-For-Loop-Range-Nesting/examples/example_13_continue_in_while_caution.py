"""
Example 13: continue inside a while loop - the update-step trap
Live Class 08 - For Loop, range(), Loop Nesting

In a while loop, continue jumps straight back to the condition check -
skipping any code written AFTER it. If the Update step (Live Class 07's
4th part of a while loop) sits after continue, it never runs and the
loop hangs forever. Always update BEFORE the continue check.
"""

# ----- WRONG order (DO NOT RUN) -----
# count = 0
# while count < 10:
#     if count % 2 == 0:
#         continue          # <-- jumps back to "while count < 10" BEFORE count += 1 runs
#     print(count, end=" ")
#     count += 1            # never reached when count is even -> infinite loop

# ----- CORRECT order: update happens before the continue check -----
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count, end=" ")
print()

# Expected Output:
# 1 3 5 7 9
