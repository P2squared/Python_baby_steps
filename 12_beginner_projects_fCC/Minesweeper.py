import random
import re


class Board:

    def __init__(self, size, bombs):
        self.size = size  # using & tracking these parameters locally
        self.bombs = bombs

        # helper function
        self.board = self.make_new_board()  # creating a board, defined later
        self.values = self.assign_values()  # assign numbers to bomb nebors

        self.dug = set()  # using this set to record where we've already dug

    def make_new_board(self):

        # Using list of lists for a 2D database
        board = [[None for _ in range(self.size)] for _ in range(self.size)]

        # Planting bombs
        bombs_planted = 0
        while bombs_planted < self.bombs:
            loc = random.randint(0, self.size ** 2 - 1)
            row = loc // self.size
            col = loc % self.size

            if board[row][col] == '*':  # if bomb already planted in the random location
                continue  # keep going, don't increment bombs_planted, retry with randomised location

            board[row][col] = '*'  # assign * to randomised location & increment counter when bomb planted
            bombs_planted += 1
        return board

    def assign_values(self):  # assign numbers to boxes next to bombs

        for r in range(self.size):
            for c in range(self.size):  # move across the board
                if self.board[r][c] == '*':  # if bomb, skip
                    continue
                self.board[r][c] = self.get_num_neboring(r, c)  # else assign number if applicable

    def get_num_neboring(self, row, col):  # find what number to assign
        # iterate for the 8 squares that are next to any square
        # add no. of bombs in those 8 squares and assign that number

        num_neboring_bombs = 0

        for r in range(max(row - 1, 0), min(self.size - 1, row + 1) + 1):
            for c in range(max(col - 1, 0), min(self.size - 1, col + 1) + 1):
                if r == row and c == col:
                    continue  # skip if checking the actual current square
                if self.board[r][c] == '*':
                    num_neboring_bombs += 1

        return num_neboring_bombs

    def dig(self, row, col):  # dig in this location, return False if bomb

        # case1 : hit bomb = GO
        # case2 : hit number = finish dig and ask for next dig
        # case3 : hit blank = continue digging into nebors until bomb

        self.dug.add((row, col))  # tracking locations that are already dug
        # double bracket in the above because add takes 1 argument only so we pass row+col as tuple

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        else:
            for r in range(max(row - 1, 0), min(self.size - 1, row + 1) + 1):
                for c in range(max(col - 1, 0), min(self.size - 1, col + 1) + 1):
                    if (r, c) in self.dug:
                        continue
                    self.dig(r, c)

        return True

    def __str__(self):  # What part of the board to show to the user

        # initially set nothing visible
        vis_board = [[None for _ in range(self.size)] for _ in range(self.size)]
        for row in range(self.size):
            for col in range(self.size):
                if (row, col) in self.dug:
                    vis_board[row][col] = str(self.board[row][col])
                else:
                    vis_board[row][col] = ' '

        # putting this together into a string
        string_rep = ''
        widths = []

        for idx in range(self.size):
            columns = map(lambda x: x[idx], vis_board)
            widths.append(
                len(
                    max(columns, key=len)
                )
            )

        # print table of strings
        indices = [i for i in range(self.size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(vis_board)):
            row = vis_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += '  '.join(cells)
            string_rep += '  \n'

        str_len = int(len(string_rep) / self.size)
        string_rep = indices_row + '-' * str_len + '\n' + string_rep + '-' * str_len

        return string_rep


def play(size=10, bombs=10):
    # step1 : Create board with bombs planted & numbers
    board = Board(size, bombs)
    # This initialises the board, plants the bombs and assigns numbers

    # step2 : Show board to user and ask where to dig

    # step3 : If bomb, game over
    # If not a bomb, dig recursively till each square is next to a bomb

    # step4 : Repeat 2 & 3 till no places left to dig = win
    while len(board.dug) < board.size ** 2 - bombs:
        print(board)
        user = re.split(',(\\s)*', input("Where to dig ? input as row,col: "))
        row, col = int(user[0]), int(user[-1])

        if row < 0 or row >= board.size or col < 0 or col >= size:
            print("Invalid location, try again :)")
            continue

        # if valid input, dig
        safe = board.dig(row, col)  # this repeats until bomb hit or digging complete

        if not safe:
            break  # hit a bomb rip

    if safe:  # if no bombs during entire digging
        print("Congrats, you won")
    else:
        print("BOOM! Game over ")
    board.dug = [(r, c) for r in range(board.size) for c in range(board.size)]  # dig the entire thing to show it
    print(board)


if __name__ == '__main__':  # boiler plate, good practice
    play()
