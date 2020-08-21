from pprint import pprint
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


graph_string = """\
D 3
0 1
1 0
0 2
"""
print(adjacency_list(graph_string))

graph_string = """\
D 3 W
0 1 7
1 0 -2
0 2 0
"""
print(adjacency_list(graph_string))

print()
# undirected graph in the textbook example
graph_string = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

pprint(adjacency_list(graph_string))

print()
graph_string = """\
U 17
1 2
1 15
1 6
12 13
2 15
13 4
4 5
"""

pprint(adjacency_list(graph_string))

print()
graph_string = """\
U 12 W
0 1 1
1 9 12
1 10 3
1 11 -4
10 11 25
"""

pprint(adjacency_list(graph_string))


dependencies = """\
D 2
0 1
"""

print(adjacency_list(dependencies))