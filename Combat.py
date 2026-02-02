"""
Module for combat. Player and mob objects should be passed into the functions,
and the result of combat should be returned.
"""

from random import randrange

def damage_calculation(turn, turn_event, entity1, entity2):
    """
    Pass in entities to remove hp from entity1
    """
    max_hit = entity1.attack
    damage_taken = randrange(0, max_hit)
    entity2.hitpoints = entity2.hitpoints - damage_taken
    print(f"[Event: {turn_event}] {entity1.name} did {damage_taken} to {entity2.name}!")

def main_combat_loop(player, enemy):
    x = True
    print("")
    print ("===== FIGHT LOG =====")
    print (f"Enemy: {enemy.name}")
    print("")
    turn_counter = 0
    turn_event = 0
    while x:
        previous_turn_counter = turn_counter
        turn_counter += 1
        print(f"\n[Turn: {turn_counter}]")
        if previous_turn_counter < turn_counter:
            turn_event = 1
        else:
            turn_event += 1
        damage_calculation(turn_counter, turn_event, player,enemy)
        if enemy.hitpoints <= 0:
            print(f"You were victorious over {enemy.name}")
            print(f"The battle lasted {turn_counter} turns")
            break
        turn_event += 1
        damage_calculation(turn_counter, turn_event, enemy, player)
        if player.hitpoints <= 0:
            print("Oh no, you're dead!")
            print(f"The battle lasted {turn_counter} turns.")
            break
        print(f"{player.name} HP: {player.hitpoints}\t{enemy.name} HP: {enemy.hitpoints}")