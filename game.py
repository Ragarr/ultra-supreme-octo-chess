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
        pyxel.init(st.screen_width, st.screen_height,
                   caption="Super orto mega ajedrez", fps=st.fps, scale=4)
        pyxel.load(st.assets_path)
        pyxel.mouse(True)
        self.init_parameters()
        # esta linea siempre al final
        pyxel.run(self.update, self.draw)
    def init_parameters(self):
        self.__board_sprite = [0, 0, 1, 0, 0, 191, 191, st.black]
        self.array = np.full([8, 8], None, dtype=object)
        self.init_pieces()
        self.piece_selected = False
        self._BlacksTurn=False
        print('turno de blancas')
        self._selecteds = {}
        self.first_coords=()
        self.second_coords=()
    def __str__(self) -> str:
        return str(np.array2string(self.array, formatter={'all': lambda x:  str(x) if x else '.'}))+'\n'

    def update(self):
        # print(self)
        self.select_and_move()
        
            

                
    def select_and_move(self):
        if len(self._selecteds)==0 and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON): # para evitar el multi click usamos btnp en vez de btn
            first_selection=self.array[pyxel.mouse_y//24][pyxel.mouse_x//24] # es una pieza o un none si has pinchado en vacio
            self.first_coords=(pyxel.mouse_y//24,pyxel.mouse_x//24) # es una coordenada
            if first_selection and first_selection._IsBlack==self._BlacksTurn:
                print('1º has seleccionado', first_selection)
                self._selecteds[self.first_coords]=first_selection
                print(self._selecteds)

        if len(self._selecteds)==1 and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            second_selection=self.array[pyxel.mouse_y//24][pyxel.mouse_x//24] # es una pieza o un none si has pinchado en vacio
            self.second_coords=(pyxel.mouse_y//24,pyxel.mouse_x//24) # es una coordenada
            print('2º has seleccionado', second_selection)
            self._selecteds[self.second_coords]=second_selection
            print(self._selecteds)

        if len(self._selecteds)==2:  
            if self._selecteds[self.first_coords]:
                if self._selecteds[self.first_coords].move(self.array,self.first_coords,self.second_coords):
                    print('se ha movido la ficha')
                    self.array[self.second_coords[0],self.second_coords[1]]=self.array[self.first_coords[0],self.first_coords[1]]
                    self.array[self.first_coords[0],self.first_coords[1]]=None
                    self._BlacksTurn= not self._BlacksTurn
                    txt =  'negras' if self._BlacksTurn else 'blancas'
                    print('turno de', txt)
                else:
                    print('NO se ha movido la ficha')
            else:
                print('seleccione una ficha primero po favo')
            self._selecteds.clear()


    def draw(self):
        pyxel.cls(st.light_brown)
        self.draw_board()
        self.draw_selections()
        self.draw_pieces()

    def draw_pieces(self):
        i = 0
        for row in self.array:
            j = 0
            for piece in row:
                if isinstance(piece, Piece):
                    coord = [(j*24)+4,i*24]
                    pyxel.blt(coord[0], coord[1], *piece._sprite)
                j += 1
            i += 1

        

    def draw_board(self):
        '''just draws the board'''
        pyxel.blt(*self.__board_sprite)

    def update_board(self):
        pass

    def init_pieces(self):
        '''sets every piece on his initial coordinate'''
        self.array[0] = [Rook(True), Knight(True), Bishop(True), King(True), Queen(True), Bishop(True), Knight(True), Rook(True)]
        self.array[1] = [Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True)]
        self.array[6] = [Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False)]
        self.array[7] = [Rook(False), Knight(False), Bishop(False), Queen(False), King(False), Bishop(False), Knight(False), Rook(False)]

    def select_piece(self, pos: list):
        if self.piece_selected:
            return

        self._selecteds = []
        coord = [((pos[1])*24), (pos[0])*24]
        if coord in self._selecteds:
            return
        self._selecteds.append(coord)

    def select(self, pos: list):
        if len(self._selecteds) > 2:
            self.piece_selected = False
        coord = [((pos[1])*24), (pos[0])*24]
        if coord in self._selecteds:
            return
        self._selecteds.append(coord)

    def draw_selections(self):
        for selec in self._selecteds.keys():
            pyxel.blt(selec[1]*24,selec[0]*24, *st.selected_sprite)

    '''def move_piece(self,pos_origen,pos_final):
        print('ficha movida')
        print(self.array[pos_final[0]][pos_final[1]])
        print(self.array[pos_origen[0]][pos_origen[1]])
        if isinstance(self.array[pos_origen[1]][pos_origen[0]],Piece) and isinstance(self.array[pos_origen[1]][pos_origen[0]],Piece):
            if self.array[pos_origen[1]][pos_origen[0]]._IsBlack!=self.array[pos_origen[1]][pos_origen[0]]._IsBlack:
                self.array[pos_final[1]][pos_final[0]]=self.array[pos_origen[1]][pos_origen[0]]
                self.array[pos_origen[1]][pos_origen[0]]='.'
        else:
            self.array[pos_final[1]][pos_final[0]]=self.array[pos_origen[1]][pos_origen[0]]
            self.array[pos_origen[1]][pos_origen[0]]='.'
        self._selecteds=[]'''


game()
