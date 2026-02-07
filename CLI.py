from typing import LiteralString
"""Handles printing messages and player input"""

class CLI:

    def convert_input_to_int(input: str) -> int | bool:
        try:
           converted_input = int(input)
        except ValueError:
            return False 
        return converted_input

    def character_class_selection() -> str:
        class_selection_message = "What class would you like to play?\n"
        class_selection_message += "1. Warrior\n"
        class_selection_message += "2. Rogue\n"
        class_selection_message += "3. Mage\n"
        class_selection_message += "Enter number for your selection >> "
        
        while True:
            selection = CLI.convert_input_to_int(input(class_selection_message))
            while selection == False:
                print("That is not a class. Please try again.")
                selection = CLI.convert_input_to_int(input(class_selection_message))
            else:
                break 
            
        if selection == 1:
            return "warrior"
        if selection == 2:
            return "rogue"
        if selection == 3:
            return "mage"