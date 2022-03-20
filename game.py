import pyxel
from classes.Board import Board
from classes.pieces.Rook import Rook
from classes.pieces.Pawn import Pawn
from classes.pieces.Queen import Queen
from classes.pieces.King import King
from classes.pieces.Knight import Knight
from classes.pieces.Bishop import Bishop


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
        for i in range(1,9,1):
            self.__p1_pieces.append(Pawn([i,7]))
        self.__p1_pieces.append(Rook([1,8]))
        self.__p1_pieces.append(Rook([8,8]))
        self.__p1_pieces.append(Queen(['e',8]))
        self.__p1_pieces.append(King(['d',8]))
        self.__p1_pieces.append(Bishop(['f',8]))
        self.__p1_pieces.append(Bishop(['c',8]))
        self.__p1_pieces.append(Knight(['b',8]))
        self.__p1_pieces.append(Knight(['g',8]))

        for i in range(1,9,1):
            self.__p1_pieces.append(Pawn([i,2],False))
        self.__p1_pieces.append(Rook([1,1],False))
        self.__p1_pieces.append(Rook([8,1],False))
        self.__p1_pieces.append(Queen(['e',1],False))
        self.__p1_pieces.append(King(['d',1],False))
        self.__p1_pieces.append(Bishop(['f',1],False))
        self.__p1_pieces.append(Bishop(['c',1],False))
        self.__p1_pieces.append(Knight(['b',1],False))
        self.__p1_pieces.append(Knight(['g',1],False))
    
game()
