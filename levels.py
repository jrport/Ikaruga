from npc import UPPER_BOUND, Npc
from random import randint
        
fast_shooter: bool = True
fast_ship: bool = True

PURPLE_SHIP = './assets/purple_ship.png'  
BLUE_SHIP = './assets/blue_ship.png'
PINK_SHIP = './assets/pink_ship.png'

SPRITES: list[str] = [PURPLE_SHIP, BLUE_SHIP, PINK_SHIP] 

DIRECTIONS = ["UP","DOWN","LEFT","RIGHT"]

class wave:
    def __init__(self) -> None:
        self.cur_wave = 1
        self.wave_size: int = 4 + (self.cur_wave * 2)
        self.enemy_count: int = self.wave_size
        self.wave_speeds: list[int] = []
        self.wave_cd: list[int] = []
        self.wave_skins: list[str] = []
        self.base_speed: int = 3
        self._npcs: list[Npc] = []

    @property
    def npc_speed(self) -> int:
        if fast_ship:
            speed = self.base_speed + (self.cur_wave // 2)
            fast_ship = False
            return speed
        fast_ship = True
        return self.base_speed

    @property
    def npc_sprite(self) -> str:
        index: int = random.randint(0,2)
        sprite: str = SPRITES[index]
        return sprite

    @property 
    def wave_direction(self) -> str:
        index: int = random.randint(0,3)
        direction: str = DIRECTIONS(index) 
        return direction

    @property
    def wave_cooldowns(self) -> int:
        if fast_shooter:
            cooldown: int = self.base_speed + (self.cur_wave // 2)
            fast_shooter = False
            return cooldown
        fast_shooter = True
        cooldown = self.base_speed
        return cooldown

    def generate_wave_speed(self) -> list[int]:
        wave_speeds: list[int] = []
        for spaceship in range(self.wave_size):
            wave_speeds.append(self.npc_speed)
        return wave_speeds

    def generate_wave_sprites(self) -> list[str]:
        wave_sprites: list[str] = []
        for spaceship in range(self.wave_size):
            wave_speeds.append(self.npc_sprite)
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

    def generate_wave_specs(self) -> None:
        wave_speeds: list[int] = self.generate_wave_speed()
        wave_sprites: list[str] = self.generate_wave_sprites()
        wave_directions: list[str] = self.generate_wave_directions()
        wave_cooldowns: list[int] = self.generate_wave_cooldowns()

    def populate_indexes(self) -> list[int]:
        indexes: list[int] = []
        for index in range(3):
            indexes.append(random.randint(0,2)
        return indexes

    def spawn_wave_npcs(self) -> None:
        indexes: list[int] = self.populate_indexes()
        for npc in range(self.wave_size):
            self._npcs.append(self.generate_npc, indexes[0], indexes[1], indexes[2])

    def generate_npc(self, file, direction, speed) -> Npc:
        npc = Npc(file, speed, direction)
        return npc
