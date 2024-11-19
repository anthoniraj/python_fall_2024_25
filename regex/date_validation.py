'''
Write a Python Program to validate date in dd-mm-yyyy format
dd-mm-yyyy
pattern: ^[0-9]{2}-[0-9]{2}-[0-9]{4}$
'''
import re
months_with_days = {
    "01": 31,  # January
    "02": 28,  # February
    "03": 31,  # March
    "04": 30,  # April
    "05": 31,  # May
    "06": 30,  # June
    "07": 31,  # July
    "08": 31,  # August
    "09": 30,  # September
    "10": 31,  # October
    "11": 30,  # November
    "12": 31,  # December
}

def check_month(month):
    if month in months_with_days.keys():
        return True
    return False

def check_days(day, month):
    for mon, d in months_with_days.items():
        if month == mon:
            if day <= d:
                return True
    return False

def validate_date(date):
    pattern = r'^[0-9]{2}-[0-9]{2}-[0-9]{4}$'
    if re.match(pattern, date):
        return True
    else:
        return False

if __name__ == '__main__':
    date = input("Enter date in dd-mm-yyyy format:")
    if validate_date(date):
        temp = date.split('-')
        if check_month(temp[1]):
            if check_days(int(temp[0]), temp[1]):
                print("The date format and day are correct ")
                # do the computation
            else:
                print(f"The day for {temp[1]} is not valid")
        else:
            print(f"The given month {temp[1]} is not valid")
    else:
        print("The date format is not valid")