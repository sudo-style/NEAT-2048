# colorize the terminal
import colorama 
from colorama import Fore, Back, Style


import numpy as np

SIZE = 4

class Game:
    def __init__(self):
        self.board = np.zeros((SIZE, SIZE), dtype=int)
        self.add_new_tile()
        self.isGameOver = False

    def random_value(self):
        return np.random.choice([2, 4], p=[0.9, 0.1])

    def add_new_tile(self):
        empty_cells = [(r, c) for r in range(SIZE) for c in range(SIZE) if self.board[r][c] == 0]
        if len(empty_cells) > 0:
            r, c = empty_cells[np.random.randint(len(empty_cells))]
            self.board[r][c] = self.random_value()

    def print_board(self):
        print(self.board)

    def isGameOver(self):
        return self.isGameOver
    
    def move_up(self):
        print('up')

    def move_down(self):
        print('down')

    def move_left(self):
        print('left')

    def move_right(self):
        print('right')
    
    def move(self, direction):
        if direction == 'w':
            self.move_up()
        elif direction == 'a':
            self.move_left()
        elif direction == 's':
            self.move_down()
        elif direction == 'd':
            self.move_right()
        else: 
            print('invalid move')
            self.print_board()
            return
        self.add_new_tile()
        self.print_board()


'''def main():
    game = Game()
    game.print_board()

    while not game.isGameOver:
        move = input('next move: ')
        game.move(move)'''




def slide_and_merge_row(row):
    # get all non-zero values
    # [2, 4, 0, 2] -> [2, 4, 2]
    # [0, 0, 0, 2] -> [2]
    non_zero = [value for value in row if value != 0]
    
    # keep track of which values have been merged
    
    # [False, False, False] means no values have been merged
    # [True, False, False] means the first value has been merged
    merged = False
    
    new_row = []
    for i, value in enumerate(non_zero):
        # if the value has been merged, skip it
        if merged: 
            merged = False
            continue
        
        # if the current value is the same as the next value, merge them
        if i < len(non_zero) - 1 and value == non_zero[i + 1] and not merged:
            new_row.append(value * 2)
            merged = True
        
        # if not able to merge, just add the value
        else: new_row.append(value)

    # add zeros for the remaining empty cells
    # [2, 4, 2] -> [2, 4, 2, 0]
    # [2] -> [2, 0, 0, 0]
    new_row += [0] * (SIZE - len(new_row))
    return new_row

def main():
    test_case = []
    test_case.append([[0, 0, 0, 2], [2, 0, 0, 0]])
    test_case.append([[2, 0, 0, 2], [4, 0, 0, 0]])
    test_case.append([[2, 0, 2, 2], [4, 2, 0, 0]])
    test_case.append([[2, 2, 2, 2], [4, 4, 0, 0]])
    test_case.append([[2, 2, 2, 4], [4, 2, 4, 0]])

    for i, (input, expected) in enumerate(test_case):
        result = slide_and_merge_row(input)
        if result == expected:
            print(f'{Fore.GREEN}in: {input} out: {result} exp: {expected} case {i + 1} Passed')
        else:
            print(f'{Fore.RED  }in: {input} out: {result} {Fore.GREEN}exp: {expected}{Fore.RESET} {Fore.RED}case {i + 1} Failed')
        print(f'{Fore.RESET}')

if __name__ == '__main__':
    main()
