from typing import Any
from tupy import BaseImage
from abc import ABC

BULLET = "./assets/laser.png"

UPPER_BOUND = -10
LEFT_BOUND = 45
RIGHT_BOUND = 630
BOTTOM_BOUND = 540

class Laser(ABC, BaseImage):
    def __init__(self, x: int, y: int):
        self._file = BULLET
        self._x = x
        self._y = y

    def update(self) -> None:
        self.check_out_of_bounds()

    def check_out_of_bounds(self) -> None:
        if (self._y <= UPPER_BOUND) or (self._y >= BOTTOM_BOUND): 
            self.destroy()

class enemy_Laser(Laser):
    def __init__(self, x: int, y: int, player):
        super().__init__(x, y)
        self.player = player
    
    def update(self) -> None:
        super().update()
        self._y += 10
        self.check_collision_with_player()

    def check_collision_with_player(self) -> None:
        if self._collides_with(self.player):
            self.player.take_damage()
            self.destroy()

class player_Laser(Laser):
    def __init__(self, x: int, y: int, enemy_list: list[Any], sender: Any):
        super().__init__(x, y)
        self.enemy_list = enemy_list
        self.sender = sender  
    def update(self) -> None:
        super().update()
        self._y -= 10
        self.check_collision_with_enemies()

    def check_collision_with_enemies(self) -> None:
        for enemy in self.enemy_list:
            if self._collides_with(enemy):
                self.destroy()
                enemy.displace()
                enemy.die()
                self.sender.score += 1
