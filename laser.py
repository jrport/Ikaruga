from tupy import Rectangle
from typing import Optional

class Laser(Rectangle):
    def __init__(self, team: str, x: int, y: int, bonus: int, kind: str, wave: Optional[int]):
        super().__init__(x, y, 5, 10, outline = 'orange', fill = 'orange')
        self.damage_bonus = bonus
        self.kind = kind 
        self.team = team
        self.wave = wave

    def update(self) -> None:
        if self.team == "ally":
            self.move(self.kind)
            return
        if self.team == "enemy":
            self.attack(self.wave)

    def move(self, kind: Optional[str]) -> None:
        if kind is None:
            self.y -= 10

    def attack(self, wave: int) -> None:
        try:
            self.y += (5 + wave//2)
        except TypeError:
            print("Null wave")



