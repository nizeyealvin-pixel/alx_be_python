def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations (add, subtract, multiply, divide)
    on two numbers based on the specified operation string.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 
                         'multiply', or 'divide').

    Returns:
        float or str: The result of the operation (float) or a specific 
                      error message (str) if division by zero occurs or 
                      the operation is unknown.
    """
    # Clean and standardize the operation string
    op = operation.strip().lower()

    if op == 'add':
        return num1 + num2
    
    elif op == 'subtract':
        return num1 - num2
    
    elif op == 'multiply':
        return num1 * num2
    
    elif op == 'divide':
        # Include handling for division by zero
        if num2 == 0:
            return "Division by zero is not allowed."
        return num1 / num2
    
    else:
        # Handle unrecognized operation input
        return f"Error: Unknown operation '{operation}'."
