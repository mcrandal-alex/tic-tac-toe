'''
Model that stores information about the game of tic-tac-toe, and
provides functionality to the game.
'''

class TicTacToeModel():

    def __init__(self) -> None:
        '''Construct a gameboard object'''
        self.gameboard = [ ['-', '-', '-'],
                          ['-', '-', '-'],
                          ['-', '-', '-']]
        self.board_size = len(self.gameboard)
        self.markers = ['X', 'O']
        self.markers_length = len(self.markers)
        self.marker_index = 0
        self.winner = ''
    
    def mark_spot(self, x: int, y: int) -> int:
        '''Have the player mark a spot on the grid, then have the game check for win
           Preconditions: x and y are inside grid boundries and target spot is open
           Returns: Exit status of play: 0 = ok, -1 = space occupied, -2 = out of bounds'''
        if x >= self.board_size or y >= self.board_size:
            return -2
        
        if self.gameboard[x][y] != '-':
            return -1
        
        self.gameboard[x][y] = self.turn_player[self.marker_index]
        self.marker_index = (self.marker_index + 1) % self.markers_length

        self.winner = self.check_win()
    
    def check_win(self, x: int, y: int) -> str:
        '''Exhaustive search the game board for a winner
           Returns: The character token for the player that won, otherwise the empty string'''
        for i in range(self.board_size):
            if self.gameboard[i][0] == self.gameboard[i][1] == self.gameboard[i][2]:
                return self.gameboard[i][0]
        
        for i in range(self.board_size):
            if self.gameboard[0][i] == self.gameboard[1][i] == self.gameboard[2][i]:
                return self.gameboard[0][i]
            
        if self.gameboard[0][0] == self.gameboard[1][1] == self.gameboard[2][2]:
            return self.gameboard[0][0]
        
        if self.gameboard[0][2] == self.gameboard[1][1] == self.gameboard[2][0]:
            return self.gameboard[0][0]
        
        return ''