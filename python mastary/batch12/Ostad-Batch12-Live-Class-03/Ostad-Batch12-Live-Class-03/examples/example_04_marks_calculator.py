bangla = float(input("Bangla marks: "))
english = float(input("English marks: "))
math = float(input("Math marks: "))

total = bangla + english + math
average = total / 3

print("\n----- Result -----")
print(f"Total   : {total}")
print(f"Average : {average:.2f}")
