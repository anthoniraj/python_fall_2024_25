'''
    Write  a Python script to get name from user and 
    remove all vowels if present then display the name. 
'''
while True:
    name = input("Enter your name: ")
    for char in name.lower():
        if char not in 'aeiou':
            print(char, end='')
    print()
    flag = input('Do you want to continue (Y/N)? ')
    if flag.lower() == 'n':
        break

print("I am outside the while loop")

    

