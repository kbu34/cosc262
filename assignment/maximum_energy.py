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
    return graph_list, edge_num

def next_vertex(in_tree, distance):
    count = 0
    copy_dist = distance[:]
    found = False
    while not found:
        u = copy_dist.index(min(copy_dist))
        if in_tree[u] is False:
            return u
        else:
            copy_dist[u] = float('inf')

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

def maximum_energy(city_map, depot_position):
    graph_list, vert_num = adjacency_list(city_map)
    bfs_parents = bfs_tree(graph_list, depot_position)
    in_tree = [False for x in range(0, vert_num)]
    distance = [float('inf') for x in range(0, vert_num)]
    count = 0
    while count < vert_num:
        if bfs_parents[count] == None and count != depot_position:
            in_tree[count] = True
            distance[count] = -1
        count += 1
    parent = [None for x in range(0, vert_num)]
    distance[depot_position] = 0
    count = 0
    while False in in_tree:
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in graph_list[u]:
            if not in_tree[v] and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return max(distance) * 2

city_map = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(maximum_energy(city_map, 0))
print(maximum_energy(city_map, 1))
print(maximum_energy(city_map, 2))

	
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

print(maximum_energy(city_map, 810))
print(maximum_energy(city_map, 820))
print(maximum_energy(city_map, 890))