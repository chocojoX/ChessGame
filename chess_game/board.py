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


if __name__=="__main__":
    board = ChessBoard()
    pass
