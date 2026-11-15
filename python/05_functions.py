# 1

def square(x):
    return x*x

# print(square(2))
# print(square(5))
# print(square(10))
    
# 2

def is_even(n):
    return n % 2 == 0

# for i in range(1,7):
#     if is_even(i):
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

# 3

def average(numbers):
    avg = round(sum(numbers) / len(numbers),2)
    return avg


# print("Average:", average([2, 4 ,6]))
# print("Average:", average([1, 3 ,3]))

# 4 

def grade(percent):
    if percent >= 90:
        return 1
    elif percent >= 75:
        return 2
    elif percent >= 60:
        return 3
    elif percent >= 45:
        return 4
    else:
        return 5

# for n in [95,80,60,50,20]:
#     print(str(n) + "% ->",grade(n))

# 5

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    else:
        return a / b

def calculate(a, op, b):
    if op == "+":
        return(add(a, b))
    if op == "-":
        return(subtract(a, b))
    if op == "*":
        return(multiply(a, b))
    if op == "/":
        return(divide(a, b))
    return None

a = float(input("First number:"))
op =input("Operator (+ - * /):")
b = float(input("Second number:"))

result = calculate(a , op , b)
if result is None:
    print("Error")
else:
    print("Result:", result)





