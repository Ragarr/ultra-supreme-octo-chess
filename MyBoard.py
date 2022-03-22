import chess
import re
import numpy as np

class MyBoard(chess.Board):
    def get_array(self):
        return np.asanyarray(re.split(' |\n',str(self))).reshape(8,8)