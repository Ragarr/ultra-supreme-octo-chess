if __name__ == "__main__":
    print("this file is not suposed to be run")
    quit()

from re import T
from classes.pieces.piece import Piece
import settings as st

class Rook(Piece):
    def __init__(self, IsBlack:bool=True) -> None:
        if IsBlack:
            sprite=[0,16,0,16,23,st.green]
        else:
            sprite=[0,16,32,16,23,st.green]
        super().__init__(sprite, IsBlack)
    
    def move(self,ctx_array,old_coords,new_coords):
        ''' defines the movement of a rook'''
        print('movimiento de torre')
        if old_coords==new_coords:
            return False
        # movimiento en linea recta
        if new_coords[0]==old_coords[0] and not self.__piece_on_path_x(ctx_array,old_coords[1],new_coords[1]): # clear path on x axis
            return True
        if new_coords[1]==old_coords[1] and not  self.__piece_on_path_y(ctx_array,old_coords[0],new_coords[0]): # clear path on y axis
            return True
        return False

    def __piece_on_path_x(self,ctx_array,old_coords_x,new_coords_x):
        ''' returns the piece on the path of the rook'''
        print('')
        ally_piece=None
        enemy_piece=None
        if old_coords_x==new_coords_x:
            return None
        for i in range(old_coords_x,new_coords_x):
            print(ctx_array[i][old_coords_x])
            if ctx_array[i][old_coords_x]:
                if ctx_array[i][old_coords_x]._IsBlack==self._IsBlack:
                    enemy_piece = [i,old_coords_x]
                if ctx_array[i][old_coords_x]._IsBlack!=self._IsBlack:
                    ally_piece= [i,old_coords_x]
        return True

    def __piece_on_path_y(self,ctx_array,old_coords_y,new_coords_y):
        ''' returns the piece on the path of the rook'''
        print('')
        if old_coords_y==new_coords_y:
            return None
        for i in range(old_coords_y,new_coords_y):
            print(ctx_array[old_coords_y][i])
            if ctx_array[old_coords_y][i]:
                return True
        return False        

    def __str__(self) -> str:
        if self._IsBlack:
            return 'r'
        else:
            return 'R'