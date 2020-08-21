def next_vertex(in_tree, distance):
    false_list = []
    for tree in in_tree:
        false_list.append(float('inf'))
    count = 0
    while count < len(in_tree):
        if in_tree[count] == False:
            false_list[count] = distance[count]
        count += 1
    count = 0
    minimum = float('inf')
    while count < len(false_list):
        if false_list[count] < minimum:
            minimum = false_list[count]
            min_index = count
        count += 1
    return min_index

in_tree = [False, True, True, False, False]
distance = [float('inf'), 0, 3, 12, 5]
print(next_vertex(in_tree, distance))