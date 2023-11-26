from tupy import BaseGroup, Label

# Essa classe estende BaseGroup gerindo e compondo todos os displays de estatísticas do player na partida.
# Ela também define alguns setters que são atualizados automaticamente com base em gatilhos estabelecidos
# na classe Game

class score_board(BaseGroup):
    def __init__(self) -> None:
        self.score = 0
        self.highest_score = self.score
        self.wave = 0
        self._add(Label("Pontuação: 0", 90, 250, font = "Arial 20", color = "white", anchor = "n"))
        self._add(Label("Onda: 0", 105, 300, font = "Arial 20", color = "white", anchor = "e"))
        self._add(Label("Vidas: 3", 107, 350, font = "Arial 20", color = "white", anchor = "se"))
        self._add(Label("Recorde: 0", 75, 400, font = "Arial 20", color = "white", anchor = "s"))

# Esse método reinicia todos o score_board sempre que Game detecta que o player perdeu

    def reset(self, lives: int) -> None:
        self.score = 0
        self.wave = 0
        self._objects[0].text = "Pontuação: 0"
        self._objects[1].text = "Onda: 0"
        self._objects[2].text = "Vidas: " + str(lives)

# Os métodos a seguir operam como setters dos Labels atualizando sempre que Game detecta alguma alteração relevante

    def update_wave(self, new_wave: int) -> None:
        self._objects[1].text = "Onda: " + str(new_wave)

    def update_lives(self, new_live: int) -> None:
        self._objects[2].text = "Vidas: " + str(new_live)

    def update_score(self, new_score: int) -> None:
        if new_score != self.score:
            self._objects[0].text = "Pontuação: " + str(new_score)
            self.score = new_score
            if new_score > self.highest_score:
                self.update_highest(new_score)
    
    def update_highest(self, new_score: int) -> None:
        self.highest_score = new_score
        self._objects[3].text = "Recorde: " + str(new_score)
