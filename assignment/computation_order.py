import itertools
def recur(sub_list, graph_list, solution_list, edge_num, yeah):
    if len(sub_list) <= 1:
        solution_list.append(sub_list)
    else:
        copy_list = graph_list[:]
        for graph in graph_list:
            for gra in graph:
                if gra not in sub_list:
                    copy_list.remove(graph)
                    break
        index_list1 = []
        index_list2 = []
        acc_nums = [None for x in range(0,edge_num)]
        first_list = [graph[1] for graph in copy_list]
        for first in first_list:
            if first in sub_list:
                if acc_nums[first] == None:
                    acc_nums[first] = 0
                acc_nums[first] += 1
        second_list = [graph[0] for graph in copy_list]
        for second in second_list:
            if second in second_list:
                if acc_nums[second] == None:
                    acc_nums[second] = 0
                acc_nums[second] -= 1
        for sub in sub_list:
            if acc_nums[sub] != None:
                if acc_nums[sub] <= 0:
                    index_list1.append(sub)
                else:
                    index_list2.append(sub)
            elif acc_nums[sub] == None:
                #yeah.append(sub)
                print(sub)
                print(acc_nums)
        if len(index_list1) == 0 or len(index_list2) == 0:
            solution_list.append(sub_list)
        else:
            recur(index_list1, copy_list, solution_list, edge_num, yeah)
            recur(index_list2, copy_list, solution_list, edge_num, yeah)
            
def permutations(list_list, perm_list, count=0, chain=[]):
    if count >= len(list_list):
        perm_list.append(chain)
    else:
        perm = list(itertools.permutations(list_list[count]))
        for per in perm:
            copy_chain = chain[:]
            copy_chain += list(per)
            permutations(list_list, perm_list, count+1, copy_chain)
    
                    
def computation_order(dependencies):
    graph_list = []
    string_list = dependencies.split('\n')
    graph_info = string_list[0].split()
    edge_num = int(graph_info[1])
    del string_list[0]
    del string_list[-1]
    for string in string_list:
        x, y = string.split()
        graph_list.append([int(x), int(y)])
    for graph in graph_list:
        x, y = graph
        if [y, x] in graph_list:
            return None
    solution_list = []
    if len(graph_list) != 0:
        for i in range(0, edge_num):
            yes = False
            for graph in graph_list:
                if i in graph:
                    yes = True
            if not yes:
                return None   
    else:
        return  [i for i in range(edge_num)]
    init_list = [x for x in range(0, edge_num)]
    yeah = []
    recur(init_list, graph_list, solution_list, edge_num, yeah)
    solution_list.reverse()       
    perm_list = []
    permutations(solution_list, perm_list)
    if len(perm_list[0]) == 0 or len(perm_list[0]) != edge_num:
        return None
    if len(perm_list) == 1:
        return perm_list[0]
    return perm_list[0]     


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
D 3
"""
# any permutation of 0, 1, 2 is valid in this case.
solution = computation_order(dependencies)
if solution is None:
    print("Wrong answer!")
else:
    print(sorted(solution))
    
dependencies = """\
D 5
2 3
3 2
"""
    
print(computation_order(dependencies))

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

#print(computation_order(dependencies))