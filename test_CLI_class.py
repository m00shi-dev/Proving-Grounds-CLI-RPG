from CLI import CLI

def test_input_dictionary():
    """Test that the input in being placed in the 
    proper locations in the input dictionary for parsing"""

    input = "equip test weapon"
    response = CLI.convert_input_to_dict(input)
    assert response == {'core_command': 'equip', 'secondary_command': 'test weapon' } 
    