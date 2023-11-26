from tupy import BaseImage
from typing import Optional

BULLET = "./assets/laser.png"

UPPER_BOUND = -10
LEFT_BOUND = 45
RIGHT_BOUND = 630
BOTTOM_BOUND = 540

class Laser(BaseImage):
    def __init__(self, team: str, x: int, y: int):
        self._file = BULLET
        self._x = x
        self._y = y
        self.team = team

    def update(self) -> None:
        self.move(self.team)
        self.check_out_of_bounds()

    def move(self, kind: str) -> None:
        if kind == "ally":
            self._y -= 10
        if kind == "enemy":
            self._y += 10

    def check_out_of_bounds(self) -> None:
        if (self._y <= UPPER_BOUND) or (self._y >= BOTTOM_BOUND): 
            self.destroy()
        
