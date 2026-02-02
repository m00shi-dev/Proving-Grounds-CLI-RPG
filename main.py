"""
 The main python file for Proving Grounds
 This is the file that starts the game and executes the main game loop
"""

import Player
import Items
import Enemy
import CLI
import Help
import time as t # Used for measuring performance
import Combat

"""
TODO:
[x] Implement help module
[x] Implement items
[ ] Implement shop
[x] Implement combat
[ ] Implement fighting random enemies
[ ] Implement drop table/drops
[ ] Implement areas
    [ ] Travel to different areas with different levels
[ ] Implement crafting
[x] Move string split to CLI class

[CHANGE LOG]
[1/31/26] Changes:
[REFACTOR]
- Moved item instantiation to Items.py. 
    -They can now be referenced with Items.object_name
- Move enemy instantiation to Enemy.py
    - They can now be referenced with Items.enemy_name
[ENHANCEMENTS]
-Added equipping items
    - Checks that slot is empty and item is in player objects inventory
    - Takes player input as a string, converts to list, strips first word from list,
      creates item string name, checks that item exists in the game, assigns the item
      object to a variable, and passes that variable to the equip_item() method in
      the player class. 

[2/1/26] Changes:
[REFACTOR]
- Moved code to update player weight from player.print_status() to player.update_player_stats()
- Command parsing refactored to now strip the or "root command" from 
  command string, and everything after is an "object command"
- Attempting to equip and item that doesn't exist will now print that the item
  doesn't exist.
- Resolved issue in main loop that would trigger player.equip_item() function.
- Added event counter to combat loop. 

[ENHANCEMENTS]
- Drop item implemented
    - Removes item from player inventory with a warning that it can't be undone.
"""      
game_load_start_time = t.time() # Start timer for game loading

# Initilize Player object

player = Player.Player(name="Bryant", hitpoints=100, gold=100, level=1, attack=0)

# [TESTING - DELETE] Delete this
player.inventory.append(Items.iron_dagger)
player.inventory.append(Items.copper_nugget)

# ==== LOADING TIME METRICS ====
print("==== PERFOMANCE METRICS ====")
# == GAME ==
game_load_end_time = t.time() # End timer for game loading
elapsed_game_load_time = game_load_end_time - game_load_start_time
formatted_elapsed_game_load_time = 'Game load time: {:.9f} seconds'.format(elapsed_game_load_time)
print(formatted_elapsed_game_load_time)

print("============================")
print("|   Proving Grounds CLI    |")
print("============================")
print("Type 'h' or 'help' for help")

x = True
while x:
    user_input = CLI.parse_user_input(CLI.sanitized_input())
    # Unpack dictionary items
    # Should these be in CLI?
    action_command = user_input['action_command']
    object_name = user_input['object_name']
    if action_command == 'q' or action_command == 'quit':
        x = False
    elif action_command == 'h' or action_command == 'help':
        Help.print_help()
    elif action_command == 'print items' or action_command == 'pi':
        for item in Items.item_list:
            print(f"==== {item.name} ====")
            print(f"Attack: {item.attack}\tArmor: {item.armor}\tMod Slots:{item.mod_slots}")
            print(f"Buy For: {item.buy_price} Sell For: {item.sell_price}\n")
    elif action_command == 'armor' or action_command == 'a':
        player.print_equipment()
    elif action_command == 'status' or action_command == 's':
        player.print_status()
    elif action_command == 'fight' or action_command == 'f':
        player.update_player_stats()
        Combat.main_combat_loop(player,Enemy.rat)
    elif action_command == 'inventory' or action_command == 'i':
        player.print_inventory()

    # ==== EQUIP ITEM ====
    elif action_command == 'equip' or action_command == 'e':
        item_found = False
        for item in Items.item_list:
            if item.name == object_name:
                player.equip_item(item)
                item_found = True
        if item_found == False:
            print(f"{object_name} doesn't appear to be an item!")
    elif action_command == 'drop' or action_command == 'd':
        item_found = False
        for item in Items.item_list:
            if item.name == object_name:
                if object_name in player.inventory:
                    verify_message = input(f"Are you sure you want to drop {item.name}?")
                    if verify_message == 'y' or verify_message == 'yes':
                        player.drop_item(item)
                    item_found = True
        if item_found == False:
            print(f"You do not have {object_name} in your inventory")
                
    # ==== [TESTING - DELETE] Testing equipping items ====#

    elif action_command == 'te':
        player.equip_item(item=Items.copper_mace)
        player.print_equipment()

    else:
        print(f"{action_command} is not a command. Type 'h' or 'help' for help.")