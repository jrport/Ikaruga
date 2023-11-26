import typing
from typing import Optional, Union
from npc import Npc
from grid import *
import random
from player import Player

# Constantes de file paths, lista de sprites das naves e direções 

PURPLE_SHIP = './assets/purple_ship.png'  
BLUE_SHIP = './assets/blue_ship.png'
PINK_SHIP = './assets/pink_ship.png'

SPRITES: list[str] = [PURPLE_SHIP, BLUE_SHIP, PINK_SHIP] 

DIRECTIONS = ["DOWN","LEFT","RIGHT"]

# Essa classe é responsável por:
# 1) Registrar e progredir a dificuldade da wave;
# 2) Compor e gerar todos os npcs de cada wave utilizando valores randomicamente selecionados 
# de maneira que cada wave possua naves variando em sprites, velocidades de locomoção,
# velocidade de atauqe e que também sejam instanciadas sempre em posições disjuntas.

class wave:
    def __init__(self, cur_num: int) -> None:
        self.cur_wave = cur_num
        self.wave_size: int = 1 + (self.cur_wave * 2)
        self.enemy_count: int = self.wave_size
        self.wave_speeds: list[int] = []
        self.wave_cd: list[int] = []
        self.wave_skins: list[str] = []
        self.base_speed: int = 1
        self.base_cooldown: int = 20
        self.npcs: list[Npc] = []
        self.fast_shooter: bool = True
        self.fast_ship: bool = True
        self.player: Optional[Player] = None

# Esses setters geram/selecionam os atributos das naves buscando garantir diversidade e originalidade 
# entre waves

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

# As funções a seguir produzem listas de todos os parâmetros de iniciliazação das quais 
# todas as naves da onda selecionarão randomicamente  

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

# Une em uma matriz todas as listas de parâmetros para 
# as naves 

    def generate_wave_specs(self) -> typing.Union[list[int],list[str]]:
        wave_speeds: list[int] = self.generate_wave_speed()
        wave_sprites: list[str] = self.generate_wave_sprites()
        wave_directions: list[str] = self.generate_wave_directions()
        wave_cooldowns: list[int] = self.generate_wave_cooldowns()
        wave_specs: typing.Union[list[int],list[str]] = [wave_sprites, wave_directions, wave_speeds, wave_cooldowns]
        return wave_specs

# Gera os índices para seleção aleatória dos atributos das naves 

    def populate_random_indexes(self) -> list[int]:
        indexes: list[int] = []
        for index in range(4):
            indexes.append(random.randint(0,2))
        return indexes

# Integra os setters, matriz de atributos e listas de indexes
# FINALMENTE chamando um construto e compositor das naves 

    def spawn_wave_npcs(self) -> None:
        wave_size = self.wave_size - 1
        indexes: list[int] = self.populate_random_indexes()
        wave_specs: list[list[int]] = self.generate_wave_specs()
        for npc in range(self.wave_size):
            sprite: str = wave_specs[0][random.randint(0,wave_size)]
            direction: str = wave_specs[1][random.randint(0,wave_size)]
            speed: int = wave_specs[2][random.randint(0,wave_size)]
            cooldown: int = wave_specs[3][random.randint(0,wave_size)]
            self.generate_npc(sprite, direction, speed, cooldown)

# Seleciona posições válidas e disjuntas definidas na matriz de coordenadas 
# definidas em grid

    def generate_coords(self) -> tuple[int, int]:
        coords = (POSITION_MATRIX[random.randint(0,2), random.randint(0,11), 0], \
                POSITION_MATRIX[random.randint(0,2), random.randint(0,11), 1]) 
        return coords

# Construtor e compositor dos Npcs 

    def generate_npc(self, file: str, direction: str, speed: int, cooldown: int) -> Npc:
        coords: tuple[int, int] = self.generate_coords()
        npc = Npc(file, speed, direction, cooldown, coords[0], coords[1], self.player)
        self.npcs.append(npc) 
        return npc

# Método utilizado por Game checar se ainda há inimigos vivos na wave 

    def check_enemy_lives(self) -> bool:
        for enemy in self.npcs:
            if enemy.alive == False:
                self.npcs.remove(enemy)
                self.enemy_count = len(self.npcs)
                return True
        return False

# Método para resetar a wave, utilizado caso Game Over

    def clear(self) -> None:
        for enemy in self.npcs:
            enemy.destroy()

# Mais uma parte de nosso esforço para combater o bug, esse é método vai  checar colisões entre as naves 

    def check_npc_collision(self) -> None:
        self.other_npcs = self.npcs
        for npc in self.npcs:
            self.other_npcs.remove(npc)
            for other_npc in self.other_npcs:
                if npc._collides_with(other_npc):
                    npc.reverse_direction()
            self.other_npcs.append(npc)

