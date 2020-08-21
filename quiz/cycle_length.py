def cycle_length(n, count=0):
    if n == 1:
        count += 1
        return count
    elif n % 2 == 0:
        count += 1
        n = n / 2
        return cycle_length(n, count)
    else:
        count += 1
        n *= 3
        n += 1
        return cycle_length(n, count)
    
print(cycle_length(22))