"""
Task 1: Variable Declaration and Initialization

Complete the methods below by implementing the required functionality.
Each method has specific requirements detailed in the docstrings.

Run the tests with: python -m pytest tests/task01/ -v
"""

from typing import Union


class VariableExercises:
    """
    Python exercises for variable declaration and initialization.
    Unlike Java, Python uses dynamic typing - no need to declare types explicitly.
    """

    def initialize_integer(self) -> int:
        """
        Create and return an integer variable with the value 42
        
        Returns:
            int: The integer value 42
        """
        # TODO: Implement this method
        return 42

    def initialize_float(self) -> float:
        """
        Create and return a float variable with the value 3.14159
        
        Returns:
            float: The float value 3.14159
        """
        # TODO: Implement this method
        # raise NotImplementedError("Method not implemented yet")
        my_float = 3.14159
        return my_float


    def initialize_boolean(self) -> bool:
        """
        Create and return a boolean variable with the value True
        
        Returns:
            bool: The boolean value True
        """
        # TODO: Implement this method
        # raise NotImplementedError("Method not implemented yet")
        its_true = True
        return its_true

    def initialize_string(self) -> str:
        """
        Create and return a string variable with the value "Hello, World!"
        
        Returns:
            str: The string value "Hello, World!"
        """
        # TODO: Implement this method
        say_hi = "Hello, World!"
        return say_hi

    def initialize_list(self) -> list:
        """
        Create and return a list with the values [1, 2, 3, 4, 5]
        
        Returns:
            list: A list containing [1, 2, 3, 4, 5]
        """
        # TODO: Implement this method
        # raise NotImplementedError("Method not implemented yet")
        my_big_list = [1, 2, 3, 4, 5]
        return my_big_list


    def variable_reassignment(self) -> int:
        """
        Demonstrate variable reassignment in Python
        Start with value 10, then add 5, then multiply by 2
        
        Returns:
            int: The final calculated value (should be 30)
        """
        # TODO: Implement this method
        value = 10
        value += 5  # or value = value + 5
        value *= 2  # or value = value * 2
        return value
        # raise NotImplementedError("Method not implemented yet")

    def work_with_constants(self) -> int:
        """
        Work with constants in Python (conventionally UPPER_CASE)
        Create a constant with value 100 and return it
        Note: Python doesn't have true constants, but uses naming convention
        
        Returns:
            int: The constant value 100
        """
        # TODO: Implement this method
        CONSTANT_VALUE = 100
        return CONSTANT_VALUE
        # raise NotImplementedError("Method not implemented yet")

    def type_conversion(self) -> int:
        """
        Type conversion exercise
        Convert the float 9.99 to an integer (truncating the decimal)
        
        Returns:
            int: The integer value 9
        """
        # TODO: Implement this method
        original_value = 9.99
        return int(original_value)
        # raise NotImplementedError("Method not implemented yet")

    def multiple_assignment(self) -> tuple:
        """
        Demonstrate Python's multiple assignment feature
        Assign values 1, 2, 3 to variables a, b, c respectively and return them as a tuple
        
        Returns:
            tuple: A tuple containing (1, 2, 3)
        """
        # TODO: Implement this method
        # a, b, c = 1, 2, 3
        # return (a, b, c)
        a, b, c, = 1, 2, 3
        x, y, z = 7, 8, 9
        return (a, b, c)
        # raise NotImplementedError("Method not implemented yet")

    def dynamic_typing(self) -> tuple:
        """
        Demonstrate Python's dynamic typing
        Start with a variable as an integer 42, then reassign it to string "Hello"
        Return both values as a tuple
        
        Returns:
            tuple: A tuple containing (42, "Hello")
        """
        # TODO: Implement this method
        # variable = 42
        variable = 42
        # first_value = variable
        first_value = variable
        # variable = "Hello"
        variable = "Hello"
        # second_value = variable
        second_value = variable
        # return (first_value, second_value)
        return (first_value, second_value)
        # raise NotImplementedError("Method not implemented yet")
