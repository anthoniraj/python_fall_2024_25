while True:   
    try:
        a = int(input("Enter a:"))
        b = int(input("Enter b:")) 
        print(f"The addition is {a+b}")
        print(f"The division is {a/b}")
        print(f"The subtraction is {a-b}")
        print(f"The multiplication is {a*b}")
    except ZeroDivisionError:
        print("Division is not possible!")
    except ValueError:
        print("a and b should be numbers")
    flag = input('Do you want to continue (Yes/No): ')
    if flag.lower() == 'no':
        print('Good Bye!')
        break