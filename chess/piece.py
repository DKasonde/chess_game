from chess_game.chess.constants import (
    WHITE,
    BLACK,
    TILE_SIZE,
)
import os
import pygame
from typing import Union, Optional, Tuple, List

sourceFileDir = os.path.dirname(os.path.abspath('main.py'))
Assets = os.path.join(sourceFileDir,'chess_game' ,'Assests')


class Piece:
    def __init__(self, row: int, col: int, colour: Tuple[int, int, int]):
        self.row = row
        self.col = col
        self.colour = colour
        self.selected = False
        self.x = 0
        self.y = 0
        self.name = ""
        self.calculate_position()

    def calculate_position(self):
        self.x = TILE_SIZE * self.col
        self.y = TILE_SIZE * self.row

    def __repr__(self):
        if self.colour == WHITE:
            str_colour = "White"
        else:
            str_colour = "Black"
        return str(str_colour + self.name)

    def draw(self, screen: Union[pygame.Surface, pygame.SurfaceType], position: Optional[Tuple[int, int]]=None):
        if self.colour == WHITE:
            str_colour = "White"
        else:
            str_colour = "Black"
        piece_image = str_colour+self.name+ '.png'
        location = os.path.join(Assets, piece_image)
        image = pygame.image.load(location).convert_alpha()
        image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        if position is not None:
            screen.blit(image, (position[0] - TILE_SIZE/2, position[1] - TILE_SIZE/2))
        else:
            screen.blit(image, (self.x, self.y))

    def move(self, row: int, col: int):
        self.row = row
        self.col = col
        self.calculate_position()

    def is_valid_move(self, row: int, col: int, board: List[List[int]]):

        return True


class King(Piece):
    def __init__(self, row: int, col: int, colour: Tuple[int, int, int]):
        super().__init__(row, col, colour)
        self.name = "King"

    def is_valid_move(self, row: int, col: int, board: List[List[int]]):

        if (row not in [x for x in range(8)]) or (col not in [x for x in range(8)]):
            return False
        if ((abs(row - self.row) > 1) or (abs(col - self.col) > 1)):
            return False
        if board[row][col] != 0:
            return False
        return True


class Queen(Piece):
    def __init__(self, row: int, col: int, colour: Tuple[int, int, int]):
        super().__init__(row, col, colour)
        self.name = "Queen"

    def is_valid_move(self, row: int, col: int, board: List[List[int]]):

        if (row not in [x for x in range(8)]) or (col not in [x for x in range(8)]):
            return False

        if ((abs(row - self.row)==abs(col - self.col)) or (abs(row - self.row) == 0) or (abs(col - self.col) == 0) ):
            return False
        if board[row][col] != 0:
            return False
        return True


class Rook(Piece):
    def __init__(self, row: int, col: int, colour: Tuple[int, int, int]):
        super().__init__(row, col, colour)
        self.name = "Rook"


class Knight(Piece):
    def __init__(self, row: int, col: int, colour: Tuple[int, int, int]):
        super().__init__(row, col, colour)
        self.name = "Knight"


class Bishop(Piece):
    def __init__(self, row: int, col: int, colour: Tuple[int, int, int]):
        super().__init__(row, col, colour)
        self.name = "Bishop"


class Pawn(Piece):
    def __init__(self, row: int, col: int, colour: Tuple[int, int, int]):
        super().__init__(row, col, colour)
        self.name = "Pawn"
        if self.colour == WHITE:
            self.direction = 1
        else:
            self.direction = -1


def put_piece(string: str, row: int, col: int):

    if string.isupper():
        colour = BLACK
    else:
        colour = WHITE
    if string.lower() == "b":
        return Bishop(row, col, colour)
    elif string.lower() == "n":
        return Knight(row, col, colour)
    elif string.lower() == "k":
        return King(row, col, colour)
    elif string.lower() == "p":
        return Pawn(row, col, colour)
    elif string.lower() == "q":
        return Queen(row, col, colour)
    else:
        return Rook(row, col, colour)
