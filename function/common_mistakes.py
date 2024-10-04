'''
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) if n > 1
'''
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def get_numbers(n):
    result = []
    for i in range(1,n+1):
        result.append(i)
    return result

if __name__ == '__main__':
    n = int(input("Enter number: "))
    print(get_numbers(n))
    print(get_numbers(20))
    print(get_numbers(30))
    print(get_numbers(40))
    print(fibonacci(10))
    print(fibonacci(12))