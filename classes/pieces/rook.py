if __name__ == "__main__":
    print("this file is not suposed to be run")
    quit()

from classes.pieces.piece import Piece
import settings as st

class Rook(Piece):
    def __init__(self, pos:list=[8,0], IsBlack:bool=True) -> None:
        if IsBlack:
            sprite=[0,16,0,16,23,st.green]
        else:
            sprite=[0,16,32,16,23,st.green]
        super().__init__(pos, sprite, IsBlack)
    
    def __move(self, new_coord, ctx):
        pass
    def __str__(self) -> str:
        if self._IsBlack:
            return 'r'
        else:
            return 'R'