"""
Example 3: variables and the four everyday data types
Live Class 02 - print(), input(), Variables, Data Types (Batch 12)

WHAT A VARIABLE IS
    A name you give to a value, so you can use it later without typing the
    value again. Written as:   name = value
    The = sign is NOT "equals" from maths. Read it as "gets" or "points to".
        age = 25     ->  "the name age now points to the value 25"

THE FOUR TYPES YOU WILL USE EVERY DAY
    int   -> whole number            25, 0, -7
    float -> number with a decimal   99.5, 3.14, 0.0
    str   -> text, inside quotes     "Rahim", "25", ""
    bool  -> True or False           True, False   (capital T, capital F)

NAMING RULES - what Python allows
    allowed     : letters, digits, underscore ; must NOT start with a digit
    not allowed : spaces, dashes, and Python's own words (print, input, ...)
    convention  : snake_case  ->  monthly_salary, not MonthlySalary or x

HOW TO RUN
    Terminal :  python example_03_variables_and_types.py
"""

# ----- 1) One variable of each type -----
name = "Rahim Uddin"        # str   - quotes make it text
age = 25                    # int   - whole number, no quotes
height = 5.6                # float - has a decimal point
is_student = True           # bool  - True or False, capital letter

# ----- 2) Using them -----
print("Name       :", name)
print("Age        :", age)
print("Height     :", height)
print("Is student :", is_student)

# ----- 3) type() tells you what kind of value a name is pointing to -----
print("type(name)       =", type(name))
print("type(age)        =", type(age))
print("type(height)     =", type(height))
print("type(is_student) =", type(is_student))

# ----- 4) A variable can be given a new value later -----
# The old value is simply forgotten; the name now points somewhere else.
age = 26
print("age after the birthday :", age)

# ----- 5) A variable can even change type -----
# Allowed in Python, but do it by accident and you get confusing bugs.
age = "twenty six"
print("age is now :", age, type(age))

# ----- 6) Good names vs bad names -----
# Bad  : x = 50000        <- what is x? nobody knows, not even you next week.
# Good : monthly_salary = 50000
monthly_salary = 50000
yearly_salary = monthly_salary * 12
print("Yearly salary :", yearly_salary)

# Expected Output:
# Name       : Rahim Uddin
# Age        : 25
# Height     : 5.6
# Is student : True
# type(name)       = <class 'str'>
# type(age)        = <class 'int'>
# type(height)     = <class 'float'>
# type(is_student) = <class 'bool'>
# age after the birthday : 26
# age is now : twenty six <class 'str'>
# Yearly salary : 600000
