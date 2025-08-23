def some_function():
    # Example code before refactoring
    long_variable_name = "This is a very long string that exceeds the character limit set by PEP 8 guidelines."
    another_long_variable = "Another long string that also needs to be broken down into smaller parts for better readability."

    # Refactored code
    long_variable_name = (
        "This is a very long string that exceeds the character limit "
        "set by PEP 8 guidelines."
    )
    another_long_variable = (
        "Another long string that also needs to be broken down into "
        "smaller parts for better readability."
    )