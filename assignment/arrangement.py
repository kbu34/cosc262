def nest_list(i, friend_list):
    for friend in friend_list:
        if i in friend:
            return True
    return False

def recur(local_friends, friend_list, graph_list):
    first_list = [graph[0] for graph in graph_list]
    if local_friends[-1] not in first_list:
        local_friends = list(set(local_friends))
        if local_friends not in friend_list:
            friend_list.append(local_friends)
    else:
        for graph in graph_list:
            copy_list = graph_list[:]
            if graph[0] == local_friends[-1]:
                local_friends.append(graph[1])
                copy_list.remove(graph)
                copy_list.remove([graph[1], graph[0]])
                recur(local_friends, friend_list, copy_list)

def arrangement(direct_friendship_info):
    count = 0
    graph_list = []
    string_list = direct_friendship_info.split('\n')
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
    for string in string_list:
        x, y = string.split()
        graph_list.append([int(x), int(y)])
        if not directed:
            graph_list.append([int(y), int(x)])
    first_list = [graph[0] for graph in graph_list]
    friend_list = []
    for i in range(0, edge_num):
        if i not in first_list:
            friend_list.append([i])
        elif nest_list(i, friend_list) == False:
            local_friends = [i]
            recur(local_friends, friend_list, graph_list)
    if len(friend_list) != 0:
        for i in range(0, edge_num):
            merge = []
            for friend in friend_list:
                if i in friend:
                    merge.append(friend)
            for merging in merge:
                friend_list.remove(merging)
            merged = []
            for merging in merge:
                merged += merging
            friend_list.append(merged)
    final_list = []
    for friend in friend_list:
        final_list.append(list(set(friend)))
    return final_list


direct_friendship_info = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

print(sorted(sorted(tables) for tables in arrangement(direct_friendship_info)))


direct_friendship_info = """\
U 2
0 1
"""

print(sorted(sorted(tables) for tables in arrangement(direct_friendship_info)))

direct_friendship_info = """\
U 2
"""

print(sorted(sorted(tables) for tables in arrangement(direct_friendship_info)))

direct_friendship_info = """\
U 0
"""

print(sorted(sorted(tables) for tables in arrangement(direct_friendship_info)))

direct_friendship_info = """\
U 1
"""

print(sorted(sorted(tables) for tables in arrangement(direct_friendship_info)))

direct_friendship_info = """\
U 5
1 3
2 0
0 1
0 4
"""

print(sorted(sorted(tables) for tables in arrangement(direct_friendship_info)))

	
direct_friendship_info = """\
U 4
2 1
"""

print(sorted(sorted(tables)
      for tables in arrangement(direct_friendship_info)))

direct_friendship_info = """\
U 8
6 0
3 7
2 0
5 7
4 0
1 7
"""

print(sorted(sorted(tables) for tables in arrangement(direct_friendship_info)))