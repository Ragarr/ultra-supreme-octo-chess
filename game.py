import pyxel
from classes.MyBoard import MyBoard
import settings as st
import numpy as np

class game:
    def __init__(self) -> None:
        pyxel.init(st.screen_width,st.screen_height,caption = "Super orto mega ajedrez", fps = st.fps,scale=4)
        pyxel.load(st.assets_path)
        pyxel.mouse(True)
        self._selecteds={}
        self.__board=MyBoard()

        print(self)
        # esta linea siempre al final 
        pyxel.run(self.update,self.draw)
    
    def __str__(self) -> str:
        return str(self.__board)

    def update(self):
        self.select_and_move()

    def draw(self):
        pyxel.cls(st.light_brown)
        # print(self.__board,end='\n\n')
        self.draw_board()
        self.draw_pieces()
        self.draw_selections()
    
    def draw_board(self):
        '''just draws the board'''
        pyxel.blt(0,0,*self.__board.sprite)
    
    def draw_pieces(self):
        i=0
        for row in self.__board.array:
            j=0
            for piece in row:
                self.draw_piece(piece,[i,j])
                j+=1
            i+=1
    
    def draw_piece(self,piece:str,pos:list):
        if piece=='.':
            return
        sprites={'r':[0,16,0,16,23,st.green],'b':[0,48,0,16,23,st.green],'k':[0,64,0,16,23,st.green],
                 'n':[0,32,0,16,23,st.green],'p':[0,0,0,16,23,st.green],'q':[0,80,0,16,23,st.green],
                 'R':[0,16,32,16,23,st.green],'B':[0,48,32,16,23,st.green],'K':[0,64,32,16,23,st.green],
                 'N':[0,32,32,16,23,st.green],'P':[0,0,32,16,23,st.green],'Q':[0,80,32,16,23,st.green]}
        coord=[((pos[1])*24)+4,(pos[0])*24] 
        pyxel.blt(coord[0],coord[1],*sprites[piece])
    
    def select_and_move(self):
        if len(self._selecteds)==0 and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON): # para evitar el multi click usamos btnp en vez de btn
            first_selection=self.__board.array[pyxel.mouse_y//24][pyxel.mouse_x//24] # es una pieza o un none si has pinchado en vacio
            self.first_coords=(pyxel.mouse_y//24,pyxel.mouse_x//24) # es una coordenada
            if first_selection and first_selection._IsBlack==self._BlacksTurn:
                print('1º has seleccionado', first_selection)
                self._selecteds[self.first_coords]=first_selection
                print(self._selecteds)

        if len(self._selecteds)==1 and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            second_selection=self.__board.array[pyxel.mouse_y//24][pyxel.mouse_x//24] # es una pieza o un none si has pinchado en vacio
            self.second_coords=(pyxel.mouse_y//24,pyxel.mouse_x//24) # es una coordenada
            print('2º has seleccionado', second_selection)
            self._selecteds[self.second_coords]=second_selection
            print(self._selecteds)

        if len(self._selecteds)==2:  
            if self._selecteds[self.first_coords]:
                if self._selecteds[self.first_coords].move(self.__board.array,self.first_coords,self.second_coords):
                    print('se ha movido la ficha')
                    self.__board.array[self.second_coords[0],self.second_coords[1]]=self.__board.array[self.first_coords[0],self.first_coords[1]]
                    self.__board.array[self.first_coords[0],self.first_coords[1]]=None
                    self._BlacksTurn= not self._BlacksTurn
                    txt =  'negras' if self._BlacksTurn else 'blancas'
                    print('turno de', txt)
                else:
                    print('NO se ha movido la ficha')
            else:
                print('seleccione una ficha primero po favo')
            self._selecteds.clear()
            print(self)
    
    
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

game()
