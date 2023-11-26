from random import randint
from tupy import Image
from laser import enemy_Laser
from typing import Optional
from player import Player

# Constantes de filepath e fronteiras do display

BOTTOM_BOUND = 580
UPPER_BOUND = 0
LEFT_BOUND = 10
RIGHT_BOUND = 700

PURPLE_SHIP = './assets/purple_ship.png'  
BLUE_SHIP = './assets/blue_ship.png'
PINK_SHIP = './assets/pink_ship.png'

SPRITES: list[str] = [PURPLE_SHIP, BLUE_SHIP, PINK_SHIP] 

DIRECTIONS = ["LEFT","RIGHT"]

# Classe que gera e descarta os npcs do jogo

class Npc(Image):
    def __init__(self, sprite: str, speed:int, direction: str, cooldown: int, x: int, y: int, player: Optional[Player]):
        super().__init__(sprite, x, y)
        self.angle = 180
        self.file = sprite
        self.speed = speed
        self.direction = direction
        self.max_cooldown = cooldown
        self.cur_cooldown = 0
        self.alive = True
        self.player = player
        self.crashed = False

    def shoot(self) -> None:
        if self.cur_cooldown <= 0:
            bullet: enemy_Laser = enemy_Laser(self.x, self.y, self.player)
            self.cur_cooldown = self.max_cooldown
        return

# Com base nas direções e valores de velocidade desloca as naves unidirecionalmente
# e também discriciona o cooldown dos disparos

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

# Deleta as naves após saírem dos confins vísiveis do display

    def check_out_of_bounds(self) -> None:
        if (self.x <= LEFT_BOUND) or (self.x >= RIGHT_BOUND) or (self.y >= BOTTOM_BOUND):
            self.alive = False
            self.destroy()

# setter do cooldown do disparo

    def reload(self) -> None:
        if self.cur_cooldown > 0:
            self.cur_cooldown -= 1
            return
        self.cur_cooldown = self.max_cooldown
        return

# Tira as naves da área visível em razão dos sprites não sumirem as vezes mesmo usando _hide() 
# antes de elimina-las

    def displace(self) -> None:
        self.x = 800
        self.y = 800

# Setter de alive especifico para mortes causadas por player para controle de score

    def die(self) -> None:
        self.alive = False
        return super().destroy()

# Tentativa de lidar com um bug em que caso um mesmo disparo colida com duas naves 
# o jogo crasha, para isso o sentido das naves é revertido no primeiro sinal de colisão 
# assim evitando que o bug ocorra muito frequentemente nas waves mais avançadas

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
