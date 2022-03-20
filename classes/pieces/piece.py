if __name__ == "__main__":
    print("this file is not suposed to be run")
    quit()


class Piece:
    def __init__(self,coord:list, sprite:list) -> None:
        self._sprite = sprite
        self.coord = coord