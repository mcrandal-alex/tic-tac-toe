'''
Input and Output handler for a game of tic tac toe
'''

class TicTacToeView():

    def print_board(self, gameboard) -> None:
        '''Display the gameboard to the user'''
        print_len = len(gameboard)
        print(' \t1\t2\t3')
        for i in range(print_len):
            print(i + 1, end='\t')
            for j in range(print_len):
                print(gameboard[i][j], end='\t')
            print('\n')
    
    def prompt_space(self, player_id: int):
        '''Prompt and input check the space the player wishes to mark'''
        invalid_input = True
        str_coords = []
        while invalid_input:
            raw_input = input('Enter a grid cell to mark Player ' + str(player_id) + ' ( ex 1,2 ): ')
            str_coords = raw_input.split(',')
            if len(str_coords) == 2:
                invalid_input = False
        
        for i in range(len(str_coords)):
            str_coords[i] = str_coords[i].strip()
        
        int_coords = []
        for str_coord in str_coords:
            int_coords.append(int(str_coord))
        
        return int_coords