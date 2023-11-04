from tupy import Image, BaseGroup, keyboard
from random import randint

dificulty: int = 0

class Npc(Image):
    def __init__(self, type: str) -> None:
        self._base_hp: int = 1
        self._base_speed: int = 1
        self.direction: int = rand.randint(1,3)
        self.file: str = './assets/red_ship.jpg'

    @property
    def speed(self):
        return self._base_speed + dificulty

    def update(self) -> None:
       self.movement(self.direction)

    def movement(self, direction: int):
        if direction == 1:
            self.y += self.speed
            return
        if direction == 2:
            self.y -= self.speed
            return
        if direction == 3:
            self.x += self.speed

class Player(Image):
    def __init__(self) -> None:
        self.file = './assets/orange_ship.png'
        self.x = 250
        self.y = 250

    def update(self) -> None:
        if keyboard.is_key_down('Left'):
            self.x -= 20
        if keyboard.is_key_down('Right'):
            self.x += 20
        if keyboard.is_key_down('Up'):
            self.y -= 20
        if keyboard.is_key_down('Down'):
            self.y += 20
