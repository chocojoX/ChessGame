import numpy as np


class ChessPiece(object):
    def __init__(self, position, color):
        self.position = position
        self.legal_destinations = None
        self.last_square = None
        assert color in ["white", "black"], "Color is neither white nor black"
        if color=="white":
            self.color = 0  # 0 for white, 1 for black
        else:
            self.color = 1


    def force_update_position(self, new_position):
        self.position = new_position


    def move_piece(self, new_position, board):
        if is_move_legal(self, new_position, board):
            self.force_update_position(position)
            return True
        else:
            return False


    def get_color(self):
        return self.color


    def get_coordinates(self):
        return self.coordinates



class Pawn(ChessPiece):
    def __init__ (self, position, color):
        self.en_passant_possible=False
        super().__init__(position, color)


class Knight(ChessPiece):
    def __init__ (self, position, color):
        super().__init__(position, color)


class Bishop(ChessPiece):
    def __init__ (self, position, color):
        super().__init__(position, color)


class Rook(ChessPiece):
    def __init__ (self, position, color):
        super().__init__(position, color)


class Queen(ChessPiece):
    def __init__ (self, position, color):
        super().__init__(position, color)


class King(ChessPiece):
    def __init__ (self, position, color):
        super().__init__(position, color)
