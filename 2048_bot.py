import numpy as np

SIZE = 4

class Game:
    def __init__(self):
        self.board = np.zeros((SIZE, SIZE), dtype=int)
        self.add_new_tile()

    def random_value(self):
        return np.random.choice([2, 4], p=[0.9, 0.1])

    def add_new_tile(self):
        empty_cells = [(r, c) for r in range(SIZE) for c in range(SIZE) if self.board[r][c] == 0]
        if len(empty_cells) > 0:
            r, c = empty_cells[np.random.randint(len(empty_cells))]
            self.board[r][c] = self.random_value()

    def print_board(self):
        print(self.board)

def main():
    game = Game()
    game.print_board()

if __name__ == '__main__':
    main()