from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains and prints the current date and time in a specific format.
    """
    # Obtain the current date and time
    current_date = datetime.now()
    
    # Format and print the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    
    return current_date

def calculate_future_date(current_date):
    """
    Prompts the user for a number of days and calculates the future date.

    Args:
        current_date (datetime): The starting date for the calculation.
    """
    while True:
        try:
            # Prompt the user for the number of days
            days_to_add_str = input("Enter the number of days to add to the current date: ")
            days_to_add = int(days_to_add_str)
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for the number of days.")
            continue
            
    # Calculate the future date using timedelta
    future_date = current_date + timedelta(days=days_to_add)
    
    # Print the future date in "YYYY-MM-DD" format
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")


def main():
    """
    Main function to run the datetime demonstrations.
    """
    # Part 1: Display Current Date and Time
    current_date = display_current_datetime()
    
    # Part 2: Calculate a Future Date
    calculate_future_date(current_date)


if __name__ == "__main__":
    main()
