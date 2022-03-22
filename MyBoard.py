import chess
import re
import numpy as np
import settings as st
class MyBoard(chess.Board):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    @property
    def sprite(self):
        return [1,0,0,191,191,st.black]
    def get_array(self):
        return np.asanyarray(re.split(' |\n',str(self))).reshape(8,8)
    

a=MyBoard()
print(a.get_array())