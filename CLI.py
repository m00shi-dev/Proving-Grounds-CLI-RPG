"""
The module for handling CLI functions
"""

def sanitized_input(user_input):
    """
    Sanitize user input with trim() and lower()
    """
    user_input = user_input.strip()
    user_input = user_input.lower()

    return user_input