if __name__ == "__main__":
    print("this file is not suposed to be run")
    quit()

from classes.pieces.Piece import Piece
import settings as st

class Queen(Piece):
    def __init__(self, pos:list, IsBlack:bool=True) -> None:
        if IsBlack:
            sprite=[0,80,0,16,23,st.green]
        else:
            sprite=[0,80,32,16,23,st.green]
        super().__init__(pos, sprite, IsBlack)
    def __str__(self) -> str:
        if self._IsBlack:
            return 'q'
        else:
            return 'Q'