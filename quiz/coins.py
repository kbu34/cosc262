def coins_reqd(value, coinage):
    """Return a list of the coins that best represent the given value
       with the given coinage. The return value is a list of (count, denomination)
       tuples in descending order of demonination, including only tuples
       where count is greater than zero."""
    numCoins = [0] * (value + 1)
    best_coins = [-1 for i in range(value + 1)]  # Predecessor ('parent') array
    
    # Build an array of the minimum number of coins required for each amount up
    # to the required value.
    for amt in range(1, value + 1):
        best_coin = None
        # Try each coin in turn to see which one gives the minimum for this amount
        for coin in coinage:
            if amt >= coin and (best_coin is None or numCoins[amt - coin] < numCoins[amt - best_coin]):
                best_coin = coin
        numCoins[amt] = 1 + numCoins[amt - best_coin]
        best_coins[amt] = best_coin  # Record what coin was used to get us to this amt
          
    # Now trace backwards to find what coins were used
    amt = value
    print(best_coins)
    coin_counts = {coin: 0 for coin in coinage}
    while amt > 0:
        new_coin = best_coins[amt]
        coin_counts[new_coin] += 1
        amt -= new_coin
    coins = [(coin, coin_counts[coin]) for coin in coin_counts if coin_counts[coin] > 0]
    coins.sort(reverse=True)
    return coins

print(coins_reqd(32, [1, 10, 25]))