num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Choose the operation (+, -, *, /): ").lower()
match operation:
    case "+":
        print(f"{num1} + {num2} = {float(num1) + float(num2)}")
    case "-":
        print(f"{num1} - {num2} = {float(num1) - float(num2)}")
    case "*":
        print(f"{num1} * {num2} = {float(num1) * float(num2)}")
    case "/":
        if float(num2) == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"{num1} / {num2} = {float(num1) / float(num2)}")