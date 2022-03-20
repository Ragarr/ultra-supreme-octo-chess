import pyxel
import settings as st
from classes import *

class game:
    def __init__(self) -> None:
        pyxel.init(st.screen_width,st.screen_height,caption = "Super orto mega ajedrez", fps = st.fps)
        pyxel.load(st.assets_path)
        pyxel.mouse(True)
        pyxel.run(self.update,self.draw)

    def update(self):
        pass
    
    def draw(self):
        pyxel.cls(st.light_brown)

    def draw_board(self):
        pyxel.blt()
game()
