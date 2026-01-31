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

game_load_start_time = t.time() # Start timer for game loading

# Initilize Player object
player = Player.Player(name="Bryant", hitpoints=100, gold=100, level=1, equipment={}, attack=1)
player.equipment = player.equipment_dictionary

# Create items for the game
# The items should be in the initialized in Items class, not instantiated in the main file, but here we are.
# AFTER CREATING THE ITEM, IT MUST BE ADDED TO THE ITEM LIST - /== ITEM LIST

print("Initializing items...")
item_load_start_time = t.time() # Start timer for item loading

# ==== WEAPONS === #
# == DAGGERS ==
iron_dagger = Items.Items(name='iron dagger', attack=11, armor=0, sell_price=25, buy_price=75, mod_slots=1, 
                          body_part = 'main_hand')

# == SWORDS == #
copper_sword = Items.Items(name='basic sword', attack=10, armor=0, sell_price=3, buy_price=10, mod_slots=0,
                           body_part='main_haind')
iron_sword = Items.Items(name='iron sword', attack=20, armor=0, sell_price=50, buy_price=250, mod_slots=2, 
                         body_part='main_hand')

# == MACES == #
copper_mace = Items.Items(name='copper mace', attack=10, armor=0, sell_price=5, buy_price=10, mod_slots=0,
                          body_part = 'main_hand')
iron_mace = Items.Items(name='iron mace', attack=25, armor=0, sell_price=50, buy_price=250, mod_slots=1,
                        body_part='main_hand')

# == WANDS == #

# ==== ARMOR ==== #
# == LEATHER ==   #
leather_helmet = Items.Items(name='leather helmet', attack=0, armor=1, sell_price=3, buy_price=10, mod_slots=0,
                             body_part='head')
leather_shoes = Items.Items('leather shoes', attack=0, armor=1, sell_price=1, buy_price=3, mod_slots=0,
                            body_part='feet')
leather_gloves = Items.Items(name='leather gloves', attack=0, armor=1, sell_price=1, buy_price=3, mod_slots=0,
                             body_part='hands')
leather_tunic = Items.Items(name='leather tunic', attack=0, armor=5, sell_price=10, buy_price=20, mod_slots=0,
                            body_part='body')

# ==== ITEM LIST ====#
item_list = []
item_list.append(copper_sword)
item_list.append(leather_helmet)
item_list.append(copper_mace)
item_list.append(leather_gloves)
item_list.append(leather_shoes)
item_list.append(leather_tunic)
item_list.append(iron_sword)
item_list.append(iron_mace)
item_list.append(iron_dagger)

item_load_end_time = t.time() # End timer for item loading

# ==== ENEMIES ====
print("Initializing enemies...")
enemy_load_start_time = t.time()
rat = Enemy.Enemy(name='rat', attack=2, defense =1, hitpoints=5, condition=None, equipment={})
goblin = Enemy.Enemy(name='goblin', hitpoints=50, attack=3, defense=3, condition=None, equipment={})

enemy_list = []

enemy_load_end_time = t.time()

# ==== LOADING TIME METRICS ====
print("==== PERFOMANCE METRICS ====")
# == ITEMS ==
elapsed_item_load_time = item_load_end_time - item_load_start_time
formatted_elapsed_item_load_time = 'Item load time: {:.9f} seconds'.format(elapsed_item_load_time)
print(formatted_elapsed_item_load_time)

# == ENEMIES ==
elapsed_enemy_load_time = enemy_load_end_time - enemy_load_start_time
formatted_elapsed_enemy_load_time = 'Enemy load time: {:.9f} seconds'.format(elapsed_enemy_load_time)
print(formatted_elapsed_enemy_load_time)

# == GAME ==
game_load_end_time = t.time() # End timer for game loading
elapsed_game_load_time = game_load_end_time - game_load_start_time
formatted_elapsed_game_load_time = 'Game load time: {:.9f} seconds'.format(elapsed_game_load_time)
print(formatted_elapsed_game_load_time)

print("============================")
print("|   Proving Grounds CLI    |")
print("============================")
print("Type 'h' or 'help' for help")


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
"""

x = True

while x:
    user_input = CLI.sanitized_input(input("Command: "))
    if user_input == 'q' or user_input == 'quit':
        x = False
    if user_input == 'h' or user_input == 'help':
        Help.print_help()
    if user_input == 'print items' or user_input == 'pi':
        for item in item_list:
            print(f"==== {item.name} ====")
            print(f"Attack: {item.attack}\tArmor: {item.armor}\tMod Slots:{item.mod_slots}")
            print(f"Buy For: {item.buy_price} Sell For: {item.sell_price}\n")
    if user_input == 'armor' or user_input == 'a':
        player.print_equipment()
    if user_input == 'status' or user_input == 's':
        player.print_status(player)
    if user_input == 'fight' or user_input == 'f':
        Combat.main_combat_loop(player,rat)
        
    # === TESTING EQUIPMENT === CAN DELETE === #
    if user_input == 'te':
        Items.Items.equip_item(item=copper_mace, player_object=player)
        player.print_equipment()