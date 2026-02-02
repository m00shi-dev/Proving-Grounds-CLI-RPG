import CLI
import Combat
import Player
import Help
import Items
import Enemy
import pytest

@pytest.fixture
def player_object():
    """An instance of the player"""
    player_object = Player.Player("Bryant", 100, 100, 1, 0)
    return player_object

def test_drop_item(player_object):
    """Test that an item has been removed from inventory"""
    player_object.inventory = [Items.Items('iron dagger', 10, 10, 10, 10, 'main_hand', 0, 'iron', 1)]
    for item in player_object.inventory:
        if item.name == 'iron dagger':
            player_object.drop_item(item)
    assert item not in player_object.inventory

def test_parse_user_input():
    """Test that user input is assigned to the dictionary
    properly"""
    user_input = "equip iron dagger"
    parsed_input = CLI.parse_user_input(user_input)
    assert parsed_input == {
        'full_command': 'equip iron dagger',
        'action_command': 'equip',
        'object_name': 'iron dagger'
    }
    
