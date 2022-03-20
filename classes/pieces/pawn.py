if __name__ == "__main__":
    print("this file is not suposed to be run")
    quit()

from classes.pieces.Piece import Piece
import settings as st

class Pawn(Piece):
    def __init__(self, coord:list, IsBlack:bool=True) -> None:
        if IsBlack:
            sprite=[0,0,0,16,23,st.green]
        else:
            sprite=[0,0,32,16,23,st.green]
        super().__init__(coord, sprite, IsBlack)