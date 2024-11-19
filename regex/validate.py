import re
def validate_mobile(number):
    #pattern = r'^[6-9]{1}[0-9]{9}$'
    pattern = r'^[6-9][0-9]{9}$'
    if re.match(pattern, number):
        return True
    else:
        return False 

def validate_pincode(code):
    #pattern = r'^[1-9]{1}[2-4]{1}[0-9]{4}$'
    pattern = r'^[1-9][2-4][0-9]{4}$'
    if re.match(pattern, code):
        return True
    else:
        return False 

def validate_username(name):
    pattern = r'^[a-zA-Z0-9_]{3,15}$'
    if re.match(pattern, name):
        return True
    else:
        return False

if __name__ == '__main__':
    name = input("Enter name:")
    flag = validate_username(name)
    if flag:
        print(f'The given name {name} is valid')
    else:
       print(f'The given name {name} is invalid')       
    code = input("Enter mobile:")
    print(validate_mobile(code))