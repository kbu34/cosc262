def adjacency_matrix(graph_str):
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
    vertex_num = int(graph_info[1])
    del string_list[0]
    del string_list[-1]
    while count < vertex_num:
        weight_list = []
        count1 = 0
        while count1 < vertex_num:
            weight_list.append(float('inf'))
            count1 += 1
        graph_list.append(weight_list)
        graph_list[count][count] = 0
        count += 1
    for string in string_list:
        x, y, weight = string.split()
        x = int(x)
        y = int(y)
        graph_list[x][y] = int(weight)
        if not directed:
            graph_list[y][x] = int(weight)
            

    return graph_list    



graph_str = """\
U 3 W
0 1 5
2 1 7
"""

print(adjacency_matrix(graph_str))

print()
graph_str = """\
D 2 W
0 1 4
"""

print(adjacency_matrix(graph_str))
print()

graph_str = """\
U 4 W
"""

print(adjacency_matrix(graph_str))
print()

graph_str = """\
U 10 W
"""

print("\n".join(str(row) for row in adjacency_matrix(graph_str)))

print()

graph_str = """\
D 3 W
0 1 1
1 2 2
2 0 4
"""

adj_matrix = adjacency_matrix(graph_str)

print("Adjacency matrix:", adj_matrix)