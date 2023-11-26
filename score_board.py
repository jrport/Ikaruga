from tupy import BaseGroup, Label

class score_board(BaseGroup):
    def __init__(self) -> None:
        self.score = 0
        self.highest_score = self.score
        self.wave = 0
        self._add(Label("Pontuação: 0", 90, 250, font = "Arial 20", color = "white", anchor = "n"))
        self._add(Label("Onda: 0", 105, 300, font = "Arial 20", color = "white", anchor = "e"))
        self._add(Label("Vidas: 3", 107, 350, font = "Arial 20", color = "white", anchor = "se"))
        self._add(Label("Recorde: 0", 75, 400, font = "Arial 20", color = "white", anchor = "s"))
        self.timer = 0

    def update_score(self, new_score: int) -> None:
        if new_score != self.score:
            self._objects[0].text = "Pontuação: " + str(new_score)
            self.score = new_score
            if new_score > self.highest_score:
                self.update_highest(new_score)

    def clock(self) -> None:
        self.timer += 1

    def update_wave(self, new_wave: int) -> None:
        self._objects[1].text = "Onda: " + str(new_wave)

    def wait(self) -> bool:
        if self.timer >= 50:
            return True
        return False

    def update_lives(self, new_live: int) -> None:
        self._objects[2].text = "Vidas: " + str(new_live)

    def reset(self, lives) -> None:
        self._objects[0].text = "Pontuação: 0"
        self._objects[1].text = "Onda: 0"
        self._objects[2].text = "Vidas: " + str(lives)
    
    def update_highest(self, new_score: int) -> None:
        self.highest_score = new_score
        self._objects[3].text = "Recorde: " + str(new_score)
