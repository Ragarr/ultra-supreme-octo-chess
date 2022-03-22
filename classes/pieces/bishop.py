if __name__ == "__main__":
    print("this file is not suposed to be run")
    quit()

from classes.pieces.piece import Piece
import settings as st

class Bishop(Piece):
    def __init__(self, pos:list=[8,0], IsBlack:bool=True) -> None:
        if IsBlack:
            sprite=[0,48,0,16,23,st.green]
        else:
            sprite=[0,48,32,16,23,st.green]
        super().__init__(pos, sprite, IsBlack)

    def __str__(self) -> str:
        if self._IsBlack:
            return 'b'
        else:
            return 'B'