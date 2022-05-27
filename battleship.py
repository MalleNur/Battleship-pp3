
# Explanation
# Y for placing ship and hit battleship
# ' ' for available space
# 'O' for missed shot

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
    for ship in range(10)
    ship_row, ship_column = randint(0,7), randint(0,7)
    while board [ship_row][ship_column] == 'Y':
        ship_row, ship_column = randint(0,7), randint(0,7)
    board[ship_row][ship_column] = 'Y'
    
def players_choice():
    pass
def count_hit_ships():
    pass

