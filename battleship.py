
# Explanation
# Y for placing ship and hit battleship
# ' ' for available space
# '0' for missed shot

import time
from os import system
from random import randint
from rich.console import Console

console = Console()

HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
GUESS_BOARD = [[' '] * 8 for x in range(8)]

LETTER_TO_NUMBERS = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
}

def print_board(board):
    
    '''
    Create board where user can guess where to hit
    '''
    console.print('  A B C D E F G H', style="bold #900C3F")
    console.print('  +++++++++++++++', style="#ADD8E6")
    row_number = 1
    for row in board:
        console.print("%d|%s|" % (row_number, "|".join(row)), style="#900C3F")
        row_number += 1

def place_ships_randomly():
    '''
    Generate random ships for player to locate
    '''
    global HIDDEN_BOARD
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
    while HIDDEN_BOARD[ship_row][ship_column] == 'Y':
        ship_row, ship_column = randint(0, 7), randint(0, 7)
    HIDDEN_BOARD[ship_row][ship_column] = 'Y'

def players_choice():
    '''
    Ask player to choose row and column to hit a ship
    '''
    row = input('\nChoose a ship row 1-8: ').strip()
    while row not in '12345678' or row == "":
        print('Please enter a valid row ')
        row = input('Choose a ship row 1-8: ') 
    column = input('Choose a ship column A-H: ').upper().strip()
    while column not in 'ABCDEFGH' or column == "":
        print('Please enter a valid column ')
        column = input('Choose a ship column A-H: ').upper().strip() 
    return (int(row) - 1, LETTER_TO_NUMBERS[column])

def count_hit_ships(board):
    '''
    Count everytime the player make a hit in order to win the game.
    If the player makes 5 hits, the game is over and the player have won.
    '''
    count = 0
    for row in board:
        for column in row:
            if column == 'Y':
                count += 1
    return count

def restart_game():
    """
    Restarts the game
    """
    system('clear')
    run_game()
    players_choice('clear')
    print_board('clear')
    
    
    

    

def ask_to_play_again():
    """
    Asks the player at the end of the game if they want to
    play again or quit the game completely
    """
    answer = input('\nDo you want to restart ? Yes or No: ')
    if answer == "Yes":
        restart_game()
    elif answer == "No":
       console.print("\nThanks for playing!", style="bold white")
       time.sleep(5)
       system('clear')
    else:
        ask_to_play_again()

    
def run_game():
    place_ships_randomly()
    turns = 10
    while turns > 0:
        system('clear')
        console.print('Welcome to Battleship\n', style="bold underline #ADD8E6")
        print("Rules:\n\n- Choose coordinate from 1-8 and A-H to hit your opponents ships.\n \n- If you hit the 5 ships, you have won the game.\n \nGood Luck!\n" )
        print_board(GUESS_BOARD)
        (row, column) = players_choice()
        if GUESS_BOARD[row][column] == '0':
            console.print('\nYou have already guessed that. ', style="bold white")
        elif HIDDEN_BOARD[row][column] == 'X':
            console.print('\nClear shot! The battleship sank. ', style="bold white")
            GUESS_BOARD[row][column] = 'Y'
            turns -= 1
        else:
            console.print('\nUnfortunately, you missed! ', style="bold white")
            GUESS_BOARD[row][column] = '0'
            turns -= 1
        if count_hit_ships(GUESS_BOARD) == 5:
            console.print("\nWe've won!, Nicely done. GAME OVER ", style="bold white")
            break
        console.print('\nYou have ' + str(turns) + ' turns remaining ', style="bold white")
        if turns == 0:
            console.print('\nSorry, you ran out of turns. Better luck next time! \n', style="bold white")
            ask_to_play_again()
            break
        time.sleep(2)
        

if __name__ == "__main__":
    run_game()
    

