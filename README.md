# AsciiGame
Ascii Game Framework for Terminal-based Games

![Language:Python3](https://img.shields.io/badge/Language-Python3-green.svg)
![License:GNU GENERAL PUBLIC LICENSE](https://img.shields.io/badge/License-GNU-orange.svg)
## Bulit with AsciiGame
- ![Monster AsciiGame](https://github.com/lauryndbrown/Monster_ASCII_Game)
- ![AsciiGame TicTacToe](https://github.com/lauryndbrown/ASCII_Tic_Tac_Toe)
## Features
* Game Menu System
* Image to ASCII Art Converter
* Common Game Display Tools
* User Input Tools
* Save Games (Comming Soon)

## Usage
### Philosophy
Keep Game Menu Logic, Game Play Entities, and Display Separate.  
### Create a Menu
Extend the Game Class in game.py.
```python
class YourGame(Game):
```
Create a class-level variable. Typically named GAME_MENU_NAME.
```python
 class YourGame(Game):
  #Menu Names
  START_MENU_NAME = "Start"
  GAME_MENU_NAME = "Game"
  SETTINGS_MENU_NAME = "Settings"
```
In the ```__init__()``` method create a list of Choice objects (found in game.py). This represents the different options that will be shown to the user on that game menu screen.
- Choice("Label Shown to User", functionToBeCalledWhenChosen,(anyInputForFunction,), self.YOUR_GAME_MENU )
```python
  def __init__(self, display, player_1, player_2):
    start_menu = []
    game_menu = []
    settings_menu = []
    start_menu.append(Choice("Start Game", self.display.game_screen, (self,), self.GAME_MENU_NAME))
    start_menu.append((Choice("Settings",self.display.settings_screen, (self,), self.SETTINGS_MENU_NAME))
    start_menu.append(Choice("Exit TicTacToe",self.end_game, None, None))
    settings_menu.append(Choice(self.BACK_OPTION,self.display.start_menu, (self,), self.START_MENU_NAME))
    game_menu.append(Choice(self.BACK_OPTION,self.display.start_menu, (self,), self.START_MENU_NAME))
```
Store those lists in an instance variable named self.menus. This variable needs to be a dictionary paring your list of choices and your GAME_MENU_NAME together. 
```python
  def __init__(self, display, player_1, player_2):
    [...]
    self.menus = {self.START_MENU_NAME:start_menu, self.GAME_MENU_NAME:game_menu, self.SETTINGS_MENU_NAME:settings_menu}
```
Set your current menu with self.menu. This will represent the first menu to display.
```python
  def __init__(self, display, player_1, player_2):
    [...]
    self.menu = start_menu
```


## Files
* **game.py** - The abstract Game Class that contains logic for the menus in the game. 
* **player.py** - The generic player class. 
* **game_display/ascii_art.py** - Image to ASCII Art Converter.
* **game_display/display.py** - Contains the Abstract base class for the game display with serveral common tools to be used in the display.
* **game_display/input_tools.py** - Contains several methods used to obtain user input.

Note that these files inherit additional functionality from the ASCII Game Framework.
