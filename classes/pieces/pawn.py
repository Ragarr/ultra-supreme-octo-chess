if __name__ == "__main__":
    print("this file is not suposed to be run")
    quit()

from hashlib import new
from classes.pieces.piece import Piece
import settings as st

class Pawn(Piece):
    def __init__(self,IsBlack:bool=True) -> None:
        if IsBlack:
            sprite=[0,0,0,16,23,st.green]
        else:
            sprite=[0,0,32,16,23,st.green]
        super().__init__(sprite, IsBlack)
    def __str__(self) -> str:
        if self._IsBlack:
            return 'p'
        else:
            return 'P'
    
    def move(self,ctx_array,old_coords,new_coords):
        if old_coords==new_coords:
            return False
        # movimiento diagonal
        if (new_coords[1]!=old_coords[1] and ctx_array[new_coords[0]][new_coords[1]] and 
            ctx_array[new_coords[0]][new_coords[1]]._IsBlack!=self._IsBlack):
            print('movimiento diagonal',abs(new_coords[0]-old_coords[0]))
            if self._IsBlack:
                if new_coords[0]-old_coords[0]!=1 :
                    return False
                else:
                    return True
            else:
                if new_coords[0]-old_coords[0]!=-1 :
                    return False
                else:
                    return True
        # movimiento en linea recta
        if new_coords[1]==old_coords[1] and not ctx_array[new_coords[0]][new_coords[1]]:
            print('movimiento recto',abs(new_coords[0]-old_coords[0]))
            if abs(new_coords[0]-old_coords[0])==2:
                if old_coords[0]==1 or old_coords[0]==6:
                    return True
                else:
                    return False
            elif abs(new_coords[0]-old_coords[0])==1:
                return True
        return False
            

        
