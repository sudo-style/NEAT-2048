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

def main():
    game = Game()
    game.print_board()

    while not game.isGameOver:
        move = input('next move: ')
        game.move(move)

if __name__ == '__main__':
    main()