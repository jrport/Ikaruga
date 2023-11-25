from tupy import Image
from laser import Laser

UPPER_BOUND = 50
LEFT_BOUND = 45
RIGHT_BOUND = 630
BOTTOM_BOUND = 455

PURPLE_SHIP = './assets/purple_ship.png'  
BLUE_SHIP = './assets/blue_ship.png'
PINK_SHIP = './assets/pink_ship.png'

SPRITES: list[str] = [PURPLE_SHIP, BLUE_SHIP, PINK_SHIP] 

class Npc(Image):
    
    def __init__(self, sprite: str, speed:int, direction: str, x: int, y: int):
        super().__init__(sprite, x, y)
        self.file = sprite
        self.speed = speed
        self.direction = direction
        self.max_cooldown = 20
        self.cur_cooldown = 0

    def shoot(self):
        bullet = Laser("enemy", self.x, self.y, None, None, None)

    def update(self) -> None:
        if self.direction == "LEFT":
            self.x += self.speed
        if self.direction == "RIGHT":
            self.x -= self.speed
        if self.direction == "UP":
            self.y -= self.speed
        if self.direction == "DOWN":
            self.y += self.speed

