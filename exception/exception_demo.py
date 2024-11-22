'''
Python: Exception is an event that interrupts the normal flow of a program when something unexpected or runtime error happens during execution.
Types of Error
1. Syntax Error
2. Logical Error
3. Runtime Error
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

try:
    print(factorial(1000))
except:
    print("Use small numbers (<=100)")


a = int(input("Enter a:"))
b = int(input("Enter b:"))
print(f"The addition is {a+b}")
try:
    print(f"The division is {a/b}")
except ZeroDivisionError:
    print("Division is not possible!")
except ValueError:
    print("message")
print(f"The subtraction is {a-b}")
print(f"The mul is {a*b}")

filename = input('Enter the filename: ')
content = []
try:
    f=open(filename)
    content = f.readlines()
    f.close()
except FileNotFoundError:
    f=open('C:\\Users\\antho\\Documents\\gitws\\python_fall_2024_25\\exception\\demo.txt')
    content= f.readlines()
    f.close()

print(content)

