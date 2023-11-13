from tupy import Image, BaseGroup 

SPACE_FRAME_01 = './assets/bg_01.jpg'
SPACE_FRAME_02 = './assets/bg_02.jpg'

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

    def switch_bg(self, which_bg: int) -> None:
        if (which_bg == 1) and (self.file == SPACE_FRAME_02):
            self.file = SPACE_FRAME_01
            return
        if (which_bg == 2) and (self.file == SPACE_FRAME_01):
            self.file = SPACE_FRAME_02

    def bg_clock(self) -> None:
        if self.clock < 40:
            self.clock += 1
            return
        if self.clock == 40:
            self.clock = 0


