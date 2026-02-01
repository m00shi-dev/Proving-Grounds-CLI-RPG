"""
Module for combat. Player and mob objects should be passed into the functions,
and the result of combat should be returned.
"""

from random import randrange

def damage_calculation(entity1, entity2):
    """
    Pass in entities to remove hp from entity1
    """
    max_hit = entity1.attack
    damage_taken = randrange(0, max_hit)
    entity2.hitpoints = entity2.hitpoints - damage_taken
    print(f"{entity1.name} did {damage_taken} to {entity2.name}!")

def main_combat_loop(player, enemy):
    x = True
    turn_counter = 0
    while x:
        turn_counter += 1
        damage_calculation(player,enemy)
        if enemy.hitpoints <= 0:
            print(f"You were victorious over {enemy.name}")
            print(f"The battle lasted {turn_counter} turns")
            break
        damage_calculation(enemy,player)
        if player.hitpoints <= 0:
            print("Oh no, you're dead!")
            print(f"The battle lasted {turn_counter} turns.")
            break