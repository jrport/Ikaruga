from tupy import Image, BaseGroup, keyboard
from random import randint
from main import *

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
        if game.pause == 0:
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
        self.x: int = 250
        self.y: int= 250
        self._base_speed: int = 5
        

    @property
    def speed(self): 
        return self._base_speed

    def hide(self) -> None:
        return super()._hide()

    def update(self) -> None:
        print(self.x,self.y)
        if session.pause is False:
            if keyboard.is_key_down('Left'):
                self.x -= self.speed
            if keyboard.is_key_down('Right'):
                self.x += self.speed
            if keyboard.is_key_down('Up'):
                self.y -= self.speed
            if keyboard.is_key_down('Down'):
                self.y += self.speed


