from levels import wave
from bg_animation import Background
from player import Player
from tupy import BaseGroup, BaseImage

# Yes, this is really bad, i shouldn't have turned this into an tupy object
# However, mostly due to poor planning, I really struggled properly utilizing
# Both functional and method-based implementations of update(), so i had to resort
# to turning this into am image, I apologize.
class game(BaseImage):
    def __init__(self) -> None:
        self.file =""
        self._x = 200
        self._y = 200
        self._background = Background()
        self.cur_wave = 1
        self.wave = wave(1)
        self.player = Player()
        self.wave.player = self.player
        self.player.wave = self.wave
        self.wave.spawn_wave_npcs()
    
    def update(self) -> None:
        self.wave.check_enemy_lives()
        self.check_enemy_count()

    def check_enemy_count(self) -> None:
        if self.wave.enemy_count <= 0:
            print("proxima wave")
            self.next_wave()

    def reset(self) -> None:
        pass

    def next_wave(self) -> None:
        self.cur_wave += 1
        self.wave = wave(self.cur_wave)
        self.wave.player = self.player
        self.wave.spawn_wave_npcs()

    #def check_enemy_collision(self) -> None:
    #    for npc in self.wave._npcs:
    #        for player_bullet in self.player.bullets:
    #            if npc.collides_with(player_bullet):
    #                npc.destroy()
    #                player_bullet.destroy()
    #                print("fui atingido")
    #
    #def check_player_collision(self) -> None:
    #    for enemy_bullet in self.enemy_bullets:
    #        if self.player._collides_with(enemy_bullet):
    #            self.player.take_damage()
    #            self.enemy_bullet.destroy()
