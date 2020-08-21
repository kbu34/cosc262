def bfs_tree(adj_list, start):
    parent_list = []
    states = []
    count = 0
    while count < len(adj_list):
        parent_list.append(None)
        states.append('U')
        count += 1
    queue = []
    states[start] = 'D'
    queue.append(start)
    while len(queue) > 0:
        dequeue = queue.pop(0)
        for adj in adj_list[dequeue]:
            neighbour = adj[0]
            if states[neighbour] == 'U':
                states[neighbour] = 'D'
                parent_list[neighbour] = dequeue
                queue.append(neighbour)
    return parent_list


# an undirected graph

adj_list = [
    [(1, None)],
    [(0, None), (2, None)],
    [(1, None)]
]

print(bfs_tree(adj_list, 0))
print(bfs_tree(adj_list, 1))

print()

# a directed graph (note the asymmetrical adjacency list)

adj_list = [
[(1, None)],
[]
]

print(bfs_tree(adj_list, 0))
print(bfs_tree(adj_list, 1))