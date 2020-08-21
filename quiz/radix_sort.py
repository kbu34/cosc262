def key_positions(seq, key):
    o = []
    for s in seq:
        o.append(key(s))
    k = max(o) + 1
    c = []
    for i in range(0, k):
        c.append(0)
    for s in seq:
        c[key(s)] += 1
    sum = 0
    for i in range(0, k):
        c[i], sum = sum, sum + c[i]
    return c

def counting_sort(seq, key):
    b = []
    for i in range(0, len(seq)):
        b.append(None)
    p = key_positions(seq, key)
    for s in seq:
        b[p[key(s)]] = s
        p[key(s)] += 1
    return b

def radix_sort(numbers, d):
    count = 1
    final = []
    while count < d + 1:
        num = numbers[:]
        for number in num:
            if len(list(str(number))) < count:
                final.append(number)
                numbers.remove(number)
        numbers = counting_sort(numbers, lambda x: int(list(str(x))[-count]))
        count += 1
    for number in numbers:
        final.append(number)
    return final

"""print(radix_sort([329, 457, 657, 839, 436, 720, 355], 3))

print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1))

print(radix_sort([329, 457, 657, 839, 436, 720, 355], 2))"""

	
print(radix_sort([9, 57, 657], 2))