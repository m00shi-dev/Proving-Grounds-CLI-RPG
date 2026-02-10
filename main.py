import Items
import Entity
from CLI import CLI

# Assign class variables for easy reference
all_items = Items.item_list
armor_list = Items.armor_list
weapon_list = Items.weapon_list
all_enemies = Entity.enemy_list

# Welcome screen
CLI.print_welcome_screen()

player_name = CLI.console.input("[bold]What is your [yellow]name[/yellow]?[/bold]\n[[yellow bold]Name[/yellow bold]]>>")
player_class = CLI.character_class_selection()
player = Entity.Player(name=player_name, entity_class=player_class) # Create a player with the defualt stat pool

player.inventory.append(Items.test_armor)
player.inventory.append(Items.test_weapon)

CLI.menu_state = "main menu"
while True:
    player_input = CLI.convert_input_to_dict(CLI.pretty_prompt())
    core_command = player_input['core_command'].lower()
    if core_command == 'h' or core_command == 'help':
        CLI.print_help()
    elif core_command == 'q' or core_command == 'quit':
        CLI.console.print(f"[bright_white on red] See ya, {player.name} [/]:wave:")
        CLI.console.print(f"Saving isn't implemented yet, so get rekt nerd! :grinning_squinting_face:")
        break
    elif core_command == 's' or core_command == 'stats':
        CLI.menu_state = "stats"
        CLI.print_player_stats(player)
        while True:
            # Print sources for stat increase?
            stat_input = CLI.convert_input_to_dict(CLI.pretty_prompt())
            core_command = stat_input['core_command']
            if core_command == 'h' or core_command == 'help':
                CLI.print_help()
            elif core_command == 'b' or core_command == 'back':
                CLI.menu_state = 'main menu'
                break
    elif core_command == 'i' or core_command == 'inventory' or core_command == 'inv':
        CLI.menu_state = "inventory"
        while True:
            inventory_input = CLI.convert_input_to_dict(CLI.pretty_prompt())
            core_command = inventory_input['core_command']
            secondary_command = inventory_input['secondary_command']
            if core_command == 'h' or core_command == 'help':
                CLI.print_help()
            elif core_command == 'g' or core_command == 'gear':
                CLI.print_equipped_items(player)
            elif core_command == 'e' or core_command == "equip":
                equip_message = player.equip_item(secondary_command)
                CLI.console.print(equip_message)
            elif core_command == 'b' or core_command == 'back':
                CLI.menu_state = 'main menu'
                break
            elif core_command == 'd' or core_command == 'drop':
                player.drop_item(secondary_command)
            elif core_command == 'v' or core_command == 'view':
                CLI.view_item(secondary_command)
            elif core_command == 'i' or core_command == 'inv' or core_command == 'inventory':
                CLI.print_inventory(player)
    elif core_command == "t" or core_command == "travel":
        CLI.menu_state = "travel"
        while True:
            travel_input = CLI.convert_input_to_dict(CLI.pretty_prompt())
            core_command = travel_input['core_command']
            secondary_command = travel_input['secondary_command']
            if core_command == 'h' or core_command == "help":
                CLI.print_help()
            if core_command == 'b' or core_command == 'back':
                CLI.menu_state = 'main menu'
                break
        # Enter travel menu
        # Players should be able to travel to different locations
    elif core_command == "f" or core_command == "fight":
        # Enter combat menu
        # Players should be able to pick an enemy to fight based on the area they're in. 
        CLI.menu_state = 'fight'
    elif core_command == "sh" or core_command == "shop":
        # Enter shop menu
        # Players should be able to buy and sell
        CLI.menu_state = 'shop'
    else:
        CLI.console.print("[misty_rose3] That is not a recognized command")

