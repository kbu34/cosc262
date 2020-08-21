def dfs_backtrack(candidate, input_data, output_data):
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)


def powerset(s):
    """Returns a list of all subsets of s. Each subset itsel is a list."""
    output_data = []
    items = list(s) # convert the set to a list so it can be indexed
    dfs_backtrack([], items, output_data)
    return output_data
    
def is_solution(candidate, items):
    """Returns True if the candidate is ready to be a subset."""
    if len(candidate) == len(items):
        return True
    else:
        return False
            
def add_to_output(candidate, output_data):
    """Takes a candidate and turns it into a subset by removing None elements
    then it adds the subset to the output_data list."""
    string = []
    for i in candidate:
        if i != [None]:
            string.append(i)
    output_data.append(string)

def children(candidate, items):
    """Assuming that the given candidate is not a solution yet, this function
    returns two new candidates: one that does not contain the next element, and
    one that does contain the next element. The next element is at index k of
    items."""
    k = len(candidate)
    left = [[None] for x in range(len(candidate) + 1)]
    for i in range(len(candidate)):
        left[i] = candidate[i]
    right = [[None] for x in range(len(candidate) + 1)]
    for i in range(len(candidate)):
        right[i] = candidate[i]
    right[-1] = items[k]
    print(left, right)
    return (right, left)

    

subsets = powerset({1, 2, 3})
for subset in sorted(sorted(sub) for sub in subsets):
    print(subset)