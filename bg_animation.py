from tupy import Image, BaseGroup 

# Constantes pra armazenar os file paths

SPACE_FRAME_01 = './assets/bg_01.jpg'
SPACE_FRAME_02 = './assets/bg_02.jpg'

# Essa classe gera a animação do plano de fundo do jogo

class Background(Image):
    def __init__(self) -> None:
        super().__init__(SPACE_FRAME_01, 10, 10)
        self.clock: int = 0

    def update(self) -> None:
        self.bg_clock()
        if (self.clock < 20):
            self.switch_bg(1)
        if (self.clock >= 20):
            self.switch_bg(2)

    # Alterna entre os wallaper com base na chamada update
    def switch_bg(self, which_bg: int) -> None:
        if (which_bg == 1) and (self.file == SPACE_FRAME_02):
            self.file = SPACE_FRAME_01
            return
        if (which_bg == 2) and (self.file == SPACE_FRAME_01):
            self.file = SPACE_FRAME_02

    # Discreciona tempo para alternância entre os wallpapers
    def bg_clock(self) -> None:
        if self.clock < 40:
            self.clock += 1
            return
        if self.clock == 40:
            self.clock = 0


