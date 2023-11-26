from random import randint
from tupy import Image
from laser import enemy_Laser
from typing import Optional
from player import Player

BOTTOM_BOUND = 580
UPPER_BOUND = 0
LEFT_BOUND = 10
RIGHT_BOUND = 700

PURPLE_SHIP = './assets/purple_ship.png'  
BLUE_SHIP = './assets/blue_ship.png'
PINK_SHIP = './assets/pink_ship.png'

SPRITES: list[str] = [PURPLE_SHIP, BLUE_SHIP, PINK_SHIP] 

DIRECTIONS = ["LEFT","RIGHT"]

class Npc(Image):
    def __init__(self, sprite: str, speed:int, direction: str, cooldown: int, x: int, y: int, player: Optional[Player]):
        super().__init__(sprite, x, y)
        self.file = sprite
        self.speed = speed
        self.direction = direction
        self.max_cooldown = cooldown
        self.cur_cooldown = 0
        self.alive = True
        self.player = player
        self.crashed = False

    def shoot(self):
        if self.cur_cooldown <= 0:
            bullet: enemy_Laser = enemy_Laser(self.x, self.y, self.player)
            self.cur_cooldown = self.max_cooldown
        return

    def update(self) -> None:
        self.reload()
        self.shoot()
        if self.direction == "LEFT":
            self.x += self.speed
        if self.direction == "RIGHT":
            self.x -= self.speed
        if self.direction == "UP":
            self.y -= self.speed
        if self.direction == "DOWN":
            self.y += self.speed
        self.check_out_of_bounds()

    def check_out_of_bounds(self) -> None:
        if (self.x <= LEFT_BOUND) or (self.x >= RIGHT_BOUND) or (self.y >= BOTTOM_BOUND):
            self.alive = False
            self.destroy()

    def reload(self) -> None:
        if self.cur_cooldown > 0:
            self.cur_cooldown -= 1
            return
        self.cur_cooldown = self.max_cooldown
        return

    def displace(self) -> None:
        self.x = 800
        self.y = 800

    def die(self) -> None:
        self.alive = False
        return super().destroy()

    def reverse_direction(self) -> None:
        if self.crashed is False:
            if self.direction == "LEFT":
                self.direction = "RIGHT"
                return
            if self.direction == "RIGHT":
                self.direction = "LEFT"
                return 
            if self.direction == "DOWN":
                self.direction = DIRECTIONS[randint(0,1)]
