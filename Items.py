"""
The equipment class for Proving Grounds. This class will contain all methods pertaining to:
creating equipment
"""
import Player

class Items():
    """
    The class for creating items
    """

    def __init__(self, name, attack, armor, sell_price, buy_price, body_part, mod_slots=0):
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

    def equip_item(item, player_object):
        """
        Pass the item and player object to update the player's equipment library
        """
        for k,v in player_object.equipment_dictionary.items():
            if item.body_part == k:
                v['name'] = item.name
                v['armor'] = item.armor
                v['attack'] = item.attack
                v['sell_price'] = item.sell_price
                v['buy_price'] = item.buy_price
                v['mod_slots'] = item.mod_slots