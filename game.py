import random
import copy


# Bot uses the minimax algorithm.
# The AI is the maximizing player. The human is the minimizing player.
class AI:
    def __init__(self, ai_board, ai_piece, opp_piece):
        self.board = ai_board  # This is the AI's current board
        self.piece = ai_piece
        self.opp_piece = opp_piece

    # Returns the empty positions for a given board
    def get_empty_spots(self, board):
        empty_spots = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ' ':
                    empty_spots.append((i, j))

        return empty_spots

    # Given a current board and the next player to play, this function
    # returns list of tuples containing successor boards and their respective positions
    def succ(self, current_board, next_player_piece):
        empty_spots = self.get_empty_spots(current_board)
        successors = []

        # Generate successor boards
        for spot in empty_spots:
            i, j = spot
            new_board = copy.deepcopy(current_board)
            new_board[i][j] = next_player_piece
            successors.append((new_board, spot))

        return successors

    # If piece won on the passed in board, return True
    # If piece is has not won, return False
    def check_win(self, board, piece):
        piece_won = False

        # Horizontal check
        for row in board:
            if row[0] != ' ' and row[0] == piece and row[1] == piece and row[2] == piece:
                piece_won = True

        # Vertical check
        for col in range(len(board)):
            if board[0][col] == piece and board[1][col] == piece and board[2][col] == piece:
                piece_won = True

        # Diagonal check /
        if board[0][0] == piece and board[1][1] == piece and board[2][2] == piece:
            piece_won = True

        # Diagonal check \
        if board[2][0] == piece and board[1][1] == piece and board[0][2] == piece:
            piece_won = True

        return piece_won

    def get_board_value(self, board, piece):
        board_value = 0
        # Horizontal counts
        max_h_val = 0
        for row in board:
            cur_h_val = row.count(piece)
            if cur_h_val > max_h_val:
                max_h_val = cur_h_val

        # Vertical counts
        transposed_board = list(map(list, zip(*board)))
        max_v_val = 0
        for row in transposed_board:
            cur_v_val = row.count(piece)
            if cur_v_val > max_v_val:
                max_v_val = cur_v_val

        # / Diagonal counts
        # \ Diagonal counts
        return board_value

    # Given a board and piece, this function returns a number
    # based on how good or bad the current board is.
    def game_state(self, board, piece):
        # If the board is a winning board, return 1 or -1 based on piece
        if self.check_win(board, piece):
            if piece == self.opp_piece:
                return -1
            else:
                return 1

        # If not winning board, calculate board value
        board_value = self.get_board_value(board, piece)

        if piece == self.opp_piece:
            return board_value * -1

        return board_value


class Engine:
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
    board_width = 3
    num_dashes = 50
    board = [[' ' for j in range(board_width)] for i in range(board_width)]

    pieces = ['X', 'O']

    # Randomly selects pieces for the player and AI
    player_piece = random.choice(pieces)
    ai_piece = pieces[1] if player_piece == pieces[0] else pieces[0]

    # ---------------------------------------------------------------------------------------------

    game_over = False
    engine = Engine(board, player_piece, ai_piece)
    ai = AI(board, ai_piece, player_piece)  # The AI object that will play against human player

    print('WELCOME TO AI TIC TAC TOE')
    print('-' * num_dashes)
    print('You are the', player_piece, 'player')
    print('The AI is the', ai_piece, 'player')
    engine.print_board()
    print('-' * num_dashes)

    num = random.randint(0, 1)
    player_turn = True if pieces[num] == player_piece else False
    print('You play first move') if player_turn else print('AI moves first')

    # While game is not over, keep playing
    while not game_over:
        if player_turn:
            user_pos = engine.get_user_input()
            engine.place_piece(player_piece, user_pos)

            print('You placed a piece at', user_pos)
            engine.print_board()
            print('-' * num_dashes)

            player_won = engine.check_win(player_piece)
            if (player_won):
                print('Congrats, you won!')
                game_over = True
        else:
            ai_pos = engine.ai_move()
            engine.place_piece(ai_piece, ai_pos)

            print('AI placed a piece at', ai_pos)
            engine.print_board()
            print('-' * num_dashes)

            ai_won = engine.check_win(ai_piece)
            if (ai_won):
                print('The AI won!')
                game_over = True

        # Toggle player turn each time
        player_turn = not player_turn

    print('Game over!')


if __name__ == '__main__':
    main()
