
# Explanation
# Y for placing ship and hit battleship
# ' ' for available space
# '0' for missed shot

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

def generate_random_coordinate_ships():
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
    count = 0
    for row in board:
        for column in row:
            if column == 'Y':
                count += 1
    return count
    

