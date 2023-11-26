from levels import wave
from bg_animation import Background
from player import Player
from score_board import score_board
from tupy import BaseGroup, BaseImage
# Yes, this is really bad, i shouldn't have turned this into an tupy object
# However, mostly due to poor planning, I really struggled properly utilizing
# Both functional and method-based implementations of update(), so i had to resort
# to turning this into am image, I apologize.
class game(BaseImage):
    def __init__(self) -> None:
        self.file =""
        self.clock = 0
        self._x = 200
        self._y = 200
        self._background = Background()
        self.cur_wave = 0
        self.wave = wave(1)
        self.player = Player()
        self.wave.player = self.player
        self.player.wave = self.wave
        self.wave.spawn_wave_npcs()
        self.score_board: BaseGroup = score_board()
    
    def update(self) -> None:
        self.timer()
        if self.wave.check_enemy_lives():
           self.score_board.update_score(self.player.score)
        self.check_enemy_count()
        self.check_player_hp()
        self.wave.check_npc_collision()
    
    def timer(self) -> None:
        self.clock += 1
        if self.clock >= 80:
            self.clock = 0
            return 

    def check_enemy_count(self) -> None:
        if self.wave.enemy_count <= 0:
            print("proxima wave")
            self.next_wave()

    def check_player_hp(self) -> None:
        if self.player.damaged:
            self.player.damaged = False
            self.score_board.update_lives(self.player.cur_hp)
        if self.player.cur_hp <= 0:
            self.game_over()

    def game_over(self) -> None:
        self.player.reset()
        self.wave.clear()
        self.set_game()

    def set_game(self) -> None:
        self.cur_wave = 0
        self.wave = wave(1)
        self.wave.player = self.player
        self.player.wave = self.wave
        self.wave.spawn_wave_npcs()
        self.score_board.reset(self.player.max_hp)

    def wait(self) -> None:
        while True:
            if self.clock > 60:
                break
            self.update()

    def next_wave(self) -> None:
        self.cur_wave += 1
        self.score_board.update_wave(self.cur_wave)
        self.wave = wave(self.cur_wave)
        self.player.cur_hp = self.player.max_hp
        self.score_board.update_lives(self.player.cur_hp)
        self.player.wave = self.wave
        self.wave.player = self.player
        self.wait()
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
