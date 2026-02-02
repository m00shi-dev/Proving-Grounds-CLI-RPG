"""
The equipment class for Proving Grounds. This class will contain all methods pertaining to:
creating equipment

Instantiate items at the bottom of this file. 
"""
import time as t

class Items():
    """
    The class for creating items
    """

    def __init__(self, name, attack, armor, sell_price, buy_price, body_part, mod_slots=0, material=None, weight=1):
        """ 
        Initialize an item
        """
        self.name = name
        self.attack = attack
        self.armor = armor
        self.sell_price = sell_price
        self.buy_price = buy_price
        self.mod_slots = mod_slots
        self.body_part = body_part
        self.material = material
        self.weight = weight
        self.item_list = []

class Shop:
    """
    The Shop class. This class controls the buying and selling of items. 
    This class will be the super class to the various shops.

    Shops can be armor, weapons, potions, crafting.
    """

    def __init__(self, shop_name, shop_type='general', shop_gold = 100):
        """
        Initialize the shop
        """
        self.shop_name = shop_name
        self.shop_type = shop_type
        self.shop_inventory = [] # A list containing the items for sale.
        self.shop_gold = shop_gold # The amount of gold the shop has

    def buy_item(self, player, item):
        """
        Buy an item from the shop
        """
        # Check player weight, player gold, and shop inventory
        # Add item player is attempting to buy to temporary weight variable and 
        # check that the item will not put the player over the player.carry_weight
        # [TODO] Accept item name input similar to equip_item() in main
        player.update_player_stats(player)
        temp_weight = item.weight + player.current_carry_weight
        if temp_weight > player.carry_weight:
            print(f"You can't carry that much weight.")
            print(f"Carry weight: {player.current_carry_weight}/{player.carry_weight} ")
            print(f"Item weight: {item.weight}")
        if player.gold < item.buy_price:
            print(f"You don't have enough gold to buy that!")
            print(f"Gold: {player.gold}")
            print(f"Item price: {item.buy_price}")
        if item not in self.shop_inventory:
            print(f"That isn't sold here.")
        
    def print_for_sale(self):
        """
        Print the items for sale in the shop
        """
        # [TODO] Make the list print as a table similar to player.print_inventory()
        for item in self.shop_inventory:
            print(item)

    def initialize_items(self):
        """Load items into memory and place in item_list"""

print("Initializing items...")
item_load_start_time = t.time() # Start timer for item loading

# ==== MATERIALS ====
copper_nugget = Items(name='copper nugget', attack=0, armor=0, sell_price=5, buy_price=15, mod_slots=0, 
                            body_part=None, material='copper', weight=.5)
leather_strip = Items(name='leather strip', attack=0, armor=0, sell_price=3, buy_price=15, mod_slots=0,
                      body_part=None, material='leather', weight=.5)

# ==== WEAPONS === #
# == DAGGERS ==
iron_dagger = Items(name='iron dagger', attack=11, armor=0, sell_price=25, buy_price=75, mod_slots=1, 
                          body_part = 'main hand', material='iron', weight=1)

# == SWORDS == #
copper_sword = Items(name='basic sword', attack=10, armor=0, sell_price=3, buy_price=10, mod_slots=0,
                           body_part='main_haind', material='iron', weight=2)
iron_sword = Items(name='iron sword', attack=20, armor=0, sell_price=50, buy_price=250, mod_slots=2, 
                         body_part='main hand', material='iron', weight=3)

# == MACES == #
copper_mace = Items(name='copper mace', attack=10, armor=0, sell_price=5, buy_price=10, mod_slots=0,
                          body_part = 'main hand', material='copper', weight=2)
iron_mace = Items(name='iron mace', attack=25, armor=0, sell_price=50, buy_price=250, mod_slots=1,
                        body_part='main hand', material='copper', weight=3)

# == WANDS == #
obsidian_wand = Items(name='obsidian wand', attack=15, armor=0, sell_price=100000, buy_price=100000000, body_part='main hand',
                      mod_slots=5, material='obsidian', weight=1)

# ==== ARMOR ==== #
# == LEATHER ==   #
leather_helmet = Items(name='leather helmet', attack=0, armor=1, sell_price=3, buy_price=10, mod_slots=0,
                             body_part='head', material='leather', weight=.5)
leather_shoes = Items('leather shoes', attack=0, armor=1, sell_price=1, buy_price=3, mod_slots=0,
                            body_part='feet', material='leather', weight=.5)
leather_gloves = Items(name='leather gloves', attack=0, armor=1, sell_price=1, buy_price=3, mod_slots=0,
                             body_part='hands', material='leather', weight=.5)
leather_tunic = Items(name='leather tunic', attack=0, armor=5, sell_price=10, buy_price=20, mod_slots=0,
                            body_part='body', material='leather', weight=1)

#==== ITEM LIST ====#
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
item_list.append(copper_nugget)
item_list.append(leather_strip)
item_list.append(obsidian_wand)

item_load_end_time = t.time() # End timer for item loading

# == ITEMS ==
elapsed_item_load_time = item_load_end_time - item_load_start_time
formatted_elapsed_item_load_time = 'Item load time: {:.9f} seconds'.format(elapsed_item_load_time)
print(formatted_elapsed_item_load_time)
        
