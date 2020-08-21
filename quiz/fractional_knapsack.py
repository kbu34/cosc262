def fractional_knapsack(capacity, items):
    benefit = 0.0
    if len(items) == 0:
        return benefit
    item_value = []
    item_quant = []
    for item in items:
        name, value, weight = item
        item_value.append(value/weight)
        item_quant.append(weight)
    while capacity > 0:
        if len(item_value) == 0:
            return benefit
        maximum = max(item_value)
        benefit += maximum
        index_value = item_quant[item_value.index(maximum)]
        index_value -= 1
        item_quant[item_value.index(maximum)] = index_value
        if index_value <= 0:
            item_quant.remove(0)
            item_value.remove(maximum)
        capacity -= 1
    return benefit

# The example from the lecture notes
items = [
    ("Chocolate cookies", 20, 5),
    ("Potato chips", 15, 3),
    ("Pizza", 14, 2),
    ("Popcorn", 12, 4)]
print(fractional_knapsack(9, items))

items = []
print(float(fractional_knapsack(11, items)))
	
items = [
    ("Chocolate cookies", 20, 5),
    ("Potato chips", 15, 3),
    ("Pizza", 14, 2),
    ("Popcorn", 12, 4)]
print(float(fractional_knapsack(100, items)))