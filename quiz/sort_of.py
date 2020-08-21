def sort_of(numbers): 
    result = [] 
    """for i in range(len(numbers)): 
        sub = sorted(numbers[i:]) 
        print(sub)
        result.append(sub[0]) 
    return result"""
    return sorted(numbers)

print(sort_of([1, 2, 3, 3]))