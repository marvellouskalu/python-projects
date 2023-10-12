import os

print("Welcome to my calculator")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero.")

operation = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}

def calculator():
    num1 = float(input("What is the first number?\n"))
    repeat = True

    while repeat: 
        choice = input("Enter your choice ('+', '-', '*', or '/'):\n ")
        num2 = float(input("What is the next number?\n"))

        if choice in operation:
            try:
                answer = operation[choice](num1, num2)
                print(f"{num1} {choice} {num2} = {answer}")
            except ValueError as e:
                print("Error:", str(e))
                break
        else:
            prin("Invalid input. Please try again.")
            continue

        print("\n")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.\n").lower() == "y":
            num1 = answer
        else:
            repeat = False
            if os.name == 'nt':  # Check if running on Windows
                os.system('cls')  # Clear console screen on Windows
            else:
                os.system('clear')  # Clear console screen on macOS and Linux


calculator()
