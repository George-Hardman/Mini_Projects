This is a basic project in python to program Conway's Game of Life, a iterative grid based game where cells on a board either live 
or die based on a set of rules (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

generate_tables(no_of_iterations, m, n) prints a series of iterations of a grid, where no_of_iterations is the number of
times that the code is iterated, m and n are the table dimentions.

analyse_cell_density(no_of_iterations, m, n) also iterates a specified number of times, as before but instead of printing out tables,
it calculated the fraction of living cells in each table, and plots these against iteration number, producing a complex graph.

Packages required for this code are Numpy and Matplotlib.

Test