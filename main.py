import Items
import Entity
from CLI import CLI

# Assign class variables for easy reference
all_items = Items.item_list
armor_list = Items.armor_list
weapon_list = Items.weapon_list

all_enemies = Entity.enemy_list

player_name = input("What is your name?: ")
player_class = CLI.character_class_selection()
print(f"Excellent choice playing as a {player_class}!")
player = Entity.Player(name=player_name, hp=100, mana=100, entity_class=player_class) # Create a player with the defualt stat pool

# Try to access the stats
while player.stats.calculate_dodge_chance() == False:
    player.stats.calculate_dodge_chance()
