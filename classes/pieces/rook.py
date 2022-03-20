from classes.pieces.Piece import Piece


if __name__ == "__main__":
    print("this file is not suposed to be run")
    quit()

class Rook(Piece):
    def __init__(self, coord: list, sprite: list) -> None:
        super().__init__(coord, sprite)