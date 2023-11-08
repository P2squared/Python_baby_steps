import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandPC(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self, game): #returns location for move
        sqr = random.choice(game.avail_moves())
        return sqr

class HumPlay(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self, game): #returns location for move
        valid_sqr = False
        val = None
        while not valid_sqr:
            sqr = input(self.letter+'\'s turn! Input move (0-8) :')
            try:
                val = int(sqr)
                if val not in game.avail_moves():
                    raise ValueError
                valid_sqr = True
            except ValueError:
                print('Invalid square. Try again.')

        return val
