# Define Global Conversion Factors
# Factors are calculated based on the standard formulas:
# C = (F - 32) * (5/9)
# F = C * (9/5) + 32
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit: float) -> float:
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.
    """
    # Formula: C = (F - 32) * (5/9)
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.
    """
    # Formula: F = C * (9/5) + 32
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    """
    Handles user interaction and demonstrates the temperature conversion functions.
    """
    print("--- Temperature Conversion Tool ---")
    
    # 1. Get Temperature Value with validation
    while True:
        temp_str = input("Enter the temperature to convert: ").strip()
        try:
            temperature = float(temp_str)
            break
        except ValueError:
            # Raise a specific error message for non-numeric input
            raise ValueError("Invalid temperature. Please enter a numeric value.")
            
    # 2. Get Unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    # 3. Perform Conversion and Output Result
    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
        
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
        
    else:
        print("Invalid unit input. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        # Catch the specific error raised in main()
        print(e)
