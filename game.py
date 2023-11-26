from levels import wave
from bg_animation import Background
from player import Player
from score_board import score_board
from tupy import BaseGroup, BaseImage

# Sim, isso é feio, sim, poderia ser melhor implementado se eu tivesse me planejado melhor
# por isso desculpa por fazer essa barbaridade. 

# A priori, game seria uma extensão de basegroup só que sofri com dificuldades de conciliar
# o uso de update como uma função no arquivo main.py e/ou game.py, entã́o recorri a transformar 
# esse mega compositor é essa classe, em uma Base Image escondida num canto da tela (clícavel, 
# mas oculto para facilitar no debugging).

# Enfim, essa classe vai compor todas as demais estabelecidas nos demais arquivos, com exceção de grid
# coordenando interações entre as várias classes e controlando a prograssão do player em um nível mais 
# elevado que a classe wave.

class game(BaseImage):
    def __init__(self) -> None:
        self.file =""
        self._x = 200
        self._y = 200
        self._background = Background()
        self.cur_wave = 0
        self.wave: wave = wave(1)
        self.player: Player = Player()
        self.wave.player = self.player
        self.player.wave = self.wave
        self.wave.spawn_wave_npcs()
        self.score_board: score_board = score_board()
    
# Este update vai checar colisões relevantes e atualizar o placar no score_board 

    def update(self) -> None:
        if self.wave.check_enemy_lives():
           self.score_board.update_score(self.player.score)
        self.check_enemy_count()
        self.check_player_hp()
        self.wave.check_npc_collision()
    
# Uma série de métodos que são constantemente executados que checam interações relevantes para engatilhar 
# em sua maioria, setters, repassando alguns parametros acessíveis só nesse nível graças a composição

    def check_enemy_count(self) -> None:
        if self.wave.enemy_count <= 0:
            self.next_wave()

    def check_player_hp(self) -> None:
        if self.player.damaged:
            self.player.damaged = False
            self.score_board.update_lives(self.player.cur_hp)
        if self.player.cur_hp <= 0:
            self.game_over()

# Reinicia player e destroi wave em caso de game_over 

    def game_over(self) -> None:
        self.player.reset()
        self.wave.clear()
        self.set_game()

# Reinstancia a wave e atualiza os placares

    def set_game(self) -> None:
        self.cur_wave = 0
        self.wave = wave(1)
        self.wave.player = self.player
        self.player.wave = self.wave
        self.wave.spawn_wave_npcs()
        self.score_board.reset(self.player.max_hp)

# Modifica atributos da wave para progressão

    def next_wave(self) -> None:
        self.cur_wave += 1
        self.score_board.update_wave(self.cur_wave)
        self.wave = wave(self.cur_wave)
        self.player.cur_hp = self.player.max_hp
        self.score_board.update_lives(self.player.cur_hp)
        self.player.wave = self.wave
        self.wave.player = self.player
        self.wave.spawn_wave_npcs()
        
