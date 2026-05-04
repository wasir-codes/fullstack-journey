a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b == 0:
        print("Error: division by zero")
    else:
        print(a / b)