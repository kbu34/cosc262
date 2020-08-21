def recur(perm, perm_list, s):
    if len(perm) == len(s):
        added(perm, perm_list)
    else:
        for i in s:
            if i not in perm:
                new_perm = perm[:]
                new_perm.append(i)
                recur(new_perm, perm_list, s)
        
def added(perm,perm_list):
    perm_list.append(tuple(perm))

def permutations(s):
    perm_list = []
    not_perm = []
    count = 0
    for i in s:
        not_perm.append([i])
    for perm in not_perm:
        recur(perm, perm_list, s)
    return perm_list
    
    
print(sorted(permutations({1,2,3})))

print(sorted(permutations({'a'})))

perms = permutations(set())
print(len(perms) == 0 or list(perms) == [()])