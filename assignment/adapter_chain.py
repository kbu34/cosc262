def recur(graph_list, chain_list, list_list, charger_plug, wall_socket):
    if charger_plug == wall_socket:
        list_list.append(chain_list)
    else:
        for graph in graph_list:  
            if graph[0] == charger_plug:   
                temp_list = chain_list[:]
                if graph[1] not in temp_list:
                    temp_list.append(graph[1])
                    recur(graph_list, temp_list, list_list, graph[1], wall_socket)   
                else:
                    break   

def adapter_chain(adapters_info, charger_plug, wall_socket):
    count = 0
    graph_list = []
    string_list = adapters_info.split('\n')
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
    #print(string_list)
    for string in string_list:
        x, y = string.split()
        graph_list.append([int(x), int(y)])
    chain_list = [charger_plug]
    list_list = []
    des_list = [graph[1] for graph in graph_list]
    if charger_plug == wall_socket:
        return [wall_socket]    
    if wall_socket not in des_list:
        return "CS Unplugged!"
    recur(graph_list, chain_list, list_list, charger_plug, wall_socket)
    if len(list_list) == 0:
        return "CS Unplugged!"
    fastest = min(list_list, key=len)
    return fastest
    
      
      
      
adapters_info_str = """\
D 5
1 0
0 2
2 3
1 2
"""
    
print(adapter_chain(adapters_info_str, 1, 2))

adapters_info_str = """\
D 2
0 1
"""

charger_plug = 0
wall_socket = 1

print(adapter_chain(adapters_info_str, charger_plug, wall_socket))

adapters_info_str = """\
D 2
0 1
"""

print(adapter_chain(adapters_info_str, 1, 1))

adapters_info_str = """\
D 2
0 1
"""

print(adapter_chain(adapters_info_str, 1, 0))

adapters_info_str = """\
D 5
1 0
0 2
2 3
1 2
"""

print(adapter_chain(adapters_info_str, 1, 2))

adapters_info_str = """\
D 1
"""

print(adapter_chain(adapters_info_str, 0, 0))

adapters_info_str = """\
D 5
0 1
0 2
1 2
2 3
1 3
3 0
"""

print(adapter_chain(adapters_info_str, 1, 0))
print(adapter_chain(adapters_info_str, 0, 3) in [[0, 1, 3], [0, 2, 3]])
print(adapter_chain(adapters_info_str, 4, 4))
print(adapter_chain(adapters_info_str, 3, 3))
print(adapter_chain(adapters_info_str, 3, 2))
print(adapter_chain(adapters_info_str, 3, 4))