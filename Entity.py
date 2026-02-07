"""
A module for creating entities in Proving Grounds
"""
entity_list = []
enemy_list = []
from random import choice

class Entity:
    def __init__(self, name: str, hp: int, mana: int, entity_class: str):
        """Initialize an entity"""
        self.name = name
        self.hp = hp
        self.mana = mana
        self.condition =  None,
        self.entity_class = entity_class
   
    def add_hp(self, heal_amount: int) -> int:
        """Add HP to an entity"""
        self.hp += heal_amount
        return self.hp 

    def subtract_hp(self, damage_amount: int) -> int:
        """Remove HP from an entity"""
        self.hp -= damage_amount
        return self.hp
    
    def add_mana(self, add_amount: int) -> int:
        """Add mana to a entity"""
        self.mana += add_amount
        return self.mana

    def subtract_mana(self, mana_cost: int) -> int:
        """Remove Mana from an entity"""
        self.mana -= mana_cost
        return self.mana

class Stats:
    """This will be bound to the stats attribute of the Player class"""
    def __init__(self, attack: int = 10, strength: int = 10, defense: int = 10, agility: int = 10):
        self.attack = attack
        self.strength = strength
        self.defense = defense
        self.agility = agility

    def level_up(self) -> None:
        "Increase all stats by 1"
        stat_list = [self.attack, self.strength, self.defense, self.agility]
        for stat in stat_list:
            stat += 1
        
    def calculate_dodge_chance(self) -> bool:
        dice_roll = [x for x in range(1, 101)]
        if choice(dice_roll) > self.agility:
            print("You were hit by the attack!")
            return False
        else:
            print("You managed to dodge the attack! Nice!")
            return True

class Player(Entity):
    """The player class
    This class will build the Player object"""
    
    def __init__(self, name: str, hp: int, mana: int, entity_class: str):
        super().__init__(name, hp, mana, entity_class)
        self.stats = Stats()
        self.equipment = {
            'head': {
                'attack': None,
                'armor': None,
                'weight': 0,
                'durability': 0, # Range 0 - 100. Represents how quickly an item degrades
                'condition': 0,
                'class': None, # heavy, medium, light
                'locked': False,
            },
            'neck': {
                'attack': None,
                'armor': None,
                'weight': 0,
                'durability': 0, # Range 0 - 100. Represents how quickly an item degrades
                'condition': 0,
                'class': None, # heavy, medium, light
                'locked': False,
            },
            'body': {
                'attack': None,
                'armor': None,
                'weight': 0,
                'durability': 0, # Range 0 - 100. Represents how quickly an item degrades
                'condition': 0,
                'class': None, # heavy, medium, light
                'locked': False,
            },
            'legs': {
                'attack': None,
                'armor': None,
                'weight': 0,
                'durability': 0, # Range 0 - 100. Represents how quickly an item degrades
                'condition': 0,
                'class': None, # heavy, medium, light
                'locked': False,
            },
           'gloves': {
                'attack': None,
                'armor': None,
                'weight': 0,
                'durability': 0, # Range 0 - 100. Represents how quickly an item degrades
                'condition': 0,
                'class': None, # heavy, medium, light
                'locked': False,
           },
           'right_hand': {
                'attack': None,
                'armor': None,
                'weight': 0,
                'durability': 0, # Range 0 - 100. Represents how quickly an item degrades
                'condition': 0,
                'class': None, # heavy, medium, light
                'locked': False,
           },
           'left_hand': {
                'attack': None,
                'armor': None,
                'weight': 0,
                'durability': 0, # Range 0 - 100. Represents how quickly an item degrades
                'condition': 0,
                'class': None, # heavy, medium, light
                'locked': False,
           },
           'feet':{
                'attack': None,
                'armor': None,
                'weight': 0,
                'durability': 0, # Range 0 - 100. Represents how quickly an item degrades
                'condition': 0,
                'class': None, # heavy, medium, light
                'locked': False,
           }
        }