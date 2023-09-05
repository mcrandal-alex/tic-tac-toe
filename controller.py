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
    while game_model.winner == -1:
        game_view.print_board(game_model.gameboard)
        invalid = True
        while invalid:
            coords = game_view.prompt_space(game_model.turn_player)
            for i in range(len(coords)):
                coords[i] -= 1
            status_code = game_model.mark_spot(coords[0], coords[1])

            switch={
                0:False,
                -1:True,
                -2:True
            }

            invalid = switch.get(status_code, True)
    
    game_view.print_board(game_model.gameboard)

    if game_model.winner > 0:
        print('Congradulations Player', game_model.winner, 'Won!\n')
    else:
        print('Game ended in a draw...\n')

def main():
    do_play = True
    while do_play:
        start_game()
        do_continue = input("\nDo you wish to play again? (y/n): ")
        do_play = do_continue == 'y'

if __name__ == "__main__":
    main()