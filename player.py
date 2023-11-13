from typing import Optional
from laser import Laser
from tupy import Image, keyboard

UPPER_BOUND = 50
LEFT_BOUND = 45
RIGHT_BOUND = 630
BOTTOM_BOUND = 455

ORANGE_SHIP = './assets/orange_ship.png'
PURPLE_SHIP = './assets/purple_ship.png'  
BLUE_SHIP = './assets/blue_ship.png'
PINK_SHIP = './assets/pink_ship.png'

class Player(Image):
    def __init__(self) -> None:
        super().__init__(ORANGE_SHIP, 250, 400)
        self.hp = 3
        self.speed = 7
        self.max_laser_cooldown = 10
        self.cur_laser_cooldown = 0
        self.ammo = 1
        self.type: Optional[str] = None

    def update(self) -> None:
        self.reload()
        if keyboard.is_key_down("Down"):
            self.move("DOWN")
        if keyboard.is_key_down("Up"):
            self.move("UP")
        if keyboard.is_key_down("Left"):
            self.move("LEFT")
        if keyboard.is_key_down("Right"):
            self.move("RIGHT")
        if keyboard.is_key_down("space"):
            self.shoot()

    def shoot(self) -> None:
        if self.cur_laser_cooldown == 0:
            self.cur_laser_cooldown = self.max_laser_cooldown
            self.bullet:Laser = Laser("ally",self.x, self.y, None, None, None)
        return

    def move(self, direction: str):
        if direction == "DOWN": 
            if (self.y + self.speed) > BOTTOM_BOUND:
                self.y = BOTTOM_BOUND
                return
            self.y += self.speed
        if direction == "UP":
            if (self.y - self.speed) < UPPER_BOUND:
                self.y = UPPER_BOUND
                return
            self.y -= self.speed
        if direction == "LEFT":
            if (self.x - self.speed) < LEFT_BOUND:
                self.x = LEFT_BOUND
                return
            self.x -= self.speed
        if direction == "RIGHT":
            if (self.x + self.speed) > RIGHT_BOUND:
                self.x = RIGHT_BOUND
                return
            self.x += self.speed
        
    def reload(self) -> None:
        if self.cur_laser_cooldown > 0:
            self.cur_laser_cooldown -= 1


