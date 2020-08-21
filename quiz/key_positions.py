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


print(key_positions([0, 1, 2], lambda x: x))

print(key_positions([2, 1, 0], lambda x: x))

print(key_positions([1, 2, 3, 2], lambda x: x))

print(key_positions([5], lambda x: x))

print(key_positions(range(-3,3), lambda x: x**2))

#print(key_positions(range(1000), lambda x: 4))

print(key_positions([1] + [0] * 100, lambda x: x))