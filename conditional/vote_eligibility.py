age = int(input("Enter your age: "))
if age <= 0:
    print("Invalid age")
else:
    if age >= 18:
        print("Major")
    else:
        print("Minor")
    