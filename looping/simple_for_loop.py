'''
write a python program to print only even number
from the given list and filter with limit till 8
'''
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(f"The number is {number}")
    if number < 8 and number % 2 != 0:
        print(number)
