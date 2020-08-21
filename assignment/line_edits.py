def neighbour(x, y, table, lcs):
    '''neighbours'''
    if x == 0:
        neighbours = [table[x][y - 1]]
    elif y == 0:
        neighbours = [table[x - 1][y]]
    elif lcs is True:
        neighbours = [table[x - 1][y], table[x][y - 1]]
    else:
        neighbours = [table[x - 1][y], table[x][y - 1], table[x - 1][y - 1]]
    return neighbours

def brackets(st, lcs):
    bra_st = ''
    count = 0
    for i in range(len(st)):
        if st[i] in lcs:
            bra_st += st[i]
            count += 1
        elif st[i] not in lcs:
            bra_st += "[["
            bra_st += st[i]
            bra_st += "]]"
        else:
            bra_st += st[i]
    return bra_st

def line_edits(s1, s2):
    """checks edited lines"""
    sp1, sp2 = (s1.splitlines(), s2.splitlines())
    table = [[None for y in range(len(sp1) + 1)] for x in range(len(sp2) + 1)]
    for y in range(len(sp1) + 1):
        for x in range(len(sp2) + 1):
            if x == 0 and y == 0:
                table[x][y] = 0
            elif x == 0:
                table[x][y] = y
            elif y == 0:
                table[x][y] = x
            elif sp1[y - 1] == sp2[x - 1]:
                table[x][y] = table[x - 1][y - 1]
            else:
                table[x][y] = min(table[x - 1][y], table[x][y - 1], table[x - 1][y - 1]) + 1
    x, y, edits = (len(table) - 1, len(table[0]) - 1, [])
    while x >= 0 and y >= 0 and not (x == 0 and y == 0):
        neighbours = neighbour(x, y, table, False)
        if x > 0 and y > 0 and sp2[x - 1] == sp1[y - 1]:
            edits.append(('T', sp1[y - 1], sp2[x - 1]))
            x -= 1
            y -= 1
        elif y > 0 and table[x][y - 1] == min(neighbours):
            edits.append(('D', sp1[y - 1], ''))
            y -= 1
        elif x > 0 and table[x - 1][y] == min(neighbours):
            edits.append(('I', '', sp2[x - 1]))
            x -= 1
        else:
            lcs1, lcs2 = sp1[y - 1], sp2[x - 1]
            lcs_grid = [[None for ly in range(len(lcs1) + 1)] for lx in range(len(lcs2) + 1)]
            for ly in range(len(lcs1) + 1):
                for lx in range(len(lcs2) + 1):
                    if lx == 0 or ly == 0:
                        lcs_grid[lx][ly] = 0
                    elif lcs1[ly - 1] == lcs2[lx - 1]:
                        lcs_grid[lx][ly] = lcs_grid[lx - 1][ly - 1] + 1
                    else:
                        lcs_grid[lx][ly] = max(lcs_grid[lx - 1][ly], lcs_grid[lx][ly - 1])
            lcs, lcs_x, lcs_y = "", len(lcs2), len(lcs1)
            while (lcs_x >= 0 or lcs_y >= 0) and not(lcs_x == 0 and lcs_y == 0):
                neigh = neighbour(lcs_x, lcs_y, lcs_grid, True)
                if lcs1[lcs_y - 1] == lcs2[lcs_x - 1]:
                    lcs += lcs1[lcs_y - 1]
                    lcs_x -= 1
                    lcs_y -= 1
                elif lcs_x > 0 and lcs_grid[lcs_x - 1][lcs_y] == max(neigh):
                    lcs_x -= 1
                elif lcs_y > 0 and lcs_grid[lcs_x][lcs_y - 1] == max(neigh):
                    lcs_y -= 1
            lcs = lcs[::-1]
            bra_str1 = brackets(lcs1, lcs)
            bra_str2 = brackets(lcs2, lcs)
            edits.append(('S', bra_str1, bra_str2))
            x -= 1
            y -= 1
    return edits[::-1]
    
    
"""s1 = "Line1\nLine2\nLine3\nLine4\n"
s2 = "Line1\nLine3\nLine4\nLine5\n"
table = line_edits(s1, s2)
for row in table:
    print(row)
    
print()
s1 = "Line1\nLine2\nLine3\nLine4\n"
s2 = "Line5\nLine4\nLine3\n"
table = line_edits(s1, s2)
for row in table:
    print(row)
    
print()
s1 = "Line1\n"
s2 = ""
table = line_edits(s1, s2)
for row in table:
    print(row)

print()    
s1 = ""
s2 = "Line1\n"
table = line_edits(s1, s2)
for row in table:
    print(row)"""

s1 = "Line1\nLine 2a\nLine3\nLine4\n"
s2 = "Line5\nline2\nLine3\n"
table = line_edits(s1, s2)
for row in table:
    print(row)
    
s1 = "Blah\nLine1\n"
s2 = "Blah\nSomething\n"
table = line_edits(s1, s2)
for row in table:
    print(row)