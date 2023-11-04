from bg_animation import *
from tupy import keyboard
from menu import InitialMenu
from spaceships import *

initial_pause: bool = True
pause: bool = False

class game:
    def __init__(self) -> None:
        self.bg = Background()
        self.initial_menu = InitialMenu()
        self.player = Player()
        self.player._hide()

    def update(self) -> None:
        pass

    def unpause_initial(self) -> None:
        self.initial_menu._hide()
        self.initial_pause = False
        self.player.hide()
