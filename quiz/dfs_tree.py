def dfs_loop(adj_list, u, states, parent_list):
    for adj in adj_list[u]:
        neighbour = adj[0]
        if states[neighbour] == 'U':
            states[neighbour] = 'D'
            parent_list[neighbour] = u
            dfs_loop(adj_list, neighbour, states, parent_list)
    states[u] = 'P'
    
def dfs_tree(adj_list, start):
    n = len(adj_list)
    parent_list = []
    states = []
    count = 0
    while count < len(adj_list):
        parent_list.append(None)
        states.append('U')
        count += 1
    stack = []
    states[start] = 'D'
    dfs_loop(adj_list, start, states, parent_list)
    return parent_list


# an undirected graph

adj_list = [
    [(1, None), (2, None)],
    [(0, None), (2, None)],
    [(0, None), (1, None)]
]

print(dfs_tree(adj_list, 0))
print(dfs_tree(adj_list, 1))
print(dfs_tree(adj_list, 2))

print()

# a directed graph (note the asymmetrical adjacency list)

adj_list = [
[(1, None)],
[]
]

print(dfs_tree(adj_list, 0))
print(dfs_tree(adj_list, 1))