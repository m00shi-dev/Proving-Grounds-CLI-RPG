"""Unit tests for the entity class"""
import pytest
from Entity import Entity

@pytest.fixture
def entity_object():
    """Object used for unit testing"""
    entity_object = Entity(hp=100, mana=100, condition=None, entity_class=None)
    return entity_object

def test_add_hp(entity_object):
    """Test adding HP"""
    entity_object.add_hp(10)
    assert entity_object.hp == 110

def test_subtract_hp(entity_object):
    """Test subtracting HP"""
    entity_object.subtract_hp(10)
    assert entity_object.hp == 90

def test_add_mana(entity_object):
    '''Testing adding mana'''
    entity_object.add_mana(10)
    assert entity_object.mana == 110

def test_subtract_mana(entity_object):
    entity_object.subtract_mana(15)
    assert entity_object.mana == 85