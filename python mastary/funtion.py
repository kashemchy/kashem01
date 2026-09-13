# user define function  - programmer nijer motho banabe
# built in funciton-- already banano.. ace


# print("Hello")
# input("Enter Your name")



# no input no return
def my_first():
    a = 10
    b = 12
    print(a+b)


my_first()  # function call kora ba switch kora


#2 input thakbe kinthu return thakbena

def add_two(a,b):
    print(a+b)

add_two(5,8)


# input return thakbe

def multiply_two(a,b):
    return a*b
result = multiply_two(12,2)
print(result)

def hello():
    return "Hello"

greetings = hello()
print(greetings)

def addition(a,b):
    result = a+b
    return result

r = addition(26, 45)
print(r)


def adds (*args):
    print(args)
    return sum(args)
p = adds(12,45,36,35,46,2,5,4,6)
print(p)

# key workd argumet

def my_func(f_name,l_name,age):
    print(f"My name is {f_name} {l_name}. I am {age} years old")

my_func(age = 25,f_name = "kashem", l_name = "Chowdhury")









# 