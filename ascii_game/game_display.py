from PIL import Image
from ascii_art import ASCII_Art
from abc import ABC, abstractmethod
from input_tools import *
class Display(ABC):
    CHARS = list('#@%S?+:*,. ')
    def __init__(self, col_size=50):
        self.image_converter = ASCII_Art(self.CHARS)
        self.image_converter.invert_chars()
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
