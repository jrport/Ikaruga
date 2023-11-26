from tupy import Image
from laser import Laser

UPPER_BOUND = 0
LEFT_BOUND = 10
RIGHT_BOUND = 700

PURPLE_SHIP = './assets/purple_ship.png'  
BLUE_SHIP = './assets/blue_ship.png'
PINK_SHIP = './assets/pink_ship.png'

SPRITES: list[str] = [PURPLE_SHIP, BLUE_SHIP, PINK_SHIP] 


class Npc(Image):
    def __init__(self, sprite: str, speed:int, direction: str, cooldown: int, x: int, y: int):
        super().__init__(sprite, x, y)
        self.file = sprite
        self.speed = speed
        self.direction = direction
        self.max_cooldown = cooldown
        self.cur_cooldown = 0
        self.alive = True
        self.count = 0

    def shoot(self):
        if self.cur_cooldown <= 0:
            bullet: Laser = Laser("enemy", self.x, self.y)
            self.cur_cooldown = self.max_cooldown
        return

    def update(self) -> None:
        self.reload()
        self.shoot()
        self.count += 1
        if self.direction == "LEFT":
            self.x += self.speed
        if self.direction == "RIGHT":
            self.x -= self.speed
        if self.direction == "UP":
            self.y -= self.speed
        if self.direction == "DOWN":
            self.y += self.speed
        self.check_out_of_bounds()

    def wait(self) -> None:
        if self.count >= 30:
            return

    def destroy(self) -> None:
        self.alive = False
        self.wait()
        super().destroy()

    def check_out_of_bounds(self) -> None:
        if (self.x <= LEFT_BOUND) or (self.x >= RIGHT_BOUND) or (self.y <= UPPER_BOUND):
            self.destroy()

    def reload(self) -> None:
        if self.cur_cooldown > 0:
            self.cur_cooldown -= 1
            return
        self.cur_cooldown = self.max_cooldown
        return
