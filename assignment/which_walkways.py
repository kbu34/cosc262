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

def which_walkways(campus_map):
    path_list = []
    graph_list, vert_num = adjacency_list(campus_map)
    in_tree = [False for x in range(0, vert_num)]
    distance = [float('inf') for x in range(0, vert_num)]
    parent = [None for x in range(0, vert_num)]
    distance[0] = 0
    while False in in_tree:
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in graph_list[u]:
            if in_tree[v] == False and weight < distance[v]:
                distance[v] = weight
                parent[v] = u
    count = 0
    while count < len(parent):
        if parent[count] != None:
            if parent[count] < count:
                path_list.append((parent[count], count))
            else:
                path_list.append((count, parent[count]))
        count += 1
    return path_list

campus_map = """\
U 3 W
0 1 1
2 1 2
2 0 4
"""

print(sorted(which_walkways(campus_map)))


campus_map = """\
U 1 W
"""

print(sorted(which_walkways(campus_map)))

campus_map = """\
U 4 W
0 1 5
1 3 5
3 2 3
2 0 5
0 3 2
1 2 1
"""

print(sorted(which_walkways(campus_map)))