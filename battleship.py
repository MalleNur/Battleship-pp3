
# Explanation
# Y for placing ship and hit battleship
# ' ' for available space
# '0' for missed shot

import time
from os import system
from random import randint

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
    print(' A B C D E F G H')
    print(' +++++++++++++++')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row-number, "|".join(row)))
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
    row = input('Choose a ship row 1-8: ').strip()
    while row not in '12345678':
        print('Please enter a valid row ')
        row = input('Choose a ship row 1-8: ')
    column = input('Choose a ship column A-H: ').upper().strip()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column ')
        column = input('Choose a ship column A-H: ').upper().strip()
    return int(row) - 1, LETTER_TO_NUMBERS[column]

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
    
    
def run_game():
    place_ships_randomly()
    turns = 10
    while turns > 0:
        system('clear')
        print('Welcome to Battleship')
        print_board(GUESS_BOARD)
        row, column = players_choice()
        if GUESS_BOARD[row][column] == '0':
            print('\n You have already guessed that. \n')
        elif HIDDEN_BOARD[row][column] == 'X':
            print('\n Clear shot! The battleship sank. \n')
            GUESS_BOARD[row][column] = 'Y'
            turns -= 1
        else:
            print('\n Unfortunately, you missed! \n')
            GUESS_BOARD[row][column] = '0'
            turns -= 1
        if count_hit_ships(GUESS_BOARD) == 5:
            print("\n We've won!, Nicely done. GAME OVER \n")
            break
        print('\n You have ' + str(turns) + 'turns remaining \n')
        if turns == 0:
            print('\n Sorry, you ran out of turns. Better luck next time! \n')
            break
        time.sleep(2)

if __name__ == "__main__":
    run_game()
    print("\n Thanks for playing! \n")