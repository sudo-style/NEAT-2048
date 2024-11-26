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
        self.moves = 0

    def random_value(self):
        return np.random.choice([1, 2], p=[0.9, 0.1])

    def add_new_tile(self):
        # get all empty cells
        empty_cells = [(r, c) for r in range(SIZE) for c in range(SIZE) if self.board[r][c] == 0]
        if len(empty_cells) > 0:
            # randomly choose an empty cell
            r, c = empty_cells[np.random.randint(len(empty_cells))]
            self.board[r][c] = self.random_value()

    def print_board(self):
        print(2**self.board)

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
                new_row.append(value + 1)
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

    def slide_and_merge(self, direction):
        board = self.board.copy()
        
        if direction in ('LEFT', 'RIGHT'):
            for r in range(SIZE):
                row = board[r]
                if direction == 'RIGHT':
                    row = row[::-1]
                new_row = self.slide_and_merge_row(row)
                if direction == 'RIGHT':
                    new_row.reverse()
                board[r] = new_row
        elif direction in ('UP', 'DOWN'):
            for c in range(SIZE):
                column = [board[r][c] for r in range(SIZE)]
                if direction == 'DOWN':
                    # reverse the column
                    column = column[::-1]
                new_column = self.slide_and_merge_row(column)
                if direction == 'DOWN':
                    new_column.reverse()
                for r in range(SIZE):
                    board[r][c] = new_column[r]
        return board
            
    def move(self, direction):
        if direction not in ('UP', 'DOWN', 'LEFT', 'RIGHT'):
            print('invalid move')
            self.print_board()
            return

        board = self.slide_and_merge(direction)
    
        if self.prev_board_same(board):
            print('invalid move')
            self.print_board()
        else:
            self.board = board
            self.add_new_tile()
            self.print_board()
            self.moves += 1 # this will determine the fitness of the bot

    def setBoard(self, board):
        self.board = board

def main():
    game = Game()
    game.print_board()

    directions = {'w': 'UP', 'a': 'LEFT', 's': 'DOWN', 'd': 'RIGHT'}

    while not game.isGameOver:
        move = input('next move: ')
        while move not in directions:
            game.print_board()
            move = input('try again: ')
            

        direction = directions[move]
        game.move(direction)

if __name__ == '__main__':
    main()
