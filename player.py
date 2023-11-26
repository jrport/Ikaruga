from laser import Laser, player_Laser
from tupy import Image, keyboard

# Algumas constantes de limites pro Tupy e file paths

UPPER_BOUND = 50
LEFT_BOUND = 30
RIGHT_BOUND = 650
BOTTOM_BOUND = 455

ORANGE_SHIP = './assets/orange_ship.png'
PURPLE_SHIP = './assets/purple_ship.png'  
BLUE_SHIP = './assets/blue_ship.png'
PINK_SHIP = './assets/pink_ship.png'

# Essa classe define os comandos, interações e atributos do jogador
# com seus respectivos setters 

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
        self.damaged = False
        self.wave = None
        self.wave_size: int = 4 + (self.cur_wave * 2)

# Captamos input do player a cada update e controlamos o cooldown dos disparos
 
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

# Verificamos cooldown e gerimos os disparos

    def shoot(self) -> None:
        if self.cur_laser_cooldown == 0:
            self.cur_laser_cooldown = self.max_laser_cooldown
            bullet: Laser = player_Laser(self.x, self.y, \
                    self.wave.npcs, self)

# Limitamos movimento do player as fronteiras do display do tupy

    def move(self, direction: str) -> None:
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
        
# Um setter do cooldown do ataque

    def reload(self) -> None:
        if self.cur_laser_cooldown > 0:
            self.cur_laser_cooldown -= 1

# Um setter do hp do player

    def take_damage(self) -> None: 
        if self.cur_hp > 0:
            self.cur_hp -= 1
        self.damaged = True

# Reinicia os atributos do player em caso de game over detectado por Game 

    def reset(self) -> None:
        self.cur_hp = self.max_hp
        self.score: int = 0
        self.damaged: bool = False
