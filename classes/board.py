import settings as st
import numpy as np
if __name__ == "__main__":
    print("this file is not suposed to be run")
    quit()
'''
class Board:
    def __init__(self) -> None:
        self._sprite=[1,0,0,191,191,st.black]
        self.array=np.full([8, 8], '▨')

    def __str__(self) -> str:
        return str(np.array2string(self.array, formatter={'all': lambda x: str(x)}))+'\n'

    def update(self,pieces:list):
        for piece in pieces:
                    self.array[abs(8-piece.position[1]),(piece.position[0]-1)]=piece
            '''