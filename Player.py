class Player():
    """
    The player class.
    """
     
    def __init__(self, name, hitpoints, gold, level, attack=1):
        self.name = name
        self.hitpoints = hitpoints
        self.gold = gold
        self.level = level
        self.equipment = {
        'head': {
            'name': None, # Name of the item
            'armor': None, # How much armor the item has
            'attack': 0,
            'weight': 0,
            'condition': 0, # Condition out of 100. This will break if it reaches 0. *PLACEHOLDER*
            'sell_price': None, # How much gold the item is worth
            'buy_price': None, # How much the player purchased the item for
            'mod_slots': None, # How many mods can be added to the item. *PLACEHOLDER*
        },
        'neck' : {
            'name': None, # Name of the item
            'armor': None, # How much armor the item has
            'attack': 0,
            'weight': 0,
            'condition': 0, # Condition out of 100. This will break if it reaches 0. *PLACEHOLDER*
            'sell_price': None, # How much gold the item is worth
            'buy_price': None, # How much the player purchased the item for
            'mod_slots': None, # How many mods can be added to the item. *PLACEHOLDER*
        },
        'torso': {
            'name': None, # Name of the item
            'armor': None, # How much armor the item has
            'attack': 0,
            'weight': 0,
            'condition': 0, # Condition out of 100. This will break if it reaches 0. *PLACEHOLDER*
            'sell_price': None, # How much gold the item is worth
            'buy_price': None, # How much the player purchased the item for
            'mod_slots': None, # How many mods can be added to the item. *PLACEHOLDER*
        },
        'legs' : {
            'name': None, # Name of the item
            'armor': None, # How much armor the item has
            'attack': 0,
            'weight': 0,
            'condition': 0, # Condition out of 100. This will break if it reaches 0. *PLACEHOLDER*
            'sell_price': None, # How much gold the item is worth
            'buy_price': None, # How much the player purchased the item for
            'mod_slots': None, # How many mods can be added to the item. *PLACEHOLDER*
        },
        'feet' : {
            'name': None, # Name of the item
            'armor': None, # How much armor the item has
            'attack': 0,
            'weight': 0,
            'condition': 0, # Condition out of 100. This will break if it reaches 0. *PLACEHOLDER*
            'sell_price': None, # How much gold the item is worth
            'buy_price': None, # How much the player purchased the item for
            'mod_slots': None, # How many mods can be added to the item. *PLACEHOLDER*
        }, 
        'hands':{
            'name': None, # Name of the item
            'armor': None, # How much armor the item has
            'attack': 5,
            'weight': 0,
            'condition': 0, # Condition out of 100. This will break if it reaches 0. *PLACEHOLDER*
            'sell_price': None, # How much gold the item is worth
            'buy_price': None, # How much the player purchased the item for
            'mod_slots': None, # How many mods can be added to the item. *PLACEHOLDER*
        },
       'main hand':{
            'name': None, # Name of the item
            'armor': None, # How much armor the item has
            'attack': 5,
            'weight': 0,
            'condition': 0, # Condition out of 100. This will break if it reaches 0. *PLACEHOLDER*
            'sell_price': None, # How much gold the item is worth
            'buy_price': None, # How much the player purchased the item for
            'mod_slots': None, # How many mods can be added to the item. *PLACEHOLDER*
        }
    }
        self.attack = attack
        self.carry_weight= 50
        self.inventory = []

    def update_player_stats(self):
        """
        Iterate through the equipment library and update the player's stats. 
        """
        new_attack = 1
        new_armor = 0
        for v in self.equipment.values():
           if v['attack']:
               new_attack += v['attack'] 
           if v['armor']:
               new_armor += new_armor
        self.attack = new_attack
        self.armor = new_armor

    def print_equipment(self):
        """
        iterate through the equipment dictionary and print what the player is wearing.
        """
        for k, v in self.equipment.items():
            if v['name'] == None:
                print(f"Your {k} slot is empty!")
            else:
                print(f"You are wearing a {v['name']} on your {k}")

    def print_status(self):
        self.update_player_stats()
        # Update weight from inventory and equipment
        equipment_weight = 0
        for k,v in self.equipment.items():
            if v['weight']:
                equipment_weight += v['weight']
        for item in self.inventory:
            if item.weight > 0:
                equipment_weight += item.weight
        print("\n==== STATUS ====")
        print(f"Level: {self.level}")
        print(f"Health: {self.hitpoints}")
        print(f"Attack: {self.attack}")
        print(f"Armor: {self.armor}")
        print(f"Gold: {self.gold}")
        print(f"Carry Weight: {equipment_weight}/{self.carry_weight}")
        print("")

    def equip_item_old(self, item):
        """
        Old equip item method. Do not use this method.
        There are several checks missing from this method.
        Use equip_item() instead.
        """
        for k,v in self.equipment.items():
            if item.body_part == k:
                v['name'] = item.name
                v['armor'] = item.armor
                v['attack'] = item.attack
                v['sell_price'] = item.sell_price
                v['buy_price'] = item.buy_price
                v['mod_slots'] = item.mod_slots
                v['weight'] = item.weight

    def print_inventory(self):
        """
        Print the players inventory 
        """
        print("Name\t\tAttack\tArmor\tSell Price   Mod Slots")
        print("==========================================================")
        for item in self.inventory:
            print (f"{item.name}\t{item.attack}\t{item.armor}\t  {item.sell_price}\t\t{item.mod_slots}")

    def equip_item(self, item):
        """
        Equip an item from the player's inventory
        """
        if self.equipment[item.body_part]['name'] == None and item in self.inventory:
            self.equipment[item.body_part]['name'] = item.name
            self.equipment[item.body_part]['attack'] = item.attack
            self.equipment[item.body_part]['armor'] = item.armor
            self.equipment[item.body_part]['buy_price'] = item.buy_price
            self.equipment[item.body_part]['weight'] = item.weight
            self.equipment[item.body_part]['mod_slots'] = item.mod_slots
            self.equipment[item.body_part]['sell_price'] = item.sell_price

            print(f"[EQUIP SUCCESS] You have equipped {item.name} to your {item.body_part}!")            
            self.inventory.remove(item)
        elif item not in self.inventory:
            print(f"You do not own {item.name}")
        else:
            print(f"[EQUIP FAILURE] You are already wearing a {self.equipment[item.body_part]['name']} in {item.body_part}!")