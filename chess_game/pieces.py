import numpy as np
import string
from utils import string2int_coordinates

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

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
        return self.position


    def is_move_legal(self, new_position, board):
        """
        This function checks if it is legal to move the piece to the square of coordinates
        new_position. It does not account for castling possibilities.
        """
        # TODO:
        # 1. Check if piece can move to its new position independantly of the other pieces
        if not self.is_destination_physically_legal(new_position, board):
            print(f"Destination {new_position} is not reachable from {self.get_coordinates()}")
            return False
        # 2. Check if other pieces are blocking the way (including friend pieces on the detination square)
        if not isinstance(self, Knight):
            squares = self.get_trajectory(new_position)
            for square in squares[:-1]:
                if not board.is_square_free(square):
                    print(f"Square {square} on trajectory is occupied")
                    return False
        if not board.is_square_free(new_position):
            if self.get_color() == board.get_color_of_piece_on_square(new_position):
                print(f"Capturing a piece of your own color on  squre {new_position}")
                return False
            elif isinstance(self, Pawn) and new_position[0]==self.get_coordinates()[0]:
                print(f"Pawn is advancing to square {new_position} where an opponent piece is stationned")
                return False
        # 3. Check if King is not in check after the
        return True


    def is_destination_physically_legal(self, new_position, board):
        """
        Returns True if the piece could reach new_position in one move on an empty board.
        Returns False otherwise
        """
        return new_position in self.get_physically_legal_destinations(board)


    def get_trajectory(self, new_position):
        """
        Lists all squares visited by the piece during the move.
        Square of arrival is last.
        """
        raise NotImplementedError


    def get_physically_legal_destinations(self, board):
        """
        Lists all squares where the piece could move if the board was empty.
        """
        raise NotImplementedError



class Pawn(ChessPiece):
    def __init__ (self, position, color):
        self.en_passant_possible=False
        super().__init__(position, color)

    def get_physically_legal_destinations(self, board):
        physically_legal_destinations = []
        # Only piece for which legal physical moves depend on its color
        if self.get_color()==0:
            # Piece is white
            coords = self.get_coordinates()
            # Normal moves
            physically_legal_destinations.append(coords[0]+str(int(coords[1]) + 1))
            # Checking for 2-square advances
            if coords[1] == '2':
                physically_legal_destinations.append(coords[0]+'4')
            # Checking for possible captures
            letter_index = string.ascii_lowercase.index(coords[0])
            if not letter_index in [0, 7]:
                capture_squares = [letters[letter_index-1]+str(int(coords[1])+1),
                                   letters[letter_index+1]+str(int(coords[1])+1)]
            elif letter_index == 0:
                capture_squares = ['b'+str(int(coords[1])+1)]
            elif letter_index == 7:
                capture_squares = ['g'+str(int(coords[1])+1)]

            physically_legal_destinations += capture_squares

            if coords[1] == '5':
                # TODO: Check for en-passant !
                pass

        else:
            # Piece is black
            coords = self.get_coordinates()
            # Normal moves
            physically_legal_destinations.append(coords[0]+str(int(coords[1]) - 1))
            # Checking for 2-square advances
            if coords[1] == '7':
                physically_legal_destinations.append(coords[0]+'5')
            # Checking for possible captures
            letter_index = string.ascii_lowercase.index(coords[0])
            if not letter_index in [0, 7]:
                capture_squares = [letters[letter_index-1]+str(int(coords[1])-1),
                                   letters[letter_index+1]+str(int(coords[1])-1)]
            elif letter_index == 0:
                capture_squares = ['b'+str(int(coords[1])-1)]
            elif letter_index == 7:
                capture_squares = ['g'+str(int(coords[1])-1)]

            physically_legal_destinations += capture_squares

            if coords[1] == '4':
                # TODO: Check for en-passant !
                pass

        return physically_legal_destinations


    def get_trajectory(self, new_position):
        coords = self.get_coordinates()
        number = int(coords[1])
        new_number = int(new_position[1])
        if self.get_color()==0:
            if new_number == number+1:
                # Pawn has either only advanced of one square or captured
                return [new_position]
            else:
                # Pawn has advanced two squares
                return [coords[0]+str(int(coords[1])+1), new_position]
        else:
            if new_number == number-1:
                # Pawn has either only advanced of one square or captured
                return [new_position]
            else:
                # Pawn has advanced two squares
                return [coords[0]+str(int(coords[1])-1), new_position]



class Knight(ChessPiece):
    def __init__ (self, position, color):
        super().__init__(position, color)

    def get_physically_legal_destinations(self, board):
        coords = self.get_coordinates()
        coords = string2int_coordinates(coords)
        physically_legal_destinations = []
        for i in [-2,-1,1,2]:
            for j in [-2,-1,1,2]:
                if np.abs(i) + np.abs(j) ==3:
                    x = coords[0] + i
                    y = coords[1] + j
                    if 0<= x<8 and 0<=y<8:
                        physically_legal_destinations.append(letters[x]+str(y+1))
        return physically_legal_destinations


    def get_trajectory(self, new_position):
        # Knights have no trajectory, this function returns only the arrival square
        return [new_position]


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
