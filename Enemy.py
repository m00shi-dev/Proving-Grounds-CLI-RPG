"""
The module for enemies in Proving Grounds
"""

class Enemy():
    def __init__(self, name, attack, defense, hitpoints, condition, equipment):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hitpoints = hitpoints
        self.condition = condition
        self.equipment = equipment

