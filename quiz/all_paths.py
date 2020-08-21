def recur(graph_list, path, path_list, source, destination):
    if source == destination:
        path_list.append(path)
    else:
        for graph in graph_list:
            if graph[0] == source:
                if graph[1] not in path:
                    path_copy = path[:]
                    path_copy.append(graph[1])
                    recur(graph_list, path_copy, path_list, graph[1], destination)
    

def all_paths(graph_string, source, destination):
    path_list = []
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
    for string in string_list:
        a, b = string.split()
        graph_list.append([int(a),int(b)])
        if not directed:
            graph_list.append([int(b),int(a)])
    path = [source]
    recur(graph_list, path, path_list, source, destination)
    return path_list
    
    
# triangle graph
graph_str = """\
U 3
0 1
1 2
2 0
"""
    
print(sorted(all_paths(graph_str, 0, 2)))
print(all_paths(graph_str, 1, 1))

print()


graph_str = """\
U 5
0 2
1 2
3 2
4 2
1 4
"""

print(sorted(all_paths(graph_str, 0, 1)))

print()


from pprint import pprint

# graph in fig 5.15 of textbook
# vertices 0 to 6 correspond to A to G
graph_str = """\
D 7
6 0
6 5
0 1
0 2
1 2
1 3
2 4
2 5
4 3
5 4
"""

pprint(sorted(all_paths(graph_str, 6, 3)))