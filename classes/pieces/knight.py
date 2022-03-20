if __name__ == "__main__":
    print("this file is not suposed to be run")
    quit()

from classes.pieces.Piece import Piece
import settings as st

class Knight(Piece):
    def __init__(self, coord:list=[8,0], IsBlack:bool=True) -> None:
        if IsBlack:
            sprite=[0,32,0,16,23,st.green]
        else:
            sprite=[0,32,32,16,23,st.green]
        super().__init__(coord, sprite, IsBlack)