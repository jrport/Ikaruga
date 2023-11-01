from tupy import BaseGroup
from tupy import Label
from tupy import Image
from tupy import Rectangle

class background(Image):
    def __init__(self) -> None:
        super().__init__('./background_01.jpg', 100, 100)
        
class menu(BaseGroup):
    
