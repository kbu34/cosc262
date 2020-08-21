def adjacency_list(graph_string):
    header, *edges = [s.split() for s in graph_string.splitlines()]
    directed = header[0] == 'D'
    weighted = len(header) == 3 and header[2] == 'W'
    num_vertices = int(header[1])
    adj_list = [[] for _ in range(num_vertices)]
    for edge in edges:
        edge_data = map(int, edge)
        if weighted:
            source, target, weight = edge_data
        else:
            source, target = edge_data
            weight = None
        adj_list[source].append((target, weight))
        if not directed:
            adj_list[target].append((source, weight))
    return adj_list

def next_vertex(in_tree, distance):
    count = 0
    while count < len(in_tree):
        if in_tree[count] is True:
            distance[count] = float('inf')
        count += 1
    return distance.index(min(distance))

def prim(adj_list, start):
    n = len(adj_list)
    in_tree = [False for x in range(n)]
    parent = [None for x in range(n)]
    distance = [float('inf') for x in range(n + 1)]
    distance[start] = 0
    while False in in_tree:
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if not in_tree[v] and weight < distance[v]:
                distance[v] = weight
                parent[v] = u
    return parent


graph_str = """\
U 4 W
2 1 3
0 1 2
2 0 1
1 3 3
0 3 5
"""

print(prim(adjacency_list(graph_str), 0))