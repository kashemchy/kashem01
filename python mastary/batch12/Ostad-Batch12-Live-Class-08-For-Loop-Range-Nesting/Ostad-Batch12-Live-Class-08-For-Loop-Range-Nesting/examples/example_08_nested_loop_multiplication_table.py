"""
Example 08: Nested loop - multiplication table
Live Class 08 - For Loop, range(), Loop Nesting

A nested loop is a loop inside another loop's body. For every ONE iteration
of the outer loop, the inner loop runs COMPLETELY. Total iterations =
outer count x inner count.
"""

for row in range(1, 6):              # outer: chooses the row
    for col in range(1, 6):          # inner: fills the columns of that row
        product = row * col
        print(f"{product:4}", end="")
    print()                          # end the row -> move to the next line

# Expected Output:
#    1   2   3   4   5
#    2   4   6   8  10
#    3   6   9  12  15
#    4   8  12  16  20
#    5  10  15  20  25
