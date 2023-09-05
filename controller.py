from model import TicTacToeModel
from view import TicTacToeView

'''
This is the controller for the Tic Tac Toe game.
It handles the exchange of information between the
console (View) and gameboard (Model)
'''

game_view = TicTacToeView()

def start_game() -> None:
    game_model = TicTacToeModel()
    while game_model.winner == '':
        game_view.print_board(game_model.gameboard)
        invalid = True
        while invalid:
            coords = game_view.prompt_space(game_model.turn_player)
            status_code = game_model.mark_spot(coords[0], coords[1])

            switch={
                0:False,
                1:False,
                -1:True,
                -2:True
            }

            invalid = switch.get(status_code, True)
    
    print('Congradulations Player', game_model.winner, 'Won!\n')

def main():
    do_play = True
    while do_play:
        start_game()
        do_continue = input("\nDo you wish to play again? (y/n): ")
        do_player = do_continue == 'y'

if __name__ == "__main__":
    main()