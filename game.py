import pyxel
from classes.Board import Board
from classes.pieces.Rook import Rook
import settings as st


class game:
    def __init__(self) -> None:
        pyxel.init(st.screen_width,st.screen_height,caption = "Super orto mega ajedrez", fps = st.fps,scale=4)
        pyxel.load(st.assets_path)
        pyxel.mouse(True)
        self.__board = Board()
        self.__p1_pieces=[]
        self.__p2_pieces=[]
        self.init_pieces()
        # esta linea siempre al final 
        pyxel.run(self.update,self.draw)

    def update(self):
        pass
    
    def draw(self):
        pyxel.cls(st.light_brown)
        self.draw_board()
        for piece in self.__p1_pieces:
            pyxel.blt(*piece.coord,*piece._sprite)

    def draw_board(self):
        pyxel.blt(0,0,*self.__board._sprite)
    def init_pieces(self):
        self.__p1_pieces.append(Rook(['a',8]))
game()
