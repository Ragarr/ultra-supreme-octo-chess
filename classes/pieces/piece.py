if __name__ == "__main__":
    print("this file is not suposed to be run")
    quit()
import settings as st

class Piece:
    def __init__(self,coord:list, sprite:list,IsBlack:bool) -> None:
        self._sprite = sprite
        if isinstance(coord[0],str):
            coord[0]=self.__replace_letter(coord[0])
        self.__coord = coord
        self._IsBlack = IsBlack
    @property
    def coord(self):
        # tranforma las coordenadas del tablero a coordenadas de pixeles
        # cada casilla son 24 pixeles, con 5 pixeles extra centras la pieza en las x
        return [self.__coord[0]*24+5,st.screen_height-(self.__coord[1]*24)] 
    @coord.setter
    def coord(self,coord:list):
        if isinstance(coord[0],str):
            coord[0]=self.__replace_letter(coord[0])
        self.__coord = coord
    
    def __replace_letter(self,letter):
        dictt = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
        return dictt[letter]-1
