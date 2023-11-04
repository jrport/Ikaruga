from tupy import Label, BaseGroup, keyboard

class InitialMenu(BaseGroup):
    def __init__(self) -> None:
        self.options: list[Label] = [Label("Iniciar", 300, 275, 'Arial 16', 'grey', anchor = 'center'),
                                    Label("Dificuldade", 300, 300, 'Arial 16', 'grey', anchor = 'center')
                                    ]
        self._add(self.options[0])
        self._add(self.options[1])
        self._add(Label("Ikaruga", 300, 250, 'Arial 22', 'grey', anchor = 'center'))
        self.cur_selected = 0

    def update(self) -> None:
        if game.initial_pause:
            if keyboard.is_key_just_down("Down"):
                self.change_highlight(-1)
                return 
            if keyboard.is_key_just_down("Up"):
                self.change_highlight(1)
                return
            if keyboard.is_key_just_down("Enter"):
                if self.cur_selected == 0:
                    self.start()
                    return
                if self.cur_selected == 1:
                    self.change_dificulty()
                    return

    def start(self) -> None:
        game.unpause_initial()

    def change_dificulty(self) -> None:
        pass

    def change_highlight(self, offset: int) -> None:
        self.options[self.cur_selected].color = 'grey'
        self.change_option(offset)
        self.options[self.cur_selected].color = 'white'


    def change_option(self, offset: int) -> None:
        if offset == 1:
            self.cur_selected += 1
            if (self.cur_selected == 2):
                self.cur_selected = 1
                return
            self.cur_selected += 1
            return
        if offset == -1:
            self.cur_selected -= 1
            if self.cur_selected == -1:
                self.cur_selected = 1

