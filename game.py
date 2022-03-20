import pyxel
import settings
from classes import *

class game:
    def __init__(self) -> None:
        pyxel.init(settings.ancho_pantalla,settings.alto_pantalla,caption = "Super orto mega ajedrez", fps = settings.fps)

        pyxel.mouse(True)
        pyxel.run(self.update,self.draw)

    def update(self):
        pass
    
    def draw(self):
        pyxel.cls(1)

game()