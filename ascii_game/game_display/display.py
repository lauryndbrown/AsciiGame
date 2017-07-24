from abc import ABC, abstractmethod
import os
from subprocess import call
from PIL import Image
from ascii_game.game_display.ascii_art import ASCII_Art
from ascii_game.game_display.input_tools import *


class Display(ABC):
    #Commonly Used characters for Horizontal Rule
    HR_BOLD = "="
    HR_DASHED = '-'
    HR_LIGHT = '_'
    def __init__(self, col_size=50, chars=list('#@%S?+:*,. ')):
        self.image_converter = ASCII_Art(chars)
        self.col_size=col_size
        self.last_screen_method = None
    @abstractmethod
    def game_screen(self, game, player_1, player_2):
        pass
    def start_menu(self):
        """
        Prints out the Start Menu Screen to to player
        """
        new_game = yes_or_no("Do you want to play a New Game?[Y/N] ")
        if new_game:
            print("New Game")
        else:
            print("Last Saved Game")
        return new_game
    
    def image_to_ascii(self, path):
        """
        """
        try:
            image = Image.open(path)
        except:
            print("Could not find image at "+path)
            exit(1)
        ascii_image = self.image_converter.image_to_ascii(image)
        print(ascii_image)
    def center(self, message, border, size=os.get_terminal_size().columns):
        """
        Returns a string with message centered between characters of a given border
        """
        return message.center(size, border)
    
    def format_HR(self, border, size=os.get_terminal_size().columns-1):
        """
        Returns a Horizontal Rule of length size
        """
        return border*size
    def clear_screen(self):
        """
        Clears the Screen
        """
        print()
        call(["clear"])
    def _in_game_menu(self, choices):
        """
        Private method to display the in-game menu choices
        """
        menu_str = ""
        for index in range(len(choices)):
            choice_str = "{}[{}]".format(choices[index].name,index)
            menu_str+="{}     ".format(choice_str)
        print(self.center("Menu", self.HR_DASHED))
        print(self.center(menu_str, ' '))

          
    def fill_screen(self, offset):
        """
        Fills remaining lines of screen with Whitespace
        """
        lines = os.get_terminal_size().lines - 1
        if offset < lines:
            print('\n'*(lines-offset))
    def actions_menu(self, menu, message="Enter next action: "):
        return enter_next_action(message, menu, self)
    def reset(self):
        """
        Re-prints the current screen 
        """
        self.last_menu[0](*tuple(self.last_menu[1]))
    def get_terminal_col(self):
        return os.get_terminal_size().columns
    def get_terminal_lines(self):
        return os.get_terminal_size().lines
