if __name__ == "__main__":
    print("this file is not suposed to be run")
    quit()

from classes.pieces.Piece import Piece
import settings as st

class King(Piece):
    def __init__(self, pos:list=[8,0], IsBlack:bool=True) -> None:
        if IsBlack:
            sprite=[0,64,0,16,23,st.green]
        else:
            sprite=[0,64,32,16,23,st.green]
        super().__init__(pos, sprite, IsBlack)
    def __str__(self) -> str:
        if self._IsBlack:
            return 'k'
        else:
            return 'K'