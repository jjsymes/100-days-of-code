from art import logo

def add(a , b):
    return a + b

def subtract(a , b):
    return a - b

def multiply(a , b):
    return a * b

def divide(a , b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator(initial_sum=None):
    if not initial_sum:
        print(logo)
    first_number = initial_sum

    valid_input = False
    while not valid_input and not first_number:
        first_number = input("What is your first number?: ")
        try:
            first_number = float(first_number)
            valid_input = True
        except ValueError:
            pass


    for symbol in operations:
        print(symbol)

    valid_input = False
    while not valid_input:
        operation = input("Pick an operation: ")
        if operation in operations.keys():
            valid_input = True

    valid_input = False
    while not valid_input:
        second_number = input("What is your second number?: ")
        try:
            second_number = float(second_number)
            valid_input = True
        except ValueError:
            pass

    func = operations[operation]
    result = func(first_number, second_number)
    print(f"{first_number} {operation} {second_number} = {result}")
    
    valid_input = False
    while not valid_input:
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if choice in ["y", "n", "yes", "no"]:
            valid_input = True
    
    if choice != "" and choice[0] == "y":
        calculator(result)
    else:
        calculator()


calculator()