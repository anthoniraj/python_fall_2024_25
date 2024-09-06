'''
    Write  a Python script to get name from user and 
    remove all vowels if present then display the name. 
'''
# E.g Python - Pythn
name = input("Enter your name: ")
for char in name.lower():
    if char not in 'aeiou':
        print(char, end='')

