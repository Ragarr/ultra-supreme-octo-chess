import pyxel
from MyBoard import MyBoard
import settings as st
import numpy as np

class game:
    def __init__(self) -> None:
        pyxel.init(st.screen_width,st.screen_height,caption = "Super orto mega ajedrez", fps = st.fps,scale=4)
        pyxel.load(st.assets_path)
        pyxel.mouse(True)
        self.__board=MyBoard()
        print(self)
        # esta linea siempre al final 
        pyxel.run(self.update,self.draw)
    
    def __str__(self) -> str:
        return str(self.__board)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(st.light_brown)
        self.draw_board()

    
    def draw_board(self):
        '''just draws the board'''
        pyxel.blt(0,0,*self.__board.sprite)
    
    
    
game()
