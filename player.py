from laser import player_Laser
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
        self.cur_wave = 1
        self.max_hp = 5
        self.cur_hp = self.max_hp
        self.speed = 7
        self.max_laser_cooldown = 10
        self.cur_laser_cooldown = 0
        self.score = 0
        self.wave_kills = 0
        self.wave = None
        self.wave_size: int = 4 + (self.cur_wave * 2)

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
            bullet = player_Laser(self.x, self.y, self.wave.npcs, self)
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

    def take_damage(self) -> None: 
        self.cur_hp -= 1
        
