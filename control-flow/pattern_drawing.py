def draw_pattern():
    """
    Prompts the user for a positive integer (size) and draws a square
    pattern of asterisks using a while loop nested with a for loop.
    """
    while True:
        try:
            # 1. Prompt User for Pattern Size
            size_input = input("Enter the size of the pattern (positive integer): ")
            size = int(size_input)

            # Validate that the input is a positive integer
            if size <= 0:
                print("Please enter a positive integer greater than zero.")
                continue  # Go back to the start of the while loop for new input
            
            break # Exit the input loop if input is valid
            
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a whole number.")

    print(f"\nDrawing a {size}x{size} square pattern:")

    # Row counter for the outer WHILE loop
    row_count = 0

    # Outer loop (WHILE loop) iterates through the rows
    while row_count < size:
        # Inner loop (FOR loop) iterates through the columns/stars in the current row
        for _ in range(size):
            # Print an asterisk without a newline character
            print("*", end="")
        
        # After the FOR loop finishes (one row is complete), print a newline
        print()
        
        # Increment the row counter to move to the next row
        row_count += 1
        
# Execute the function
if __name__ == "__main__":
    draw_pattern()
