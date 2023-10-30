from tupy import Label
from tupy import Image

class option(Label):
    def __init__(self, name: str, x: int, y: int) -> None:
        super().__init__(name, x, y)
        self.selected: bool = False
    
    def update(self) -> None:
        if self.selected:
            self.font = "Arial 28"
            self.color = "red"
            return
        self.font = "Arial 20"
        self.color = "black"

class Menu(Image):
    def __init__(self) -> None:
        super().__init__("./assets/backgroung_01.jpg")
        self.cur_option: int = 1
        self.items: list[option] = [
                option("Iniciar", 225, 300), \
                option("Dificuldade", 225, 275), \
                option("Sair", 225, 250) \
                ]
    
    def update(self) -> None:
        if keyboard.is_key_just_down("Down"):
            self.change_select(1)
        if keyboard.is_key_just_down("Up"):
            self.change_select(-1)

    def change_select(self, jmp: int) -> None:
        if (self.cur_option + jmp) > 3:
            self.cur_option = 1
            return
        if (self.cur_option + jmp) < 1:
            self.cur_option = 3
            return
        self.cur_option += jmp
    
    def enter(self):
        pass

    def change_dificulty(self):
        pass

    def exit(self):
        pass


        
