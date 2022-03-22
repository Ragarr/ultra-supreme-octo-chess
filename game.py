from select import select
import pyxel
from classes.pieces.piece import Piece
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
        self.array=np.full([8, 8], '.',dtype=object)
        self.init_pieces()
        self.piece_selected=False
        self._selecteds=[]
        # esta linea siempre al final 
        pyxel.run(self.update,self.draw)
    def __str__(self) -> str:
        return str(np.array2string(self.array.copy(), formatter={'all': lambda x: str(x)}))+'\n'

    def update(self):
        # print(self)
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            if self.piece_selected:
                self.select([pyxel.mouse_y//24,pyxel.mouse_x//24])
                self.piece_selected=False
            elif isinstance(self.array[pyxel.mouse_y//24][pyxel.mouse_x//24],Piece):
                self.select_piece([pyxel.mouse_y//24,pyxel.mouse_x//24])
                self.piece_selected=True
            

    def draw(self):
        pyxel.cls(st.light_brown)
        self.draw_board()
        self.draw_selections()
        self.draw_pieces()


    

    def draw_pieces(self):
        i=0
        for row in self.array:
            j=0
            for piece in row:
                self.draw_piece(piece,[i,j])
                j+=1
            i+=1
    def draw_piece(self,piece:Piece,pos:list):
        if isinstance(piece,Piece):
            coord=[((pos[1])*24)+4,(pos[0])*24] 
            pyxel.blt(coord[0],coord[1],*piece._sprite)
    
    def draw_board(self):
        '''just draws the board'''
        pyxel.blt(*self.__board_sprite)
    
    def update_board(self):
        pass
    def init_pieces(self):
        '''sets every piece on his initial coordinate'''
        self.array[0]=[Rook(True),Knight(True),Bishop(True),King(True),Queen(True),Bishop(True),Knight(True),Rook(True)]
        self.array[1]=[Pawn(True),Pawn(True),Pawn(True),Pawn(True),Pawn(True),Pawn(True),Pawn(True),Pawn(True)]
        self.array[6]=[Pawn(False),Pawn(False),Pawn(False),Pawn(False),Pawn(False),Pawn(False),Pawn(False),Pawn(False)]
        self.array[7]=[Rook(False),Knight(False),Bishop(False),Queen(False),King(False),Bishop(False),Knight(False),Rook(False)]
    def select_piece(self,pos:list):
        if self.piece_selected:
            return

        self._selecteds=[]
        coord=[((pos[1])*24),(pos[0])*24]
        if coord in self._selecteds:
            return
        self._selecteds.append(coord)

    def select(self,pos:list):
        if len(self._selecteds)>2:
            self._selecteds=[]
            self.piece_selected=False
        coord=[((pos[1])*24),(pos[0])*24]
        if coord in self._selecteds:
            return
        self._selecteds.append(coord)
    
    def draw_selections(self):
        for selec in self._selecteds:
            pyxel.blt(*selec,*st.selected_sprite)  
                    

game()
