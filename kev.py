
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Infinite"
    return x / y

def ask_question():
    print("Choice:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'exit' to end the program")

    data_input = input(": ")

    if data_input.lower() == "exit":
        return 0
    

    if data_input in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if data_input == "add":
            print("Answer:", add(num1, num2))
        elif data_input == "subtract":
            print("Answer:", subtract(num1, num2))
        elif data_input == "multiply":
            print("Answer:", multiply(num1, num2))
        elif data_input == "divide":
            print("Answer:", divide(num1, num2))
    else:
        print("Invalid input")

    print()
    print()
    ask_question()

ask_question()