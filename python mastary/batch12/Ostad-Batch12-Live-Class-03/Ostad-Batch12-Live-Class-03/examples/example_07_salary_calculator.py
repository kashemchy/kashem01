monthly_salary = float(input("Enter monthly salary: "))

yearly_salary = monthly_salary * 12
bonus = yearly_salary * 0.10
total = yearly_salary + bonus

print("\n----- Salary Information -----")
print(f"Monthly Salary : {monthly_salary:,.2f}")
print(f"Yearly Salary  : {yearly_salary:,.2f}")
print(f"Bonus          : {bonus:,.2f}")
print(f"Total          : {total:,.2f}")
