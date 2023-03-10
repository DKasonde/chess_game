from chess_game.chess.constants import (
    config,
)
from chess_game.chess.board import Board
from chess_game.chess.piece import (
    Piece,
)
import pygame
from typing import Union, Optional, Tuple


class Game:
    def __init__(
        self,
        screen: Union[pygame.Surface, pygame.SurfaceType],
        cfg: Optional[str] = None,
    ):
        self.piece_grabbed = None
        self.selected_piece = None
        self.screen = screen
        if cfg is None:
            self.cfg = config
        else:
            self.cfg = cfg
        self.board = Board(self.cfg)
        self.board.create_board()

    def _init(self):
        self.selected_piece = None
        self.piece_grabbed = False
        self.board = Board(self.cfg)
        self.board.create_board()

    def reset(self):
        self._init()

    def select(self, piece: Piece, row: int, col: int):
        if self.selected_piece is not None:
            if piece == self.selected_piece[0]:
                self.selected_piece = None
                return

        if piece != 0:
            self.selected_piece = piece, row, col
            self.piece_grabbed = True
        return

    def move(self, new_position: Tuple[int, int]):

        if self.selected_piece is not None:
            self.piece_grabbed = False

        if (new_position[0] is not None) & (new_position[1] is not None):
            piece, old_row, old_col = self.selected_piece
            new_row, new_col = new_position
            self.board.move(piece, new_row, new_col)
            self.selected_piece = None

        return

    def draw(self, mouse_position):
        if self.piece_grabbed:
            self.board.draw_piece(self.screen, self.selected_piece, mouse_position)
        else:
            self.board.draw_piece(self.screen, self.selected_piece)
