'''Items module'''

class Item:
    '''Parent class of all items'''
    def __init__(self, name: str, material: str, buy_price: int, sell_price: int, weight: float = .5):
        self.name = name
        self.material = material 
        self.buy_price = buy_price 
        self.sell_price = sell_price 
        self.condition: int = 100
        self.weight = weight

class Weapon(Item):
    '''Weapon class'''
    def __init__(self, name: str, material: str, buy_price: int, sell_price: int, weight: float, attack: int, equip_slot: str, equip_class: str):
        super().__init__(name, material, buy_price, sell_price, weight)
        self.equip_class = equip_class
        self.attack = attack
        self.equip_slot = equip_slot

class Armor(Item):
    def __init__(self, name:str, material: str, buy_price: int, sell_price: int, weight: float, armor: int, equip_slot: str, equip_class: str):
        super().__init__(name, material, buy_price, sell_price, weight)
        self.equip_class= equip_class
        self.armor = armor
        self.equip_slot = equip_slot

class Alchemy():
    def __init__(heal_amount: int, damage_amount: int, buff_stat: str, buff_amount: int, buff_duration: int):
        """
        Create potion items to provide benefit to the player
        
        :param heal_amount: Description
        :param damage_amount: Description
        :param buff_stat: Description
        :param buff_amount: Description
        :param buff_duration: Description
        """

# ====[ WEAPONS ]====
test_weapon = Weapon(name="test weapon", material='copper', attack=10, buy_price=10, weight=.5, sell_price=10, equip_slot='right hand', equip_class='any')
test_armor = Armor('test armor', 'iron', 100, 100, 5, 10, 'head', 'any')
#====[ ITEM LISTS ]====
item_list = [test_weapon, test_armor]
material_list = []
weapon_list = [test_weapon]
armor_list = [test_armor]
