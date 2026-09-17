# # user define function  - programmer nijer motho banabe
# # built in funciton-- already banano.. ace


# # print("Hello")
# # input("Enter Your name")



# # no input no return
# def my_first():
#     a = 10
#     b = 12
#     print(a+b)


# my_first()  # function call kora ba switch kora


# #2 input thakbe kinthu return thakbena

# def add_two(a,b):
#     print(a+b)

# add_two(5,8)


# # input return thakbe

# def multiply_two(a,b):
#     return a*b
# result = multiply_two(12,2)
# print(result)

# def hello():
#     return "Hello"

# greetings = hello()
# print(greetings)

# def addition(a,b):
#     result = a+b
#     return result

# r = addition(26, 45)
# print(r)


# def adds (*args):
#     print(args)
#     return sum(args)
# p = adds(12,45,36,35,46,2,5,4,6)
# print(p)

# # key workd argumet

# def my_func(f_name,l_name,age):
#     print(f"My name is {f_name} {l_name}. I am {age} years old")

# my_func(age = 25,f_name = "kashem", l_name = "Chowdhury")


# def my_details(**kwargs):
#     print(kwargs)
#     print(f"My name is {kwargs['f_name']} {kwargs['l_name']}, I am {kwargs['age']} years old. i read in class {kwargs['read']}. Do you like to play {kwargs['game']}")
# print("All information has been updated")

# my_details(f_name = input("Your first name Here: "), l_name = input("Your last name here: "), age = int(input("Enter age here: ")), game = input("Favourite game Here: "), read = input("your class name: "))


# lambda fucntion : it is a anonymous function

# def square(x):
#     return x*x
# print(square(5))

squares = lambda x : x*x

print(squares(3))

add = lambda a,b : a + b
print(add(3,6))

students = [('kashem',60),('Rubel', 55),('Lambu', 80),('akram',99)]

sorted_students = sorted(students, key = lambda x : x[1])

print(sorted_students)


# map travel kore 1 by one
numss = [2,3,6,4,5,8,9]
sq_nums = list(map(lambda x: x*x, numss))
print(sq_nums)

# filter

even = list(filter(lambda x:x%2 == 1, numss))
print(even)
















