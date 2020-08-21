def recursive_divide(x, y, count=0):
    remainder = x - y
    if remainder < 0:
        return count
    elif remainder >= 0:
        count += 1
        return recursive_divide(remainder, y, count)
        	
print(recursive_divide(9, 3))