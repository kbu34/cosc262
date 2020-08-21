def common(s1, s2, cashe=None):
    """does recursion"""
    if cashe is None:
        cashe = {}
    if (len(s1), len(s2)) not in cashe:
        if len(s1) == 0 or len(s2) == 0:
            cashe[(len(s1), len(s2))] = (0, '')
        elif s1[len(s1) - 1] == s2[len(s2) - 1]:
            tup = common(s1[:-1], s2[:-1], cashe)
            cost, lcs = tup
            cost += 1
            lcs += s1[-1]
            cashe[(len(s1), len(s2))] = (cost, lcs)
        else:
            tup1 = common(s1[:-1], s2, cashe)
            tup2 = common(s1, s2[:-1], cashe)
            cost1, lcs1 = tup1
            cost2, lcs2 = tup2
            if cost1 < cost2:
                cashe[(len(s1), len(s2))] = (cost2, lcs2)
            else:
                cashe[(len(s1), len(s2))] = (cost1, lcs1)
    return cashe[(len(s1), len(s2))]    

def longest_common_substring(s1, s2):
    """calls recursion"""
    value = common(s1, s2)
    return value[1]
    

s1 = "Look at me, I can fly!"
s2 = "Look at that, it's a fly"
print(longest_common_substring(s1, s2))

s1 = "abcdefghijklmnopqrstuvwxyz"
s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
print(longest_common_substring(s1, s2))

s1 = "balderdash!"
s2 = "balderdash!"
print(longest_common_substring(s1, s2))
