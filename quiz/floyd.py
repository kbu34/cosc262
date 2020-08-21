import copy
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


def floyd(adjacency_matrix):
    count = 0
    output_matrix = copy.deepcopy(adjacency_matrix)
    n = len(output_matrix)
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                output_matrix[i][j] = min(output_matrix[i][j], output_matrix[i][k] + output_matrix[k][j])
    return output_matrix


graph_str = """\
D 3 W
0 1 1
1 2 2
2 0 4
"""

adj_matrix = adjacency_matrix(graph_str)
dist_matrix = floyd(adj_matrix)

print("Adjacency matrix:", adj_matrix)
print("Distance matrix:", dist_matrix)

print()

import pprint

# example from the textbook - figure 6.3

graph_str = """\
U 7 W
0 1 5
0 2 7
0 3 12
1 2 9
2 3 4
1 4 7
2 4 4
2 5 3
3 5 7
4 5 2
4 6 5
5 6 2
"""

pprint.pprint(floyd(adjacency_matrix(graph_str)))