from tupy import keyboard

class Game:
    def __init__(self) -> None:
        self.pause = 0

    def update(self) -> None:
        if keyboard.is_key_just_down("Escape"):
            self.pause = 0
