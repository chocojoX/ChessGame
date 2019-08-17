import numpy as np
from utils import string2int_coordinates
from pieces import *

class ChessBoard(object):
    def __init__(self):
        self.create_board()
        self.init_board()
        print("Board has been set")

    def create_board(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        return True


    def init_board(self):
        # Add pawns
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            self.add_piece("pawn", color="white", coordinates=letter+"2")
            self.add_piece("pawn", color="black", coordinates=letter+"7")

        # Add Rooks
        self.add_piece("rook", color="white", coordinates="a1")
        self.add_piece("rook", color="white", coordinates="h1")
        self.add_piece("rook", color="black", coordinates="a8")
        self.add_piece("rook", color="black", coordinates="h8")

        # Add Knights
        self.add_piece("knight", color="white", coordinates="b1")
        self.add_piece("knight", color="white", coordinates="g1")
        self.add_piece("knight", color="black", coordinates="b8")
        self.add_piece("knight", color="black", coordinates="g8")

        # Add Bishops
        self.add_piece("bishop", color="white", coordinates="c1")
        self.add_piece("bishop", color="white", coordinates="f1")
        self.add_piece("bishop", color="black", coordinates="c8")
        self.add_piece("bishop", color="black", coordinates="f8")

        # Add Kings qnd Queens
        self.add_piece("king", color="white", coordinates="e1")
        self.add_piece("queen", color="white", coordinates="d1")
        self.add_piece("king", color="black", coordinates="e8")
        self.add_piece("queen", color="black", coordinates="d8")
        pass


    def add_piece(self, piece_type, color, coordinates):
        if piece_type == "pawn":
            piece = Pawn(coordinates, color)
        elif piece_type == "rook":
            piece = Rook(coordinates, color)
        elif piece_type == "knight":
            piece = Knight(coordinates, color)
        elif piece_type == "bishop":
            piece = Bishop(coordinates, color)
        elif piece_type == "king":
            piece = King(coordinates, color)
        elif piece_type == "queen":
            piece = Queen(coordinates, color)
        else:
            print(f"Piece {piece_type} does not exist")
            import pdb; pdb.set_trace()

        x,y = string2int_coordinates(coordinates)
        self.board[x][y] = piece
        pass


    def move_piece(self, origin, dest, piece_type=None):
        x,y = string2int_coordinates(origin)
        x_dest, y_dest = string2int_coordinates(dest)
        piece = self.board[x][y]
        assert piece is not None, f"No piece is present on square {origin}"
        # TODO: Need to handle the following cases :
        # 1.0 : Basic movements of the pieces
        # 1.1 : Captures
        # 2 : Castling (short and long)
        # 3 : En-passant
        # 4 : Pawn promotion
        assert piece.is_move_legal(dest, self), "Move is not legal."
        self.board[x][y] = None
        self.board[x_dest][y_dest] = piece
        piece.force_update_position(dest)
        return True


    def get_piece_on_square(self, coordinates):
        x, y = string2int_coordinates(coordinates)
        return self.board[x][y]


    def is_square_free(self, coordinates):
        return self.get_piece_on_square(coordinates) is None


    def get_color_of_piece_on_square(self, coordinates):
        assert not self.is_square_free(coordinates), f"Color of the piece is asked but the square {coordinates} is free."
        piece = self.get_piece_on_square(coordinates)
        return piece.get_color()


if __name__=="__main__":
    board = ChessBoard()
    board.move_piece('e2', 'e4')
    print(board.is_square_free('e2'))
    print(board.get_color_of_piece_on_square('e4'))
    board.move_piece('e4', 'e5')
    board.move_piece('e5', 'e6')
    # board.move_piece('e7', 'e5')
    pass
