def add(a = 1, b= 2):
    return a+b

def subtract(a, b):
    return a-b

def greet(name="Raj"):
    return f"Welcome {name}"

'''
Write a python function to check the given
number is even
'''
def is_even(number):
    if number % 2 == 0:
        return True
    else: 
        return False

def is_evn_modified(number):
    if number % 2 == 0:
        return True
    return False

def is_even_optimized(number):
    return number % 2 ==  0

def generate_even_numbers(limit):
    even_numbers = []
    for num in range(2, limit + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

result = generate_even_numbers(10)
print(result)
