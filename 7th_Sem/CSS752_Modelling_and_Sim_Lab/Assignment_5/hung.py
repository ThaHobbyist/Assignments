from getTable import * 

# check if table is balanced
def checkBal(table):
    r = len(table)
    c = len(table[0])

    if r == c:
        print("table is balanced")
    else:
        print("table is not balanced, balancing now...")
        if r > c:
            tmp  = r - c
            for row in table:
                for i in range(tmp):
                    row.append(0)
        else:
            tmp = c - r
            trow = []
            for i in range(c):
                trow.append(0)
            
            for i in range(tmp):
                table.append(trow)

# for each row find smallest elem and subtract from the row

def minElem(table):
    min_r = []
    for row in table:
        m = 999
        for elem in row:
            m = min(m, elem)
        min_r.append(m)

    for i in range(len(table)):
        for j in range(len(table[0])):
            table[i][j] = table[i][j] - min_r[i]

# for each col find least value and subtract from the col
    min_c = []
    for j in range(len(table[0])):
        m = 999
        for i in range(len(table)):
            m = min(table[i][j], m)
    
    for j in range(len(table[0])):
        for i in range(len(table)):
            table[i][j] = table[i][j] - min_c[j]
    
    return table

# 4 cover the zeroes with min num of horizontal and vertival lines


# if num of lines < n, not optimal, else optimal. the pos. of zeroes are allocations

#  select lowest number not covered by line

#  subtract said amount from uncovered rows

# add said amount to covered cols

# go back to 4