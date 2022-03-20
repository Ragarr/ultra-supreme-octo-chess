import pyxel
import settings as st
from classes import *

class game:
    def __init__(self) -> None:
        pyxel.init(st.ancho_pantalla,st.alto_pantalla,caption = "Super orto mega ajedrez", fps = st.fps)

        pyxel.mouse(True)
        pyxel.run(self.update,self.draw)

    def update(self):
        pass
    
    def draw(self):
        pyxel.cls(1)

game()
