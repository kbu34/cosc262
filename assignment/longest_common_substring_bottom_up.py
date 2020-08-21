def longest_common_substring(s1, s2):
    """maybe not recursive"""
    grid = [[0 for y in range(len(s1) + 1)] for x in range(len(s2) + 1)]
    x = 0
    for x in range(len(grid)):
        y = 0
        while y < len(grid[0]):
            if x == 0 or y == 0:
                grid[x][y] = 0
            elif s1[y - 1] == s2[x - 1]:
                grid[x][y] = grid[x - 1][y - 1] + 1
            else:
                grid[x][y] = max(grid[x][y - 1], grid[x - 1][y])
            y += 1
    a = len(s2)
    b = len(s1)
    lcs = ''
    while a > 0 and b > 0:
        if s1[b - 1] == s2[a - 1]:
            lcs += s1[b - 1]
            a -= 1
            b -= 1
        elif grid[a][b - 1] > grid[a - 1][b]:
            b -= 1
        else:
            a -= 1
    return lcs[::-1]

s1 = "Look at me, I can fly!"
s2 = "Look at that, it's a fly"
print(longest_common_substring(s1, s2))

s1 = "abcdefghijklmnopqrstuvwxyz"
s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
print(longest_common_substring(s1, s2))

s1 = "balderdash!"
s2 = "balderdash!"
print(longest_common_substring(s1, s2))

s1 = 1500 * 'x'
s2 = 1500 * 'y'
print(longest_common_substring(s1, s2))