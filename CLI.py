"""
The module for handling CLI functions
"""

prompt = "Command>> "

def sanitized_input():
    """
    Sanitize user input with trim() and lower()
    Do not call directly. This is used in parse_user_input()
    """
    user_input = input(prompt)
    user_input = user_input.strip()
    user_input = user_input.lower()

    return user_input

def parse_user_input(user_input):
    """
    Split user input workable, key-value pairs, then join with spaces
    returns a dictionary

    parsed_input_dictionary = {
                'full_command': 'equip iron dagger',
                'action_command': 'equip',
                'object_name': 'iron dagger',
    }

    """
    parsed_input_dictionary = {
        'full_command': None,
        'action_command': None,
        'object_name': None,
    }
    # Assign full command to parsed input dictionary
    parsed_input_dictionary['full_command'] = user_input 
    # Split the string into a list then join as a string without spaces
    user_input = user_input.split()
    try:
        if user_input[0] == 'print':
            two_word_command = f"{user_input[0]} {user_input[1]}"
            parsed_input_dictionary['action_command'] = two_word_command
        # Assign action command to action command in dictionary and remove from list
        else:
            parsed_input_dictionary['action_command'] = user_input.pop(0)
    except:
        pass
    # Join the remaining parts of string and add to dictionary
    user_input = " ".join(user_input)
    parsed_input_dictionary['object_name'] = user_input
        
    return parsed_input_dictionary 
    