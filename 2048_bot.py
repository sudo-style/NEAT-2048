import numpy as np

# colorize the terminal
import colorama 
from colorama import Fore, Back, Style

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
    
    def slide_and_merge_row(self, row):
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
    
    def prev_board_same(self, prev_board):
        return np.array_equal(self.board, prev_board)
    
    def move_up(self):
        new_board = self.board.copy()
        
        # for every column in the board, slide and merge
        for c in range(SIZE):
            column = [new_board[r][c] for r in range(SIZE)]
            new_column = self.slide_and_merge_row(column)
            for r in range(SIZE):
                new_board[r][c] = new_column[r]
        return new_board
    
    def move_down(self):
        print('down')

    def move_left(self):
        print('left')

    def move_right(self):
        print('right')
    
    def move(self, direction):
        if direction == 'w':
            board = self.move_up()
        elif direction == 'a':
            board = self.move_left()
        elif direction == 's':
            board = self.move_down()
        elif direction == 'd':
            board = self.move_right()
        else: 
            print('invalid move')
            self.print_board()
            return
        if self.prev_board_same(board):
            print('invalid move')
            self.print_board()
        else:
            self.board = board
            self.add_new_tile()
            self.print_board()

def main():
    game = Game()
    game.print_board()

    while not game.isGameOver:
        move = input('next move: ')
        game.move(move)

if __name__ == '__main__':
    main()
