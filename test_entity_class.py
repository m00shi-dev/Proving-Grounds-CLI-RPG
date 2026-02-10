"""Unit tests for the entity class"""
import pytest
from Entity import Entity, Player

@pytest.fixture
def entity_object():
    """Object used for unit testing"""
    mage = Player(name="MageMan69420", entity_class='mage')
    warrior = Player(name='WarriorBoi', entity_class='warrior')
    rogue = Player(name='SneakyPants', entity_class="rogue")
    traveler = Player(name='Jack', entity_class='traveler') 
    player_list = [warrior, mage, rogue, traveler]
    return player_list

def test_add_hp(entity_object):
    """Test adding HP"""
    for entity in entity_object:
       entity.add_hp(10)
    assert entity_object[0].hp == 120
    assert entity_object[1].hp == 100
    assert entity_object[2].hp == 100
    assert entity_object[3].hp == 110

def test_subtract_hp(entity_object):
    """Test subtracting HP"""
    for entity in entity_object:
        entity.subtract_hp(10)
    assert entity_object[0].hp == 100 
    assert entity_object[1].hp == 80 
    assert entity_object[2].hp == 80 
    assert entity_object[3].hp == 90 

def test_add_mana(entity_object):
    """Testing adding mana"""
    for entity in entity_object:
        entity.add_mana(10)
    assert entity_object[0].mana == 25 
    assert entity_object[1].mana == 60 
    assert entity_object[2].mana == 25 
    assert entity_object[3].mana == 40 

def test_subtract_mana(entity_object):
    for entity in entity_object:
        entity.subtract_mana(7)
    assert entity_object[0].mana == 8
    assert entity_object[1].mana == 43
    assert entity_object[2].mana == 8 
    assert entity_object[3].mana == 23 