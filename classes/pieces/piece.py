if __name__ == "__main__":
    print("this file is not suposed to be run")
    quit()
import settings as st

class Piece:
    def __init__(self,pos:list, sprite:list,IsBlack:bool) -> None:
        self._sprite = sprite
        if isinstance(pos[0],str):
            pos[0]=self.__replace_letter(pos[0])
        for i in pos:
            if i<1 or i>8:
                raise ValueError("coord out of range")
        self._position= pos
        self._IsBlack = IsBlack

    @property
    def coord(self):
        # tranforma las coordenadas del tablero a coordenadas de pixeles
        # cada casilla son 24 pixeles, con 5 pixeles extra centras la pieza en las x
        return [(self._position[0]-1)*24+4,st.screen_height-(self._position[1]*24)+1] 
    @property
    def position(self):
        return self._position
    @position.setter
    def position(self,position:list):
        if isinstance(position[0],str):
            position[0]=self.__replace_letter(position[0])
        for i in position:
            if i<1 or i>8:
                raise ValueError("piece position out of board")
        self.__position = position
    
    def __replace_letter(self,letter):
        dictt = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
        return dictt[letter]
    def move(self,new_coord):
        self.__move(new_coord)   
    def __move(self,new_coord):
        raise Exception("The movement of this piece is not defined")
    def __str__(self) -> str:
        return 'generic piece'