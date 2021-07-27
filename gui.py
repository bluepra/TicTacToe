import pygame
import random
from game import *

pygame.init()

# Pygame setup
square_width = 100
img_width = 64
img_padding = (square_width - img_width) // 2

line_width = 5
screen_width = square_width * 3 + line_width * 2
screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption('Tic-Tac-Toe vs. AI Bot')

x_img = pygame.image.load('images/x.png')
o_img = pygame.image.load('images/o.png')
display_icon = pygame.image.load('images/display_icon.png')

pygame.display.set_icon(display_icon)

run = True
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game setup:
board = [[' ' for j in range(3)] for i in range(3)]
pieces = ['X', 'O']

# Randomly selects pieces for the player and AI
player_piece = random.choice(pieces)
ai_piece = pieces[1] if player_piece == pieces[0] else pieces[0]

# Select first turn
player_turn = True if pieces[random.randint(0, 1)] == player_piece else False

num_dashes = 50
game_over = False
ai = AI(copy.deepcopy(board), ai_piece, player_piece)  # The AI object that will play against human player
engine = Engine(copy.deepcopy(board), player_piece, ai)


def draw_board_lines(surface):
    # first horizontal line
    pygame.draw.rect(surface, BLACK, pygame.Rect(0, square_width, screen_width, line_width))
    # second horizontal line
    pygame.draw.rect(surface, BLACK, pygame.Rect(0, 2 * square_width + line_width, screen_width, line_width))
    # first vertical line
    pygame.draw.rect(surface, BLACK, pygame.Rect(square_width, 0, line_width, screen_width))
    # second vertical line
    pygame.draw.rect(surface, BLACK, pygame.Rect(2 * square_width + line_width, 0, line_width, screen_width))


def draw_board(surface, board):
    draw_board_lines(surface)

    # Draw the pieces
    for i in range(len(board)):
        for j in range(len(board[i])):
            x = j * (square_width + line_width) + img_padding
            y = i * (square_width + line_width) + img_padding
            if engine.board[i][j] == pieces[0]:
                screen.blit(x_img, (x, y))
            elif engine.board[i][j] == pieces[1]:
                screen.blit(o_img, (x, y))


def get_user_input(pos):
    j = pos[0] // square_width  # pos[0] is the x direction
    i = pos[1] // square_width  # pos[1] is the y direction
    return i, j


print('WELCOME TO AI TIC TAC TOE')
print('-' * num_dashes)
print('You are the', player_piece, 'player')
print('The AI is the', ai_piece, 'player')
print('You play first move') if player_turn else print('AI moves first')
print('-' * num_dashes)

while run:
    mouse_pos = None
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if player_turn:
                mouse_pos = pygame.mouse.get_pos()

    # --- Game Logic
    if not game_over:
        if player_turn:
            if mouse_pos is not None:
                user_pos = get_user_input(mouse_pos)
                engine.place_piece(player_piece, user_pos)
                ai.place_piece(player_piece, user_pos)

                # print('You placed a piece at', user_pos)
                # engine.print_board()
                # print('-' * num_dashes)

                # Tie check
                if engine.check_draw():
                    print('Tie game!')
                    game_over = True

                player_won = engine.check_win(player_piece)
                if player_won:
                    print('Congrats, you won!')
                    game_over = True
                player_turn = not player_turn
        else:
            ai_pos = engine.ai_move()
            engine.place_piece(ai_piece, ai_pos)
            ai.place_piece(ai_piece, ai_pos)

            # print('AI placed a piece at', ai_pos)
            # engine.print_board()
            # print('-' * num_dashes)

            # Tie check
            if engine.check_draw():
                print('Tie game!')
                game_over = True

            ai_won = engine.check_win(ai_piece)
            if ai_won:
                print('The AI won!')
                game_over = True
            player_turn = not player_turn

    # --- Draw the new game board
    screen.fill(WHITE)
    draw_board(screen, engine.board)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
