from tupy import *

class menu_item(Image):
    def __init__(self, name: str) -> None:
        self.name: str = name 
        self._label = Label(name, self.x + 50, self.y - 30)
        self._label.color = "white"
        self.selected: bool = False
        self.origin = self._label._x
    def update(self) -> None:
        if self.selected:
            self._label._x += 30
        else:
            self._x = self.origin

class Menu(menu_item):
    def __init__(self) -> None:
      self.file: str = "./assets/backgroung_01.jpg"
      self.current_option: int = 1
      self.items: list[menu_item] = [
              menu_item("Iniciar"), \
              menu_item("Dificuldade"), \
              menu_item("Sair") \
              ]
      
    def update(self) -> None:
      if keyboard.is_key_down('Down'):
        self.change_selected(1)
      if keyboard.is_key_down('Up'):
        self.change_selected(-1)
      if self.current_option > 3:
        self.current_option = 1
      if self.current_option < 1:
        self.current_option = 3

    def change_selected(self, n: int) -> None:
        try:
            self.items[self.current_option].selected = False
            self.current_option = self.current_option + n
            self.items[self.current_option].selected = True
        except IndexError: 
            if self.current_option > 3:
                self.items[self.current_option].selected = False
                self.current_option = 1
                self.items[self.current_option].selected = True
            elif self.current_option < 1:
                self.items[self.current_option].selected = False
                self.current_option = 3
                self.items[self.current_option].selected = True

