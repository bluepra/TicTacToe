import random


class Engine():
    def __init__(self, board, player_piece, ai_piece):
        self.board = board
        self.player_piece = player_piece
        self.ai_piece = ai_piece

    # Prints this engine's board
    def print_board(self):
        for row in self.board:
            print(row)

    # Places a given piece on this engines board
    def place_piece(self, piece: str, position):
        i, j = position
        # If spot is not empty, throw exception
        if (self.board[i][j] != ' '):
            raise Exception(f'{position} is occupied')
        else:
            self.board[i][j] = piece

    # Checks the user's requested input for validity.
    # Returns true if spot is valid and empty, False otherwise
    def check_user_input(self, pos):
        i, j = pos
        valid_pos = False
        # Check if coords are within board's bounds
        if (i >= 0 and i < len(self.board) and j >= 0 and j < len(self.board)):
            # Check if coords point to an empty spot
            if (self.board[i][j] == ' '):
                valid_pos = True
            else:
                print(f'Spot {i},{j} is occupied.')
        else:
            print('The position you entered is out of bounds.')

        return valid_pos

    # Gets the user's choice
    def get_user_input(self):
        valid_pos = False

        # Keeps looping till the user enters a valid pos
        while (not valid_pos):
            pos = input('Enter a position, ex: 0,2: ')
            i, j = pos.split(',')
            i = int(i)
            j = int(j)

            if (self.check_user_input((i, j))):
                valid_pos = True

        return (i, j)

    # AI randomly choose a empty spot
    def ai_move(self):
        invalid_position = True
        i = random.randint(0, len(self.board) - 1)
        j = random.randint(0, len(self.board) - 1)
        while (self.board[i][j] != ' '):
            i = random.randint(0, len(self.board) - 1)
            j = random.randint(0, len(self.board) - 1)

        return (i, j)

    # If piece won, return True
    # If piece is has not won, return False
    def check_win(self, piece):
        # Horizontal check
        for row in self.board:
            if row[0] != ' ' and row[0] == piece and row[1] == piece and row[2] == piece:
                return True

        # Vertical check
        for col in range(len(self.board)):
            if self.board[0][col] == piece and self.board[1][col] == piece and self.board[2][col] == piece:
                return True

        # Diagonal check /
        if self.board[0][0] == piece and self.board[1][1] == piece and self.board[2][2] == piece:
            return True

        # Diagonal check \
        if self.board[2][0] == piece and self.board[1][1] == piece and self.board[0][2] == piece:
            return True


def main():
    # Standard 3x3 board
    board_width = 3
    board = [[' ' for j in range(3)] for i in range(3)]

    pieces = ['X', 'O']

    # Randomly selects pieces for the player and AI
    player_piece = random.choice(pieces)

    if player_piece == pieces[0]:
        ai_piece = pieces[1]
    else:
        ai_piece = pieces[0]

    # ---------------------------------------------------------------------------------------------

    game_over = False
    engine = Engine(board, player_piece, ai_piece)

    print('You are the', player_piece, 'player')
    print('The AI is the', ai_piece, 'player')
    engine.print_board()

    num = random.randint(0, 1)
    player_turn = False
    if pieces[num] == player_piece:
        player_turn = True

    # While game is not over, keep playing
    while not game_over:
        if player_turn:
            user_pos = engine.get_user_input()
            engine.place_piece(player_piece, user_pos)

            print('You placed a piece at', user_pos)
            engine.print_board()
            print('-' * 50)

            player_won = engine.check_win(player_piece)
            if (player_won):
                print('Congrats, you won!')
                game_over = True
        else:
            ai_pos = engine.ai_move()
            engine.place_piece(ai_piece, ai_pos)

            print('AI placed a piece at', ai_pos)
            engine.print_board()
            print('-' * 50)

            ai_won = engine.check_win(ai_piece)
            if (ai_won):
                print('The AI won!')
                game_over = True

        # Toggle player turn each time
        player_turn = not player_turn

    print('Game over!')


if __name__ == '__main__':
    main()
