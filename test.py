from tupy import *

class Bolha(Image):
  def __init__(self,x,y,velocidade):
    self.file = 'bolha.png'
    self.x = x
    self.y = y
    self.velocidade = velocidade
  def update(self):
    self.y -= self.velocidade
    if self.y < -20:
      self.y = 520
    if self.y > 520:
      self.y = -20


class Crianca(Image):
    def __init__(self, x, y):
        self.file = "crianca.png"
        self.x = x
        self.y = y
    def update(self):
        if keyboard.is_key_just_down('Left'):
            self.x -= 20
        if keyboard.is_key_just_down('Right'):
            self.x += 20
        if keyboard.is_key_just_down('Up'):
            self.y -= 20
        if keyboard.is_key_just_down('Down'):
            self.y += 20

c = Crianca(100,100)
run(globals())
