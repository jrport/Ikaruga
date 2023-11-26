from levels import wave
from bg_animation import Background
from player import Player

class game:
    def __init__(self) -> None:
        self._background = Background()
        self.player = Player()
        self.wave = wave()
        self.wave.spawn_wave_npcs()

    #def update(self) -> None:
    #    self.wave.check_enemy_lives()
    #    print(self.wave.enemy_count)

    #def check_enemy_collision(self) -> None:
    #    for npc in wave._npcs:
    #        for player_bullet in player.bullets:
    #            if npc._collides_with(player_bullet):
    #                npc.destroy()
    #                player_bullet.destroy()
    #                print("fui atingido")
    #
    #def check_player_collision(self) -> None:
    #    for enemy_bullet in wave.enemy_bullets:
    #        if player._collides_with(enemy_bullet):
    #            player.take_damage()
    #            enemy_bullet.destroy()
