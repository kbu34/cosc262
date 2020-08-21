def key_positions(seq, key):
    o = []
    for s in seq:
        o.append(key(s))
    k = max(o) + 1
    c = []
    for i in range(0, k):
        c.append(0)
    for s in seq:
        c[key(s)] += 1
    sum = 0
    for i in range(0, k):
        c[i], sum = sum, sum + c[i]
    return c

def sorted_array(seq, key, positions):
    b = []
    for i in range(0, len(seq)):
        b.append(None)
    p = key_positions(seq, key)
    for s in seq:
        b[p[key(s)]] = s
        p[key(s)] += 1
    return b

print(sorted_array([3, 1, 2], lambda x: x, [0, 0, 1, 2]))

print(sorted_array([3, 2, 2, 1, 2], lambda x: x, [0, 0, 1, 4]))

print(sorted_array([100], lambda x: x, [0]*101))

"""Counting Sort"""
import operator

def counting_sort(iterable, key):
    positions = key_positions(iterable, key)
    return sorted_array(iterable, key, positions)
    
objects = [("a", 88), ("b", 17), ("c", 17), ("d", 7)]

key = operator.itemgetter(1)
print(", ".join(object[0] for object in counting_sort(objects, key)))