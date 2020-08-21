pit_list = []

def added(value, pit_list):
    pit_list.append(value)
    
def recur(seq, pit_list):
    if seq == [] or len(seq) == 1:
        return []
    if len(seq) % 2 == 1:
        s = len(seq) + 1 // 2
    else:
        s = len(seq) // 2
    try:
        if seq[s] <= seq[s-1]:
            pit_list.append(seq[s])
    except:
        if seq[s] <= seq[s+1]:
            pit_list.append(seq[s])
    try:
        if seq[s] <= seq[s+1]:
            pit_list.append(seq[s])
    except:
        if seq[s] <= seq[s-1]:
            pit_list.append(seq[s])    
    right = seq[s:]
    recur(right, pit_list)
    left = seq[:s]    
    recur(left, pit_list)

def find_pit(seq):
    pit_list = []
    recur(seq, pit_list)
    pit_list = sort(list(set(pit_list)))
    return pit_list

print(find_pit([5, 4, 5]))