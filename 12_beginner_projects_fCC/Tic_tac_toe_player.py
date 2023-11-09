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

class GeniPC(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.avail_moves()) == 9:
            sqr = random.choice(game.avail_moves())
        else:
            sqr=self.minimax(game, self.letter)['position'] #only use position from best (position + score)
            #needs to be recursive so define outside
        return sqr

    def minimax(self, state, player): #state=current state of the game like a screenshot in time
        max_player = self.letter #not the Genius AI
        other_player = 'O' if player == 'X' else 'X'

        if state.winner == other_player: #check if previous move led to victory #
            return {'position': None,
                    'score': 1*(state.num_empty_sqrs() +1) if other_player == max_player #score should be maximised for other player (GeniPC)
                            else -1*(state.num_empty_sqrs()+1) #score should be minimised for human
                    }
        elif not state.empty_sqrs(): #no empty squares, so nobody won, so score=0
            return {'position' : None, 'score' : 0} #MiniMax returns the best position for the next move and the score for it

        if player == max_player:
            best = {'position' : None, 'score' : -math.inf} #initialise to negative infinity so that it'll raise when comparing with other score, ensuring making an update #best stores highest score and best position to move into. This has to be maximised every time
        else :
            best = {'position': None, 'score': math.inf} #should be minimised at every step so start with positive infinity

        for possible_move in state.avail_moves(): #explore details of the next possible move
            #make move, simulate & check impact of making that move, undo the move to come back to previous state of the game
            #update details in dictionary if simulated move is better than previously recorded move
            state.make_move(possible_move, player) #execute make_move for current state : assign letter, check winner

            sim_score = self.minimax(state, other_player) #go into recursion, switch players and calculate. Again go into recursion, inception style

            state.board[possible_move] = ' ' #undo data change from recursion
            state.winner = None #undo data change from recursion
            sim_score['position'] = possible_move #set simulated position to the move we evaluated in minimax

            if player == max_player:
                if sim_score['score'] > best['score']: # better outcome for max player
                    best = sim_score #best & sim_score both deal with move position & score for that move
            else:
                if sim_score['score'] < best['score']: #better outcome for min player
                    best = sim_score

        return best #minimax returns best position & the score
