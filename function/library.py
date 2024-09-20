def add(a = 1, b= 2):
    """
        Addition of Two Numbers
        Parameters:
        a (int): number one, Default value is 1
        b (int): number two, Default value is 2
        Return:
        (a+b)
    """
    return a+b

def subtract(a, b):
    return a-b

def greet(name="Raj"):
    return f"Welcome {name}"

def is_even_basic(number):
    if number % 2 == 0:
        return True
    else: 
        return False

def is_evn_modified(number):
    if number % 2 == 0:
        return True
    return False

def is_even(number):
    return number % 2 ==  0

def generate_even_numbers(limit):
    even_numbers = []
    for num in range(2, limit + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

if __name__ == '__main__':
    print(is_even(10))
    print(greet("Ant"))