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
[ ] Implement combat
[ ] Implement fighting random enemies
[ ] Implement drop table/drops
[ ] Implement areas
    [ ] Travel to different areas with different levels

[1/31/26] Changes:
- Moved item instantiation to Items.py. 
    -They can now be referenced with Items.object_name

"""

game_load_start_time = t.time() # Start timer for game loading

# Initilize Player object
player = Player.Player(name="Bryant", hitpoints=100, gold=100, level=1, attack=1)
# Delete this
player.inventory.append(Items.iron_dagger)
player.inventory.append(Items.copper_nugget)
player.inventory.append(Items.iron_mace)

# ==== LOADING TIME METRICS ====
print("==== PERFOMANCE METRICS ====")
# == ENEMIES ==
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
    user_input = CLI.sanitized_input(input("Command: "))
    if user_input == 'q' or user_input == 'quit':
        x = False
    elif user_input == 'h' or user_input == 'help':
        Help.print_help()
    elif user_input == 'print items' or user_input == 'pi':
        for item in Items.item_list:
            print(f"==== {item.name} ====")
            print(f"Attack: {item.attack}\tArmor: {item.armor}\tMod Slots:{item.mod_slots}")
            print(f"Buy For: {item.buy_price} Sell For: {item.sell_price}\n")
    elif user_input == 'armor' or user_input == 'a':
        player.print_equipment()
    elif user_input == 'status' or user_input == 's':
        player.print_status()
    elif user_input == 'fight' or user_input == 'f':
        player.update_player_stats()
        Combat.main_combat_loop(player,Enemy.rat)
    elif user_input == 'inventory' or user_input == 'i':
        player.print_inventory()

    # ==== EQUIP ITEM ====
    elif user_input.split()[0] == 'equip' or 'e':
        # build string to pass into equip_item:
        string_list = user_input.split()
        string_list.pop(0) # remove 'equip' or 'e' from string
        item_name = " ".join(string_list)
    # ALWAYS RETURNS FALSE BECAUSE Items.item_list constains objects and not strings
    # How do we compare to Items.item_list.name?
        for item in Items.item_list:
            if item.name == item_name:
                player.equip_item(item)
                
    # === TESTING EQUIPMENT === CAN DELETE === #

    elif user_input == 'te':
        player.equip_item(item=Items.copper_mace)
        player.print_equipment()
