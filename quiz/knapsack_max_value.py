class Item:
    """An item to (maybe) put in a knapsack"""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
def max_value(items, capacity):
    """The maximum value achievable with a given list of items and a given
       knapsack capacity."""
       
    grid = [[0 for y in range(len(items) + 1)] for x in range(capacity + 1)]
    cap = capacity
    x = 0
    y = 1
    while y <= len(items):
        x = 0
        while x <= capacity:
            if x == 0:
                grid[x][y] = 0
            elif items[y - 1].weight <= x:
                last_value = grid[x][y - 1]
                new_value = grid[x - items[y - 1].weight][y - 1] + items[y - 1].value
                grid[x][y] = max(last_value, new_value)
            else:
                grid[x][y] = grid[x][y - 1]
            x += 1
        y += 1
    return grid[capacity][len(items)]
        
                
# A large test (blows away top-down DP)
# 1000 items, capacity 50 knapsack.
from random import random, seed
N = 1000
items = []
seed(12345)  # So we get same data every run
for i in range(N):
    value = int(1 + 100 * random())
    weight = int(1 + 20 * random())
    items.append(Item(value, weight))
your_answer = max_value(items, 50)
print(your_answer)

items = [Item(45, 3),
         Item(45, 3),
         Item(80, 4),
         Item(80, 5),
         Item(100, 8)]
print(max_value(items, 10))

items = [Item(45, 3),
         Item(45, 3),
         Item(80, 4),
         Item(80, 5),
         Item(100, 8)]
for capacity in range(26):
    print(f"{capacity:2}: {max_value(items, capacity)}")