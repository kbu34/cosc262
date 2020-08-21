"""A broken implementation of a recursive search for the optimal path through
   a grid of weights.
   Richard Lobb, January 2019.
"""
from math import inf as INFINITY

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid


def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given grid of
       integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    row_count = 1
    col_count = 0
    
    def cell_cost(row_count, col_count):
        """The cost of getting to a given cell in the current grid."""
        while row_count < n_rows:
            if col_count >= n_cols:
                row_count += 1
                col_count = 0
            else:
                cost = grid[row_count][col_count]
                if row_count != 0:
                    values = []
                    for i in range(-1, 2):
                        if col_count + i > -1 and col_count + i < n_cols:
                            values.append(grid[row_count - 1][col_count + i])
                    cost += min(values)
                    grid[row_count][col_count] = cost
                col_count += 1
                
    cell_cost(row_count, col_count)
    new_list = [grid[n_rows-1][x] for x in range(n_cols)]
    return min(new_list)
    
    
def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))

print(file_cost('grid.txt'))