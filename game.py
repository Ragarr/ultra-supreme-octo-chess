import pyxel
import sys
import timeit
import chess_game
import settings as st


class game:
    def __init__(self) -> None:
        pyxel.init(st.screen_width,st.screen_height,caption = "Super orto mega ajedrez", fps = st.fps,scale=4)
        pyxel.load(st.assets_path)
        pyxel.mouse(True)
        board=
        # esta linea siempre al final 
        pyxel.run(self.update,self.draw)

    def update(self):
        print(self.__board)
        self.__board.update(self.pieces)
    
    def draw(self):
        pyxel.cls(st.light_brown)
        self.draw_board()
        self.draw_pieces()
    

    
    
game()
