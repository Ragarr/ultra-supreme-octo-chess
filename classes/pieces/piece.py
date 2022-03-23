if __name__ == "__main__":
    print("this file is not suposed to be run")
    quit()
import settings as st

class Piece:
    def __init__(self,sprite:list,IsBlack:bool) -> None:
        self._IsBlack=IsBlack
        self._sprite = sprite
    def move(self,old_coords,new_coords):
        print('esta pieza tiene un movimiento generico que siempre es posible')
        return True


