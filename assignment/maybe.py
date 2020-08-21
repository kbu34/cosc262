def dfs_loop(adj_list, u, states, parent_list, stack):
    global cycle
    for adj in adj_list[u]:
        neighbour = adj[0]
        if states[neighbour] == 'D':
            cycle = True      
        if states[neighbour] == 'U':
            states[neighbour] = 'D'
            parent_list[neighbour] = u
            dfs_loop(adj_list, neighbour, states, parent_list, stack)
    states[u] = 'P'
    stack.append(u)

def adjacency_list(graph_str, edge_num=None):
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
    
def computation_order(dependencies):
    global cycle
    adj_list = adjacency_list(dependencies)
    graph_list = []
    cycle = False
    stack = []
    states = ['U' for x in range(0, len(adj_list))]
    n = len(adj_list)
    for i in range(0, n):
        parent_list = []
        count = 0
        parent_list = [None for x in range(0, n)]
        if states[i] == 'U':
            states[i] = 'D'
            dfs_loop(adj_list, i, states, parent_list, stack)
            if cycle:
                return None
    return stack   


dependencies = """\
D 2
0 1
"""

print(computation_order(dependencies))

dependencies = """\
D 3
1 2
0 2
"""

print(computation_order(dependencies) in [[2, 1, 0], [2, 0, 1]])

dependencies = """\
D 5
2 3
3 2
"""
    
print(computation_order(dependencies))

dependencies = """\
D 3
"""
# any permutation of 0, 1, 2 is valid in this case.
solution = computation_order(dependencies)
if solution is None:
    print("Wrong answer!")
else:
    print(sorted(solution))

dependencies = """\
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
print(computation_order(dependencies))

dependencies = """\
D 10
1 2
8 7
9 8
7 6
6 5
5 4
4 9
0 1
"""

print(computation_order(dependencies))

dependencies = """\
D 2000
"""

print(sorted(computation_order(dependencies)) == [i for i in range(2000)])

dependencies = """\
D 6
5 1
0 1
1 2
2 3
3 4
4 5
"""

print(computation_order(dependencies))