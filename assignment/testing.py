def adjacency_list(graph_str):
    graph_list = []
    count = 0
    string_list = graph_str.split('\n')
    graph_info = string_list[0].split()
    if graph_info[0] == 'D':
        directed = True
    else:
        directed = False
    if graph_info[-1] == 'W':
        weighted = True
    else:
        weighted = False
    edge_num = int(graph_info[1])
    del string_list[0]
    del string_list[-1]
    list_copy = string_list[:]
    while count < edge_num:
        node = []
        graph_list.append(node)
        count += 1
    for string in list_copy:
        string_split = string.split()
        if weighted:
            weight = int(string_split[2])
        else:
            weight = None
        graph_list[int(string_split[0])].append((int(string_split[1]), weight))
        if not directed:
            graph_list[int(string_split[1])].append((int(string_split[0]), weight))
    return graph_list

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

city_map = """\
U 1000 W
810 820 100
830 840 100
810 830 100
820 840 200
810 840 500
840 850 100
860 850 100
860 840 150
880 870 100
890 880 100
"""
p = adjacency_list(city_map)
print(bfs_tree(p, 0))
#print(maximum_energy(city_map, 820))
#print(maximum_energy(city_map, 890))