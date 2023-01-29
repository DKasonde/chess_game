# import modules

import pygame
import os
from chess_game.chess import (
    Board,
    WIDTH,
    HEIGHT,
    WHITE,
    TILE_SIZE,
)

"""
Created on Fri Aug 20 18:06:50 2021

@author: kasonde
"""

"""
Chess game with graphics
"""

# Get file directory

sourceFileDir = os.path.dirname(os.path.abspath('main.py'))
# define the screen, framerate and other
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FRAMERATE = 60
pygame.display.set_caption("Chess")
Assets = os.path.join(sourceFileDir, 'chess_game' ,'Assests')


def get_square_under_mouse(board):
    x, y = pygame.mouse.get_pos()
    row = y // TILE_SIZE
    col = x // TILE_SIZE
    piece = board.get_piece(row, col)

    return piece, row, col


def draw_drag(board, selected_piece):
    row, col = None, None
    if selected_piece:
        piece, row, col = get_square_under_mouse(board)

    return row, col


def draw_window():
    screen.fill(WHITE)

    pygame.display.update()
    return


# place chess piece on board


# main game loop


def main():
    clock = pygame.time.Clock()
    run = True
    board = Board()
    draw_window()
    selected_piece = None

    while run:
        clock.tick(FRAMERATE)
        piece, row, col = get_square_under_mouse(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if piece != 0:
                    selected_piece = piece, row, col

            if event.type == pygame.MOUSEBUTTONUP:
                if (drop_position[0] is not None) & (drop_position[1] is not None):
                    piece, old_row, old_col = selected_piece
                    new_row, new_col = drop_position
                    board.move(piece, new_row, new_col)


                selected_piece = None
                drop_position = None

        board.draw(screen, selected_piece, pygame.mouse.get_pos())
        drop_position = draw_drag(board, selected_piece)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
