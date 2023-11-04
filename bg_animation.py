from tupy import Image, BaseGroup 

class Background(Image):
    def __init__(self) -> None:
        super().__init__('./assets/bg_01.jpg', 10, 10)
        self.clock: int = 0

    def update(self) -> None:
        self.bg_clock()
        if (self.clock < 20):
            self.switch_bg(1)
        if (self.clock >= 20):
            self.switch_bg(2)

    def switch_bg(self, which_bg: int) -> None:
        if (which_bg == 1) and (self.file == './assets/bg_02.jpg'):
            self.file = './assets/bg_01.jpg'
            return
        if (which_bg == 2) and (self.file == './assets/bg_01.jpg'):
            self.file = './assets/bg_02.jpg'

    def bg_clock(self) -> None:
        if self.clock < 40:
            self.clock += 1
            return
        if self.clock == 40:
            self.clock = 0


