class Player():
    """
    The player class.
    """
    equipment_dictionary = {
        'head': {
            'name': None, # Name of the item
            'armor': None, # How much armor the item has
            'attack': 0,
            'condition': 0, # Condition out of 100. This will break if it reaches 0. *PLACEHOLDER*
            'sell_price': None, # How much gold the item is worth
            'buy_price': None, # How much the player purchased the item for
            'mod_slots': None, # How many mods can be added to the item. *PLACEHOLDER*
        },
        'neck' : {
            'name': None, # Name of the item
            'armor': None, # How much armor the item has
            'attack': 0,
            'condition': 0, # Condition out of 100. This will break if it reaches 0. *PLACEHOLDER*
            'sell_price': None, # How much gold the item is worth
            'buy_price': None, # How much the player purchased the item for
            'mod_slots': None, # How many mods can be added to the item. *PLACEHOLDER*
        },
        'torso': {
            'name': None, # Name of the item
            'armor': None, # How much armor the item has
            'attack': 0,
            'condition': 0, # Condition out of 100. This will break if it reaches 0. *PLACEHOLDER*
            'sell_price': None, # How much gold the item is worth
            'buy_price': None, # How much the player purchased the item for
            'mod_slots': None, # How many mods can be added to the item. *PLACEHOLDER*
        },
        'legs' : {
            'name': None, # Name of the item
            'armor': None, # How much armor the item has
            'attack': 0,
            'condition': 0, # Condition out of 100. This will break if it reaches 0. *PLACEHOLDER*
            'sell_price': None, # How much gold the item is worth
            'buy_price': None, # How much the player purchased the item for
            'mod_slots': None, # How many mods can be added to the item. *PLACEHOLDER*
        },
        'feet' : {
            'name': None, # Name of the item
            'armor': None, # How much armor the item has
            'attack': 0,
            'condition': 0, # Condition out of 100. This will break if it reaches 0. *PLACEHOLDER*
            'sell_price': None, # How much gold the item is worth
            'buy_price': None, # How much the player purchased the item for
            'mod_slots': None, # How many mods can be added to the item. *PLACEHOLDER*
        }, 
        'hands':{
            'name': None, # Name of the item
            'armor': None, # How much armor the item has
            'attack': 5,
            'condition': 0, # Condition out of 100. This will break if it reaches 0. *PLACEHOLDER*
            'sell_price': None, # How much gold the item is worth
            'buy_price': None, # How much the player purchased the item for
            'mod_slots': None, # How many mods can be added to the item. *PLACEHOLDER*
        },
       'main_hand':{
            'name': None, # Name of the item
            'armor': None, # How much armor the item has
            'attack': 5,
            'condition': 0, # Condition out of 100. This will break if it reaches 0. *PLACEHOLDER*
            'sell_price': None, # How much gold the item is worth
            'buy_price': None, # How much the player purchased the item for
            'mod_slots': None, # How many mods can be added to the item. *PLACEHOLDER*
        }
    }

    def __init__(self, name, hitpoints, gold, level, equipment, attack=1):
        self.name = name
        self.hitpoints = hitpoints
        self.gold = gold
        self.level = level
        self.equipment = equipment
        self.attack = attack

    def update_player_stats(self, player_object):
        """
        Iterate through the equipment library and update the player's stats. 
        """
        new_attack = 1
        new_armor = 0
        for v in self.equipment_dictionary.values():
           if v['attack']:
               new_attack += v['attack'] 
           if v['armor']:
               new_armor += new_armor
        player_object.attack = new_attack
        player_object.armor = new_armor

    def print_equipment(self):
        """
        iterate through the equipment dictionary and print what the player is wearing.
        """
        for k, v in self.equipment_dictionary.items():
            if v['name'] == None:
                print(f"Your {k} slot is empty!")
            else:
                print(f"You are wearing a {v['name']} on your {k}")

    def print_status(self, player_object):
        self.update_player_stats(player_object)
        print("\n==== STATUS ====")
        print(f"Level: {self.level}")
        print(f"Health: {self.hitpoints}")
        print(f"Attack: {player_object.attack}")
        print(f"Armor: {player_object.armor}")
        print(f"Gold: {self.gold}")
        print("")