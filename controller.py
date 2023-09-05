from model import TicTacToeModel

'''
This is the controller for the Tic Tac Toe game.
It handles the exchange of information between the
console (View) and gameboard (Model)
'''

def start_game() -> None:
    game = TicTacToeModel()
    while game.winner == '':
        # TODO: print board
        # TODO: prompt for spot to mark
        # TODO: mark grid space
    
    # TODO: Congradulate winner

def main():
    do_play = True
    while do_play:
        start_game()
        do_continue = input("\nDo you wish to play again? (y/n): ")
        do_player = do_continue == 'y'

if __name__ == "__main__":
    main()