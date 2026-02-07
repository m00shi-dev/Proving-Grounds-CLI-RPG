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
    def __init__(self, name, material: str, buy_price: int, sell_price: int, weight: float, attack: int):
        super().__init__(name, material, buy_price, sell_price, weight)
        self.attack = attack

class Armor(Item):
    def __init__(self, name:str, material: str, buy_price: int, sell_price: int, weight: float, armor: int):
        super().__init__(name, material, buy_price, sell_price, weight)

# ====[ WEAPONS ]====
test_weapon = Weapon('test weapon', 'copper', 3, 3, .5, 7)

#====[ ITEM LISTS ]====
item_list = [test_weapon]
material_list = []
weapon_list = [test_weapon]
armor_list = []
