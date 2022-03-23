if __name__ == "__main__":
    print("this file is not suposed to be run")
    quit()
import settings as st

class Piece:
    def __init__(self,sprite:list,IsBlack:bool) -> None:
        self._IsBlack=IsBlack
        self._sprite = sprite
    def move(self,ctx_array,old_coords,new_coords):
        print('esta pieza tiene un movimiento generico que siempre es posible')
        # ctx array significa context array que es la matriz del tablero para saber las posiciones de las otras fichas
        return True


