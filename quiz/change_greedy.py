def change_greedy(amount, coinage):
    coinage.sort(reverse=True)
    change = []
    for coin in coinage:
        coin_amount = 0
        while amount >= coin:
            amount -= coin
            coin_amount += 1
        if coin_amount > 0:
            change.append((coin_amount, coin))
    if amount != 0:
        return None
    else:
        return change

print(change_greedy(82, [1, 10, 25, 5]))
print(change_greedy(80, [1, 10, 25]))
print(change_greedy(82, [10, 25, 5]))