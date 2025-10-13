def generate_table():
    """
    Prompts the user for a number and generates its multiplication table
    from 1 to 10 using a for loop.
    """
    try:
        # 1. Prompt User for a Number
        number_str = input("Enter a number to see its multiplication table: ")
        # Convert the input to an integer
        number = int(number_str)

        print(f"--- Multiplication Table for {number} (1 to 10) ---")

        # 2. Generate and Print the Multiplication Table
        # Iterate from 1 up to (and including) 10
        for i in range(1, 11):
            # Calculate the product
            product = number * i
            
            # Print the result in the required format: "X * Y = Z"
            print(f"{number} * {i} = {product}")

    except ValueError:
        # Handle cases where the input is not a valid integer
        print("Invalid input. Please enter a whole number.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Execute the function
if __name__ == "__main__":
    generate_table()