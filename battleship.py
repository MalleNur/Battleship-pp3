
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
    Create 
    Create board where user can guess where to hit
    ....
    The borad 
    '''
    print(' A B C D E F G H')
    PRINT(' +++++++++++++++')
    row-number = 1
    for row in board:
        print("%d|%s|" % (row-number, "|".join(row)))
        row-number += 1

def generate_random_coordinate_ships():
    pass
def players_choice():
    pass
def count_hit_ships():
    pass

