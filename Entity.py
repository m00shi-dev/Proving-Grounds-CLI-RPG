from __future__ import annotations
"""
A module for creating entities in Proving Grounds
"""
from random import choice
from typing import List, Callable, Tuple
import Items
from Items import Item, Weapon
from CLI import CLI
entity_list = []
enemy_list = []

class Entity:
    def __init__(self, name: str, hp: int = 100, mana: int = 100, entity_class: str = None):
        """Initialize an entity"""
        self.name = name
        self.hp = hp
        self.mana = mana
        self.condition =  None,
        self.entity_class = entity_class
        self.spells = Spells()
   
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

    def __init__(self, attack: int = 10, strength: int = 10, defense: int = 10, agility: int = 10, intelligence: int = 10):
        self.attack = attack
        self.strength = strength
        self.defense = defense
        self.agility = agility
        self.intelligence = intelligence

    def level_up(self) -> None:
        "Increase all stats by 1"
        stat_list = [self.attack, self.strength, self.defense, self.agility]
        for stat in stat_list:
            stat += 1
        
    def calculate_dodge_chance(self) -> bool:
        dice_roll = [x for x in range(1, 101)]
        result_of_roll = choice(dice_roll)
        if result_of_roll > self.agility:
            print(f"[{self.agility}/{result_of_roll}] You were hit by the attack!")
            return False
        else:
            print(f"[{self.agility}/{result_of_roll}] You managed to dodge the attack! Nice!")
            return True

class Player(Entity):
    """The player class
    This class will create and control the Player object"""
     
    def __init__(self, name: str, hp: int = 1, mana: int = 1, entity_class: str = None):
        super().__init__(name, hp, mana, entity_class)
        if self.entity_class == "warrior":
            self.stats = Stats(attack = 5, strength = 10, defense = 7, agility =2, intelligence=3)
            self.hp = 110
            self.mana = 15
        elif self.entity_class == "mage":
            self.stats = Stats(attack = 2, strength = 2, defense = 5, agility= 4, intelligence=10)
            self.hp = 90
            self.mana = 50
        elif self.entity_class == "rogue":
            self.stats = Stats(attack=10, strength=4, defense=2, agility=8, intelligence=3)
            self.hp = 90
            self.mana = 15
        elif self.entity_class == "traveler": 
            self.stats = Stats(attack=8, strength=8, defense=8, agility=6, intelligence=7)
            self.hp = 100
            self.mana = 30
        self.experience = 0
        self.condition = None
        self.inventory = []
        self.max_carry_weight = 50
        self.gold = 0
        self.equipment = {
            'head': {
                'item': None,
                'locked': False,
            },
            'neck': {
                'item': None,
                'locked': False,
            },
            'body': {
                'item': None,
                'locked': False,
            },
            'legs': {
                'item': None,
                'locked': False,
            },
           'gloves': {
                'item': None,
                'locked': False,
           },
           'right hand': {
                'item': None,
                'locked': False,
           },
           'left hand': {
                'item': None,
                'locked': False,
           },
           'feet':{
                'item': None,
                'locked': False,
           }
        }
        self.spells = Spells()
        
    def equip_item_check(self, item: Item) -> Tuple[bool, str]:
        """
        Check if an item is equippable

        Return tuple of the check result 
        """
        if item not in Items.item_list:
            return (False, f"{item} is not an item!")
        elif item not in self.inventory:
            # Item isn't in players inventory
            return (False, f"You don't have {item.name}.")
        elif self.equipment[item.equip_slot]['item'] != None:
            # Equipment slot is not empty
            return (False, f"You're already wearing an item in {item.equip_slot}.")
        elif item.equip_class != 'any':
            if self.entity_class != item.equip_class:
                # Can not be worn by the player's class
                return (False, f"Your class can't wear that item.")
        elif self.equipment[item.equip_slot]['locked'] == True:
            # Slot is locked for some reason, like equipping a two handed weapon
            return (False, f"That slot is locked. Are you wearing a two handed weapon?")
        else:
            return (True, f"{item.name.capitalize()} equipped to {item.equip_slot}!")

    def equip_item(self, item: Weapon) -> Tuple[bool, str] | None:
        """ Equips the item to the player if equip_item_check passes"""
        check_result = self.equip_item_check(item)
        if check_result[0] != True:
                return check_result[1] 
        elif check_result[0] == True:
            if item.equip_slot != "2h":
                self.equipment[item.equip_slot]['item'] = item
                self.inventory.remove(item)
            elif item.equip_slot == '2h':
                self.equipment['right_hand']['locked'] = True
                self.equipment['left_hand']['locked'] = True
            return check_result[1]
    
    def drop_item(self, item: Item) -> None:
        """Drop an item from inventory"""
        response = CLI.drop_item_check(item)
        if response[0] == True:
            self.inventory.remove(item)

    def calculate_carry_weight(self) -> int:
        """Add up the weight of all items on the player, and in their inventory
        return: int
        """
        carry_weight = 0
        # Add weight from all items in inventory
        for item in self.inventory:
            carry_weight += item.weight
        
        for item in self.equipment.values():
            if item['item'] != None:
                carry_weight += item['item'].weight
        return carry_weight
    
    def remove_item_check(self, item: Item) -> bool:
        """Check if the player has the carry capacity to remove the item"""
    
    def remove_item(self, item: Item) -> None:
        ...

class Spells:
    """A spells class to create and control spells
    
    reference with player_object.spells
    """

    def __init__(self):
        self.spells = {
            'zap': {
                'mana_cost': 10, 
                'int_required': 10,
                'base_damage': 6,
                'int_damage_scale': .2,
                'attribute': 'electric',
            },
            'fire bolt': {
                'mana_cost': 10, 
                'int_required': 10,
                'base_damage': 6,
                'int_damage_scale': .15,
                'attribute': 'fire',
            }
        }