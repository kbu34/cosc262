def almost_all(numbers):
    new_list = []
    total = sum(numbers)
    for x in numbers:
        new_list.append(total - x)
    return new_list
    #return [sum(numbers) - x for x in numbers] 
    
print(almost_all([1,2,3]))
almost_all(list(range(10**5)))
print('okay')