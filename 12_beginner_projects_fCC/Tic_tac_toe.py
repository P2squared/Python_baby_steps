import math
import time
from Tic_tac_toe_player import HumPlay, RandPC

class TicTacToe: #all game functions
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None

    def print_board(self): #prints board with the live contents in squares
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row)+' |')

    @staticmethod
    def print_board_nums(): #prints board with numbers assigned to squares
        num_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in num_board:
            print('| '+' | '.join(row)+' |')

    def avail_moves(self): #list of all squares that are blank
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_sqrs(self): #whether its true/false that there are empty squares
        return ' ' in self.board

    def num_empty_sqrs(self): #number of empty squares
        return self.board.count(' ')

    def make_move(self, sqr, letter): #runs action from any player and checks for victory
        if self.board[sqr] == ' ':
            self.board[sqr] = letter
            if self.win(sqr, letter):
                self.winner = letter
            return True
        else: return False

    def win(self, sqr, letter): #checks if there's victory
        row_ind = sqr //3 #find which row the last move was made in
        row = self.board[row_ind*3: (row_ind + 1)*3] #find content of all sqrs in that row
        if all([spot == letter for spot in row]) :# if every sqr in the row is the player letter
            print('Winner by row')
            return True

        col_ind = sqr%3 #find column the last move was made in
        col = [self.board[col_ind+i*3] for i in range(3)] #find content of all sqrs in that column
        if all([spot == letter for spot in col]) :# if every sqr in the column is the player letter
            print('Winner by column')
            return True

        if sqr % 2 == 0 :# if sqr is one of the corners or center square of the board (prerequisite for diagonal victory)
            diagonal1 = [self.board[i] for i in [0,8,4]] #find content in left upper to right lower diagonal
            if all([spot == letter for spot in diagonal1]):
                print('Winner by diagonal1')
                return True
            diagonal2 = [self.board[i] for i in [6, 2, 4]]  # find content in left lower to right upper diagonal
            if all([spot == letter for spot in diagonal2]):
                print('Winner by doaginal2')
                return True

        #print('No winner yet')
        return False


def play(game, Xplayr, Oplayr, print_game=True) :#initiates & runs the entire thing
    if print_game == True:
        game.print_board_nums()

    letter = 'X'

    while game.empty_sqrs(): # run as long as board is incomplete
        if letter =='O' :
            sqr = Oplayr.get_move(game) #runs player code from other file
        else:
            sqr = Xplayr.get_move(game)

        if game.make_move(sqr, letter): #if made move is legit
            if print_game:
                print(letter + f' player makes move at square {sqr}')
                game.print_board() # runs print_board(), prints current board progress
                print('') # add empty line

            if game.winner: #if there's currently a winner
                if print_game: #if printing the game progress
                    print(letter+' wins!')
                return letter #return letter that won

            print('No winner yet')
            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print('It\'s a tie')

if __name__ == '__main__':
    Xplayr = HumPlay('X')
    Oplayr = RandPC('Y')
    t = TicTacToe()
    play(t, Xplayr, Oplayr, print_game=True)
