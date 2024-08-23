age = int(input("Enter your age: "))
# Ternary Operator
status = "Major" if age >=18 else "Minor" 
print(status)

# Similar to above syntax
if age >= 18:
    print("Major")
else:
    print("Minor")