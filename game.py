import pyxel
from MyBoard import MyBoard
import settings as st


class game:
    def __init__(self) -> None:
        pyxel.init(st.screen_width,st.screen_height,caption = "Super orto mega ajedrez", fps = st.fps,scale=4)
        pyxel.load(st.assets_path)
        pyxel.mouse(True)
        self.__board=MyBoard()
        # esta linea siempre al final 
        pyxel.run(self.update,self.draw)

    def update(self):
        print(self.__board)

    
    def draw(self):
        pyxel.cls(st.light_brown)
    
    def draw_board(self):
        
    

    
    
game()
