import random

# Standard 3x3 board
board_width = 3
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

pieces = ['X', 'O']

# Randomly selects pieces
player_piece = random.choice(pieces)

if player_piece == pieces[0]:
    ai_piece = pieces[1]
else:
    ai_piece = pieces[0]

# ---------------------------------------------------------------------------------------------

class Engine():
    def __init__(self, board, player_piece, ai_piece):
        self.board = board
        self.player_piece = player_piece
        self.ai_piece = ai_piece

    def print_board(self):
        for row in self.board:
            print(row)

    def place_piece(self, piece: str, position):
        i,j = position
        # If spot is not empty, throw exception
        if (self.board[i][j] != ' '):
            raise Exception(f'{position} is occupied')
        else:
            self.board[i][j] = piece

    # Gets the user's choice
    def get_user_input(self):
        valid_pos = True

        pos = input('Enter a position, ex: 2,3: ')
        i,j = pos.split(',')
        i = int(i)
        j = int(j)

        if(i < 0 or i >= len(self.board) or j < 0 or j >= len(self.board)):
            valid_pos = False
        
        while(not valid_pos):
            print('That position is occupied')
            pos = input('Enter a position, ex: 2,3: ')
            i,j = pos.split(',')
            i = int(i)
            j = int(j)

            if(i >= 0 and i < len(self.board) and j >= 0 and j < len(self.board)):
                valid_pos = True

        return (i,j)

    # AI randomly choose a empty spot
    def ai_move(self):
        invalid_position = True
        i = random.randint(0, len(self.board) - 1)
        j = random.randint(0, len(self.board) - 1)
        while(self.board[i][j] != ' '):
            i = random.randint(0, len(self.board) - 1)
            j = random.randint(0, len(self.board) - 1)

        return (i,j)

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

game_over = False
engine = Engine(board, player_piece, ai_piece)

print('You are the', player_piece, 'player')
print('The AI is the', ai_piece, 'player')
engine.print_board()

num = random.randint(0,1)
player_turn = False
if pieces[num] == player_piece:
    player_turn = True

# While game is not over, keep playing
while(not game_over):
    if player_turn:
        user_pos = engine.get_user_input()
        engine.place_piece(player_piece, user_pos)

        print('You placed a piece at', user_pos)
        engine.print_board()
        print('-' * 50)

        player_won = engine.check_win(player_piece)
        if(player_won):
            print('Congrats, you won!')
            game_over = True
    else:
        ai_pos = engine.ai_move()
        engine.place_piece(ai_piece, ai_pos)

        print('AI placed a piece at', ai_pos)
        engine.print_board()
        print('-' * 50)
        
        ai_won = engine.check_win(ai_piece)
        if(ai_won):
            print('The AI won!')
            game_over = True

    # Toggle player turn each time
    player_turn = not player_turn

print('Game over!')
