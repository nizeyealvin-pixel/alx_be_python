class Calculator:
    """A calculator class demonstrating class methods and static methods."""
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Add two numbers together.
        
        This is a static method that doesn't need access to class or instance data.
        
        Args:
            a (float): The first number
            b (float): The second number
            
        Returns:
            float: The sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Multiply two numbers together.
        
        This is a class method that can access class attributes via cls.
        
        Args:
            cls: The class itself (automatically passed)
            a (float): The first number
            b (float): The second number
            
        Returns:
            float: The product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b