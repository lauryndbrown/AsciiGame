from abc import ABC, abstractmethod
import os
from subprocess import call
from PIL import Image
from game_display.ascii_art import ASCII_Art
from game_display.input_tools import *


class Display(ABC):
    def __init__(self, col_size=50, chars=list('#@%S?+:*,. ')):
        self.image_converter = ASCII_Art(chars)
        self.col_size=col_size
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
