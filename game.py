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
        self.pieces=[]
        self.pieces=[]
        self.init_pieces()
        # esta linea siempre al final 
        pyxel.run(self.update,self.draw)

    def update(self):
        print(self.__board)
        self.__board.update(self.pieces)
    
    def draw(self):
        pyxel.cls(st.light_brown)
        self.draw_board()
        self.draw_pieces()
    

    def draw_pieces(self):
        for piece in self.pieces:
            pyxel.blt(*piece.coord,*piece._sprite)
        for piece in self.pieces:
            pyxel.blt(*piece.coord,*piece._sprite)
    def draw_board(self):
        '''just draws the board'''
        pyxel.blt(0,0,*self.__board._sprite)
    
    
    def init_pieces(self):
        '''sets every piece on his initial coordinate'''
        for i in range(1,9,1):
            self.pieces.append(Pawn([i,7]))
        self.pieces.append(Rook(['a',8]))
        self.pieces.append(Rook(['h',8]))
        self.pieces.append(Queen(['e',8]))
        self.pieces.append(King(['d',8]))
        self.pieces.append(Bishop(['f',8]))
        self.pieces.append(Bishop(['c',8]))
        self.pieces.append(Knight(['b',8]))
        self.pieces.append(Knight(['g',8]))

        for j in range(1,9,1):
            self.pieces.append(Pawn([j,2],False))
        self.pieces.append(Rook(['a',1],False))
        self.pieces.append(Rook(['h',1],False))
        self.pieces.append(Queen(['e',1],False))
        self.pieces.append(King(['d',1],False))
        self.pieces.append(Bishop(['f',1],False))
        self.pieces.append(Bishop(['c',1],False))
        self.pieces.append(Knight(['b',1],False))
        self.pieces.append(Knight(['g',1],False))
    
game()
