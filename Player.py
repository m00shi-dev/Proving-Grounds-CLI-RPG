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
            'attack': 0,
            'weight': 0,
            'condition': 0, # Condition out of 100. This will break if it reaches 0. *PLACEHOLDER*
            'sell_price': None, # How much gold the item is worth
            'buy_price': None, # How much the player purchased the item for
            'mod_slots': None, # How many mods can be added to the item. *PLACEHOLDER*
        },
       'main hand':{
            'name': None, # Name of the item
            'armor': None, # How much armor the item has
            'attack': 3,
            'weight': 0,
            'condition': 0, # Condition out of 100. This will break if it reaches 0. *PLACEHOLDER*
            'sell_price': None, # How much gold the item is worth
            'buy_price': None, # How much the player purchased the item for
            'mod_slots': None, # How many mods can be added to the item. *PLACEHOLDER*
        }
    }
        self.attack = attack
        self.current_carry_weight = 0
        self.carry_weight= 50
        self.inventory = []

    def update_player_stats(self):
        """
        Iterate over the player's equipment and update attack, armor, and weight
        Call this object to update the player object.
        """
        new_attack = 0
        new_armor = 0
        new_weight = 0
        for v in self.equipment.values():
           if v['attack']:
               new_attack += v['attack'] 
               print(f"Attack to add: {v['attack']}")
               print(f"New attack:{new_attack}")
           if v['armor']:
               new_armor += v['armor']
           if v['weight']:
               new_weight += v['weight']
        for item in self.inventory:
            if item.weight > 0:
                new_weight += item.weight
        self.attack = new_attack
        self.armor = new_armor
        self.current_carry_weight = new_weight


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
        print("\n==== STATUS ====")
        print(f"Level: {self.level}")
        print(f"Health: {self.hitpoints}")
        print(f"Attack: {self.attack}")
        print(f"Armor: {self.armor}")
        print(f"Gold: {self.gold}")
        print(f"Carry Weight: {self.current_carry_weight}/{self.carry_weight}")
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
            if item.body_part != None:
                self.equipment[item.body_part]['name'] = item.name
                self.equipment[item.body_part]['attack'] = item.attack
                self.equipment[item.body_part]['armor'] = item.armor
                self.equipment[item.body_part]['buy_price'] = item.buy_price
                self.equipment[item.body_part]['weight'] = item.weight
                self.equipment[item.body_part]['mod_slots'] = item.mod_slots
                self.equipment[item.body_part]['sell_price'] = item.sell_price
            elif item.body_part == None:
                print(f"You can't equip an {item.name}")
            else:
                print(f"[EQUIP SUCCESS] You have equipped {item.name} to your {item.body_part}!")            
                self.inventory.remove(item)
        elif item not in self.inventory:
            print(f"You do not own {item.name}")
        else:
            print(f"[EQUIP FAILURE] You are already wearing a {self.equipment[item.body_part]['name']} in {item.body_part}!")

    def drop_item(self, item):
        """
        Drop an item from the player's inventory
        :parameter item should be an item object
        """
        try:
            self.inventory.remove(item)
        except ValueError:
            print(f"{item.name} not found.")
    
    def compare_item(self, item1, item2):
        """
        Helper function to determine if items are equal
        This was used to determine if objects could be compared
        and found equal on separate lists
        """

        print(item1)
        print(item2)

        if item1 == item2:
            return True
        else:
            return False