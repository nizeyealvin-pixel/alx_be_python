def calculate():
    """
    A simple calculator that uses the match-case statement to perform
    addition, subtraction, multiplication, and division on two numbers.
    """
    try:
        # Prompt for user input and convert numbers to float for calculation accuracy
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /): ")

        result = None
        
        # Use structural pattern matching (match-case) for the operation
        match operation:
            case '+':
                result = num1 + num2
            case '-':
                result = num1 - num2
            case '*':
                result = num1 * num2
            case '/':
                # Handle division by zero case gracefully
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Cannot divide by zero.")
                    return  # Exit the function if division by zero occurs
            case _:
                # Handle invalid operation input
                print("Invalid operation chosen. Please use +, -, *, or /.")
                return

        # Output the result if a calculation was successful
        if result is not None:
            print(f"The result is {result}.")

    except ValueError:
        # Handle non-numeric input for the numbers
        print("Invalid input. Please ensure you enter valid numbers.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Run the calculator function
if __name__ == "__main__":
    calculate()
