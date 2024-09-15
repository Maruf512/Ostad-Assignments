# Variables
operations = [{"index":1, "name":"Add", "simble": "+"},
              {"index":2, "name":"Subtract", "simble": "-"},
              {"index":3, "name":"Multiply", "simble": "*"},
              {"index":4, "name":"Divide", "simble": "/"},
              {"index":5, "name":"Modulus", "simble": "%"}]


def calculation(first_number, second_number, operation):
    if operation == 1:
        return first_number + second_number
    elif operation == 2:
        return first_number - second_number
    elif operation == 3:
        return first_number * second_number
    elif operation == 4:
        if second_number == 0:
            return "Cannot divide by zero!!!"
        else:
            return first_number / second_number
    elif operation == 5:
        return first_number % second_number
    else:
        return "Invalid operation!!!"


while True:
    print("Select operation: ")
    for item in operations:
        print(f"{item['index']}. {item['name']}")

    # Error Handling
    try:
        # Get user input
        operation = int(input("Chose one from Above(1/2/3....): "))
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        # Input Validation
        if operation <= len(operations):
            final_value = calculation(first_number, second_number, operation)
            print("+++++++++++++++++ Output +++++++++++++++++")
            print(f"{first_number} {operations[operation - 1]["simble"]} {second_number} = {final_value}")
            print("+++++++++++++++++ Output +++++++++++++++++\n")
        else:
            print("\nInvalid operation. Please select a valid operation.")

    except Exception as e:
        print("\nInvalid input. Please enter numbers only and select a valid operation.\n")
        print(f"{e}\n")
