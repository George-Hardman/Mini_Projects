import numpy as np
import matplotlib.pyplot as plt

np.random.seed()


class Board:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.grid = np.zeros((n, m), dtype=int)

    def __str__(self):
        return str(self.grid)

    def random_board(self):
        self.grid = np.random.randint(2, size=(self.n, self.m))

    def set_cell_value(self, value, i, j):
        if value == 0 or value == 1:
            self.grid[j-1][i-1] = value
        else:
            print(f"Invalid Input: Set_cell_value: {value}")
            pass

    def get_cell_value(self, i, j):
        value = 0
        if i > self.m or j > self.n or i < 1 or j < 1:
            pass
        else:
            value = self.grid[j-1][i-1]
        return value

    def sum_neighbour_values(self, i, j):
        get_cell_val = self.get_cell_value
        count = 0
        if i < 1 or j < 1 or i > self.m or j > self.n:
            print('Invalid Input B')
            pass

        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                count += get_cell_val(x, y)
        count = count - get_cell_val(i, j)
        return count

    def cell_next_step(self, i, j):
        next_value = 0
        current_value = self.get_cell_value(i, j)
        sum_neighbour_values = self.sum_neighbour_values(i, j)

        if current_value == 1:
            if (sum_neighbour_values == 2) or (sum_neighbour_values == 3):
                next_value = 1
            else:
                pass
        elif sum_neighbour_values == 3:
            next_value = 1
        else:
            pass
        return next_value

    def board_next_step(self):
        m = self.m
        n = self.n
        new_board = Board(m, n)

        for i in range(1, m+1):
            for j in range(1, n+1):
                next_val = self.cell_next_step(i, j)
                new_board.set_cell_value(next_val, i, j)
        self.grid = new_board.grid
        del new_board

    def num_of_living_cells(self):
        count = 0
        m = self.m
        n = self.n
        for i in range(1, m+1):
            for j in range(1, n+1):
                current_cell = self.get_cell_value(i, j)
                count += current_cell
        return count


def analyse_cell_density(no_of_iterations, m, n):
    board = Board(m, n)
    board.random_board()

    x = [i + 1 for i in range(no_of_iterations)]
    y = []
    cell_no = m * n

    for i in range(no_of_iterations):
        num_of_cells = board.num_of_living_cells()
        density = num_of_cells/cell_no
        y.append(density)
        board.board_next_step()

    plt.plot(x, y)
    plt.xlabel("No. of iterations")
    plt.ylabel("Cell Density")
    plt.show()


def generate_tables(no_of_iterations, m, n):
    board = Board(m, n)
    board.random_board()
    i = 1
    for i in range(no_of_iterations + 1):
        print("____________________________")
        print(f"Iteration number {i}\n")
        print(board)
        board.board_next_step()


generate_tables(5, 4, 4)

analyse_cell_density(400, 30, 30)
