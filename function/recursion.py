'''
    Function Recall
    - Function is a group of statements with a meaningfull name
    - In Python, You can define a function using def keyword
    - function takes parameters. Parameters may have default value
    - Function should always return a value
    - Function can be called anywhere in your code
    - Function should be tested using statement 
        if __name__ == '__main__':  
    Recursive Function:
    - Function calls itself
    - Conditions 1. Base Case, 2. Recursive Case
'''
def sum_of_natural_loop(n):
    result = 0
    for i in range(1, n+1):
        result = result + i
    return result

def sum_of_natural(n):
    if n == 1: # Base Case
        return n
    else: # Recursive Case
        return n + sum_of_natural(n-1)

def factorial(n):
    """
        Factorial of a given positive number
        Parameters: n (int)
        Return: Factorial of a given number
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    n = int(input("Enter number: "))
    if n < 0:
        print("Number should be >= 0")
    else:
        print(f"The factorial of {n} is {factorial(n)}")