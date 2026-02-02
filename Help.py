"""
Module for Help 

This module controls everything related to help
"""

help_message = "\n==== HELP PAGE ====\n"
help_message += "Tip: The first letter is an alias for most commands, or use the first\nletters of the command as an acronym\n"
help_message += "For example, 'Print Items' may be abbreviated as 'pi'\n\n"
help_message += "==== COMMAND LIST ====\n"
help_message += "'print items' - Prints a list of items in the game, and their attributesn\n"
help_message += "'armor' - Prints what the player is wearing\n"
help_message += "'status' - Prints players level, health, and gold."
help_message += "'quit' - Does exactly what you expect.\n"
help_message += "'inventory' - Print a list of items in your inventory"
help_message += "'equip' - Type 'equip' and then the item name to equip the item"
help_message += "'fight' to fight enemies"

def print_help():
   print(f"{help_message}\n") 