from npc import Npc
from grid import *
import random

PURPLE_SHIP = './assets/purple_ship.png'  
BLUE_SHIP = './assets/blue_ship.png'
PINK_SHIP = './assets/pink_ship.png'

SPRITES: list[str] = [PURPLE_SHIP, BLUE_SHIP, PINK_SHIP] 

DIRECTIONS = ["DOWN","LEFT","RIGHT"]

class wave:
    def __init__(self) -> None:
        self.cur_wave = 1
        self.wave_size: int = 4 + (self.cur_wave * 2)
        self.enemy_count: int = self.wave_size
        self.wave_speeds: list[int] = []
        self.wave_cd: list[int] = []
        self.wave_skins: list[str] = []
        self.base_speed: int = 1
        self.base_cooldown: int = 20
        self._npcs: list[Npc] = []
        self.fast_shooter: bool = True
        self.fast_ship: bool = True

    def update(self):
        self.check_enemy_lives()

    @property
    def npc_speed(self) -> int:
        if self.fast_ship:
            speed = self.base_speed + (self.cur_wave // 2)
            self.fast_ship = False
            return speed
        self.fast_ship = True
        return self.base_speed

    @property
    def npc_sprite(self) -> str:
        sprite_index: int = random.randint(0,2)
        sprite: str = SPRITES[sprite_index]
        return sprite

    @property 
    def wave_direction(self) -> str:
        dir_index = random.randint(0,2)
        direction: str = DIRECTIONS[dir_index]
        return direction

    @property
    def wave_cooldowns(self) -> int:
        if self.fast_shooter:
            cooldown: int = self.base_cooldown - (self.cur_wave // 2)
            self.fast_shooter = False
            return cooldown
        self.fast_shooter = True
        cooldown = self.base_cooldown
        return cooldown

    def generate_wave_speed(self) -> list[int]:
        wave_speeds: list[int] = []
        for spaceship in range(self.wave_size):
            wave_speeds.append(self.npc_speed)
        return wave_speeds

    def generate_wave_sprites(self) -> list[str]:
        wave_sprites: list[str] = []
        for spaceship in range(self.wave_size):
            wave_sprites.append(self.npc_sprite)
        return wave_sprites

    def generate_wave_directions(self) -> list[str]:
        wave_directions: list[str] = []
        for spaceship in range(self.wave_size):
            wave_directions.append(self.wave_direction)
        return wave_directions

    def generate_wave_cooldowns(self) -> list[int]:
        wave_cooldowns: list[int] = []
        for spaceship in range(self.wave_size):
            wave_cooldowns.append(self.wave_cooldowns)     
        return wave_cooldowns 

    def generate_wave_specs(self) -> list[list[int]]:
        wave_speeds: list[int] = self.generate_wave_speed()
        wave_sprites: list[str] = self.generate_wave_sprites()
        wave_directions: list[str] = self.generate_wave_directions()
        wave_cooldowns: list[int] = self.generate_wave_cooldowns()
        wave_specs: list[list[int]] = [wave_sprites, wave_directions, wave_speeds, wave_cooldowns]
        return wave_specs

    def populate_random_indexes(self) -> list[int]:
        indexes: list[int] = []
        for index in range(4):
            indexes.append(random.randint(0,2))
        return indexes

    def spawn_wave_npcs(self) -> None:
        wave_size = self.wave_size - 1
        indexes: list[int] = self.populate_random_indexes()
        wave_specs: list[list[int]] = self.generate_wave_specs()
        for npc in range(self.wave_size):
            self._npcs.append(self.generate_npc \
                              (wave_specs[0][random.randint(0,wave_size)], \
                              wave_specs[1][random.randint(0,wave_size)], \
                              wave_specs[2][random.randint(0,wave_size)], \
                              wave_specs[3][random.randint(0,wave_size)]))

    def generate_coords(self) -> tuple[int, int]:
        coords = (POSITION_MATRIX[random.randint(0,2), random.randint(0,11), 0], \
                POSITION_MATRIX[random.randint(0,2), random.randint(0,11), 1]) 
        return coords

    def generate_npc(self, file: str, direction: str, speed: int, cooldown: int) -> Npc:
        coords: tuple[int, int] = self.generate_coords()
        npc = Npc(file, speed, direction, cooldown, coords[0], coords[1])
        self._npcs.append(npc)
        return npc

    def check_enemy_lives(self) -> None:
        for enemy in self._npcs:
            if enemy.alive == False:
                self._npcs.remove(enemy)
                self.enemy_count = len(self._npcs)
