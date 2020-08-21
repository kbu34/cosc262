def coins_reqd(value, coinage):
    """The minimum number of coins to represent value"""
    num_coins = [0] * (value + 1)
    path_list = [None for x in range(value + 1)]
    for amt in range(min(coinage), value + 1):
        min_coin = float('inf')
        for c in coinage:
            if amt >=c:
                if num_coins[amt - c] < min_coin:
                    min_coin = num_coins[amt - c]
                    path_list[amt] = c
        num_coins[amt] = 1 + min_coin
    coin_used = [[coin, 0] for coin in coinage]
    cvalue = value
    while cvalue > 0:

        coin = path_list[cvalue]
        for used in coin_used:
            if used[0] == coin:
                used[1] += 1
        cvalue -= coin
    coin_final = coin_used[:]
    for coin in coin_used:
        if coin[1] == 0:
            coin_final.remove([coin[0], 0])
    coin_tuple = []
    for coins in coin_final:
        coin_tuple.append(tuple(coins))
    coin_tuple.sort(reverse=True, key=lambda x: x[0])
    return coin_tuple

print(coins_reqd(32, [1, 10, 25]))