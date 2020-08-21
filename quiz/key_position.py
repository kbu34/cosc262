def key_positions(strings):
    k = len(max(strings, key=lambda x: len(x))) + 1
    c = [0 for x in range(k)]
    for stri in strings:
        c[len(stri)] += 1
    summ = 0
    for i in range(k):
        c[i], summ = summ, summ + c[i]
    return c


print(key_positions(["", "a", "aa"]))

print(key_positions(["aa", "a", ""]))

print(key_positions(["a", "ab", "abc", "aa"]))

print(key_positions(["abcde"]))

print(key_positions(["cba", "ba", "b", "ac"]))