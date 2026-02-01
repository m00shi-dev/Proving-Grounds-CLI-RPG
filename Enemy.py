"""
The module for enemies in Proving Grounds

Instantiate enemies at the bottom of this file
"""
import time as t
import Items

class Enemy():
    def __init__(self, name, attack, defense, hitpoints, condition, equipment):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hitpoints = hitpoints
        self.condition = condition
        self.equipment = equipment 

# ==== ENEMIES ====
print("Initializing enemies...")
enemy_load_start_time = t.time()
rat = Enemy(name='rat', attack=2, defense =1, hitpoints=5, condition=None, equipment={})
goblin = Enemy(name='goblin', hitpoints=50, attack=3, defense=3, condition=None, equipment={})

# ==== ENEMY LIST ====
enemy_list = [rat, goblin]

enemy_load_end_time = t.time()

elapsed_enemy_load_time = enemy_load_end_time - enemy_load_start_time
formatted_elapsed_enemy_load_time = 'Enemy load time: {:.9f} seconds'.format(elapsed_enemy_load_time)
print(formatted_elapsed_enemy_load_time)

