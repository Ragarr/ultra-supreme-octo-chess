import pyxel
# from classes.Board import Board
from classes.pieces.rook import Rook
from classes.pieces.pawn import Pawn
from classes.pieces.queen import Queen
from classes.pieces.king import King
from classes.pieces.knight import Knight
from classes.pieces.bishop import Bishop
import settings as st
import numpy as np

class game:
    def __init__(self) -> None:
        pyxel.init(st.screen_width,st.screen_height,caption = "Super orto mega ajedrez", fps = st.fps,scale=4)
        pyxel.load(st.assets_path)
        pyxel.mouse(True)
        self.__board_sprite=[0,0,1,0,0,191,191,st.black]
        self.array=np.full([8, 8], '▨')
        self.pieces1=[]
        self.pieces2=[]
        self.init_pieces()
        self.i=0
        # esta linea siempre al final 
        pyxel.run(self.update,self.draw)
    def __str__(self) -> str:
        return str(np.array2string(self.array, formatter={'all': lambda x: str(x)}))+'\n'

    def update(self):
        # print(self)
        self.update_board()
        if self.i>50:
            self.play1()
        self.i+=1
        
    def draw(self):
        pyxel.cls(st.light_brown)
        self.draw_board()
        self.draw_pieces()
    

    def draw_pieces(self):
        for piece in self.pieces1:
            pyxel.blt(*piece.coord,*piece._sprite)
        for piece in self.pieces2:
            pyxel.blt(*piece.coord,*piece._sprite)
    
    def draw_board(self):
        '''just draws the board'''
        pyxel.blt(*self.__board_sprite)
    
    def update_board(self):
        for piece in self.pieces1:
            self.array[abs(8-piece.position[1]),(piece.position[0]-1)]=piece
        for piece in self.pieces2:
            self.array[abs(8-piece.position[1]),(piece.position[0]-1)]=piece
    def init_pieces(self):
        '''sets every piece on his initial coordinate'''
        for i in range(1,9,1):
            self.pieces1.append(Pawn([i,7]))
        self.pieces1.append(Rook(['a',8]))
        self.pieces1.append(Rook(['h',8]))
        self.pieces1.append(Queen(['e',8]))
        self.pieces1.append(King(['d',8]))
        self.pieces1.append(Bishop(['f',8]))
        self.pieces1.append(Bishop(['c',8]))
        self.pieces1.append(Knight(['b',8]))
        self.pieces1.append(Knight(['g',8]))

        for j in range(1,9,1):
            self.pieces2.append(Pawn([j,2],False))
        self.pieces2.append(Rook(['a',1],False))
        self.pieces2.append(Rook(['h',1],False))
        self.pieces2.append(Queen(['e',1],False))
        self.pieces2.append(King(['d',1],False))
        self.pieces2.append(Bishop(['f',1],False))
        self.pieces2.append(Bishop(['c',1],False))
        self.pieces2.append(Knight(['b',1],False))
        self.pieces2.append(Knight(['g',1],False))
    def select(self,pos:list):
        print('selected',pos)
        pyxel.blt(*pos,0,50,50,24,24)
    def play1(self):
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            for piece in self.pieces1:
                print(pyxel.mouse_x//24,pyxel.mouse_y//24)
                if (pyxel.mouse_x//24,pyxel.mouse_y//24)==piece.position:
                    print('piece selected')
                    self.select(piece.position)

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            print('board selected')
            self.select([pyxel.mouse_x//24+1,8-pyxel.mouse_y//24])
            
                    

game()
