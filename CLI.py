from rich.panel import Panel 
from rich.table import Table 
from rich.console import Console
from typing import List, Callable, Any, Tuple
import Items
import Entity

Player: Entity = Callable[..., Any]

"""Handles printing messages and player input"""
command_history: List[str] = []
#====[ EMOJI CODES ]====
warrior: str = ":man_firefighter_light_skin_tone:"
rogue: str = ":man_gesturing_no:"
mage: str = ":mage:"
traveler:str = ":man_elf_light_skin_tone:"


class CLI(Console):

    # Create console instance for rich
    console = Console()

    #====[ MENU STATE ]====
    # Used to determine where the user is in the menu
    # This will then be used to edit the prompt
    menu_state: str = "main menu"

    def print_welcome_screen() -> None:
        welcome_message = f":skull: [white on dark_red] Welcome to the proving grounds [/] :knife:"
        CLI.console.print(Panel(welcome_message, expand=False), style="dark_red")

    def convert_input_to_int(input: str) -> int | bool:
        """Convert input to integer. Used to determine a menu selection
        returns: False if can't convert"""
        try:
           converted_input = int(input)
        except ValueError:
            return False 
        return converted_input

    def character_class_selection() -> str:
        """Only serves to handle character class selection from __main__
        returns: string of class character wants to play. 
        """
        class_selection_message = "What [yellow]class[/yellow] would you like to play?\n"
        class_selection_message += f"1. Warrior{warrior}\n"
        class_selection_message += f"2. Rogue{rogue}\n"
        class_selection_message += f"3. Mage{mage}\n"
        class_selection_message += f"4. Traveler{traveler}"
        CLI.console.print(Panel(class_selection_message, expand=False, border_style="chartreuse3"))
        CLI.menu_state = "class_selection"
         
        while True:
            selection = CLI.convert_input_to_int(CLI.pretty_prompt())
            while selection == False:
                print(Panel("That is not a class. Please try again.", expand=False, style="chartreuse3"))
                selection = CLI.convert_input_to_int(CLI.pretty_prompt())
            else:
                if selection == 1:
                    class_selected = "warrior"
                elif selection == 2:
                    class_selected = "Rogue"
                elif selection == 3:
                    class_selected = "Mage"
                elif selection == 4:
                    class_selected = "Traveler"
                CLI.console.print(Panel(f"[white]Excellent choice playing as a {class_selected}[/]", expand=False, style="chartreuse3"))
                break 
            
        if selection == 1:
            return "warrior"
        if selection == 2:
            return "rogue"
        if selection == 3:
            return "mage"
        if selection == 4:
            return "traveler"
        
    def convert_input_to_dict(player_input: str) -> dict:
        """Segment the players input to be parsed."""
        player_input = player_input.strip()
        dict_player_input: dict = {}
        list_player_input: List[str] = []
        list_player_input = player_input.split(" ")
        dict_player_input['core_command'] = list_player_input.pop(0)
        secondary_command = " ".join(list_player_input)
        for item in Items.item_list:
            if item.name == secondary_command:
                dict_player_input['secondary_command'] = item
                break
            else:
                dict_player_input['secondary_command'] = secondary_command
        return dict_player_input

    def pretty_prompt() -> Callable:
        """Format a prompt using rich
        This should be fed to CLI.console.input"""
        if CLI.menu_state == "class_selection":
            new_prompt = "[[green]Class Selection[/green]]>> " 
            return CLI.console.input(new_prompt)
        elif CLI.menu_state == "inventory":
            new_prompt = "[[yellow] INVENTORY [/yellow]]>> "
            return CLI.console.input(new_prompt)
        elif CLI.menu_state == "stats":
            new_prompt = "[[blue] STATS [/blue]]>> "
            return CLI.console.input(new_prompt)
        elif CLI.menu_state == 'main menu':
            new_prompt = "[[cyan] MAIN MENU [/cyan]]>> "
            return CLI.console.input(new_prompt)
        elif CLI.menu_state == 'help':
            new_prompt = "[[pale_violet_red1] HELP [/]]>> "
            return CLI.console.input(new_prompt)
        elif CLI.menu_state == "travel":
            new_prompt = "[[royal_blue1] TRAVEL [/]]>> "
        else:
            new_prompt = "[[red][blink] GAME [/red][/blink]]>> "
            return CLI.console.input(new_prompt)
    
    def print_player_stats(player) -> str:
        """Print the player stats"""
        current_weight = player.calculate_carry_weight()
        table = Table(title="Stats")
        table.add_column("Stat")
        table.add_column("Value")
        table.add_row('Attack', str(player.stats.attack))
        table.add_row('Strength', str(player.stats.strength))
        table.add_row('Defense', str(player.stats.defense))
        table.add_row('Agility', str(player.stats.agility))
        table.add_row('Intelligence', str(player.stats.intelligence))
        table.add_section()
        table.add_row("Weight", f"{current_weight} / {player.max_carry_weight}")
        table.add_row("Gold", str(player.gold))
        CLI.console.print(table)

    def print_equipped_items(player: Player) -> None:
        """Iterate through the player's worn equipment
        and print the items in a table."""
        table = Table(title="[light_slate_blue]Equipment")
        table.add_column("Slot")
        table.add_column("Name")
        table.add_column("Attack")
        table.add_column("Armor")
        for slot, nested_dict in player.equipment.items():
            for key, value in nested_dict.items():
                if value == None:
                    table.add_row(slot.capitalize(), "-", "-", "-")
                elif slot != 'right hand' and slot != 'left hand':
                    if key == 'item':
                        table.add_row(slot.capitalize(), value.name, "-", str(value.armor))
                else:
                    if key == 'item':
                        table.add_row(slot.capitalize(), value.name, str(value.attack), "-")
        CLI.console.print(table)

    def print_help() -> None:
        """Read menu state, and print the help
        screen for that menu
        """
        table = Table(title=f"{CLI.menu_state.upper()} Help")
        if CLI.menu_state == "help":
            table.add_column("Command")
            table.add_column("Description")
            table.add_row("Help", "Prints this menu")
            CLI.console.print(table)
        elif CLI.menu_state == "main menu":
            table.add_column("Command (Shortcut)")
            table.add_column("Description")
            table.add_row("(s) - Stats", "Print character stats")
            table.add_row("(i) - Inventory", "Enter inventory submenu")
            table.add_row("(h) - Help", "Print this help menu")
            CLI.console.print(table)
        elif CLI.menu_state == "stats":
            table.add_column("Command")
            table.add_column("Description")
            table.add_row("(g) - Gear", "Print buffs from gear")
            CLI.console.print(table)
        elif CLI.menu_state == "inventory":
            table.add_column("Command")
            table.add_column("Description")
            table.add_row("(e) - Equip", "Equip an item. Usage: [bold]equip[/bold] [italic] item name[/italic]")
            table.add_row("(g) - Gear", "View currently equipped items")
            table.add_row("(i) - Inventory", "View inventory items")
            CLI.console.print(table)
        else:
            # print help was called for a menu that doesn't exist
            table.add_column("Command")
            table.add_column("Description")
            table.add_row("Whoops", "[blink]A help menu doesn't exist for this menu![/blink]")
            CLI.console.print(table)

    def drop_item_check(item: Items) -> Tuple[bool, Items]:
        if item in Items.item_list:
            confirmation_message = f"Are you sure you want to drop [turqoise2]{item.name}?\n"
            confirmation_message += f"[white on red] THIS ACTION CANNOT BE UNDONE![/]"
            CLI.console.print(Panel(confirmation_message, expand=False), end="")
            answer = CLI.console.input(f"Please enter [green]yes[/] or [orange3]no[/] >>")
            answer = answer.lower()
            if answer == "y" or answer == "yes":
                return (True, item)
        else:
            CLI.console.print(Panel(f"[orange3]{item}[/] not found.", expand=False, border_style="red"))
            return (False, item)

    def print_inventory(player) -> None:
        """Print inventory table"""
        table = Table(title="Inventory")
        table.add_column("Name")
        table.add_column("Material")
        table.add_column("Attaack")
        table.add_column("Armor")
        table.add_column("Sell Price")
        table.add_column("Buy Price")
        for item in player.inventory:
            try:
                if item.armor:
                    table.add_row(item.name, item.material, "-", str(item.armor), str(item.sell_price), str(item.buy_price))
            except AttributeError:
                pass
            try:
                if item.attack:
                    table.add_row(item.name, item.material, str(item.attack), "-", str(item.sell_price), str(item.buy_price))
            except AttributeError:
                pass
        CLI.console.print(table)
    
    def view_item(item) -> None:
        """Print item attributes to console"""
        table = Table(title=item.name)
        table.add_column("Attribute")
        table.add_column("Value")
        try:
            if item.armor:
                for attribute, value in vars(item).items():
                    table.add_row(str(attribute), str(value))
        except ValueError:
            pass
        except AttributeError:
            pass
        try:
            if item.attack:
                for attribute, value in vars(item).items():
                    table.add_row(str(attribute), str(value))
        except AttributeError:
            pass
        CLI.console.print(table)