import pyxel
from classes.Board import Board
import settings as st


class game:
    def __init__(self) -> None:
        pyxel.init(st.screen_width,st.screen_height,caption = "Super orto mega ajedrez", fps = st.fps,scale=4)
        pyxel.load(st.assets_path)
        pyxel.mouse(True)
        self.__board = Board()
        
        # esta linea siempre al final 
        pyxel.run(self.update,self.draw)

    def update(self):
        pass
    
    def draw(self):
        pyxel.cls(st.light_brown)
        self.draw_board()

    def draw_board(self):
        pyxel.blt(0,0,*self.__board._sprite)

game()
