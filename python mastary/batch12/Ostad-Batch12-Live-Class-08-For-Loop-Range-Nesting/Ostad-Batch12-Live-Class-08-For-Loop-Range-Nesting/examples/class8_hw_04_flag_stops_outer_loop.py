found = False

for row in range(1, 4):
    print(f"Row {row}:")
    for col in range(1, 6):
        if col == 3:
            found = True
            break
        print(f"  col {col}")
    if found:
        break

print("Outer loop stopped too - the flag variable ended both loops.")
