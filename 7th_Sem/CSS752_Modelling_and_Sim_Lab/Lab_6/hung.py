def getTable():
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))

    table = []
    print("\nTable Entry......")
    for a in range(r):
        tmp = []
        print(f"Enter values of row {a}: ")
        tmp = list(map(int, input().split()))

        if len(tmp) != c:
            print("Incorrect number of elements")
            exit(1)

        table.append(tmp)
    
    return table

# check if table is balanced

def checkBal(table):
    r = len(table)
    c = len(table[0])

    if r == c:
        print("table is balanced")
    else:
        print("table is not balanced, balancing now...")
        if r > c:
            tmp = r - c
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
        print("balanced table is:")
        showTable(table)

def showTable(table):
    for r in table:
        for c in r:
            print(c, end=" ")
        print("")
    print("\n")

def getMinZero(table):
    cnt = 99999
    for r in table:
        cntt = 0
        for c in r:
            if c == 0:
                cntt += 1
        cnt = min(cnt, cntt)
    
    for j in range(len(table[0])):
        cntt = 0
        for i in range(len(table)):
            if table[i][j] == 0:
                cntt += 1
        cnt = min(cntt, cnt)
    
    return cnt

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

    min_c = []
    for j in range(len(table[0])):
        m = 999
        for i in range(len(table)):
            m = min(table[i][j], m)
        min_c.append(m)

    for j in range(len(table[0])):
        for i in range(len(table)):
            table[i][j] = table[i][j] - min_c[j]

    return table


def countListZeroes(ar, skip_index=[]):
    cnt = 0
    for i in range(len(ar)):
        if i not in skip_index and ar[i] == 0:
            cnt += 1

    return cnt


def makeCol(table, col_num):
    col = []
    for i in range(len(table)):
        col.append(table[i][col_num])
    return col


def countZeroes(table, omit_rows=[], omit_cols=[]):
    zeroes = 0
    for i in range(len(table)):
        if i not in omit_rows:
            for j in range(len(table[i])):
                if j not in omit_cols and table[i][j] == 0:
                    zeroes += 1
    return zeroes


def cover(table):

    numZeroes = countZeroes(table)
    # print(numZeroes)
    mark_rows = []
    mark_cols = []
    res = []

    # print(numZeroes)
    minZero = getMinZero(table)

    while numZeroes > 0:
        # print(numZeroes)
        # scan Rows
        for i in range(len(table)):
            if i not in mark_rows and countListZeroes(table[i], skip_index=mark_cols) <= minZero:
                for j in range(len(table[i])):
                    if j not in mark_cols and table[i][j] == 0:
                        mark_cols.append(j)
                        res.append([i, j])
                        col = makeCol(table, j)
                        numZeroes -= countListZeroes(col, mark_rows)

        # scan cols
        for j in range(len(table[0])):
            if j not in mark_cols and countListZeroes(makeCol(table, j), skip_index=mark_rows) <= minZero:
                for i in range(len(table)):
                    if i not in mark_rows and table[i][j] == 0:
                        mark_rows.append(i)
                        res.append([i, j])
                        numZeroes -= countListZeroes(table[i], mark_cols)
        
        minZero += 1


    return [mark_cols, mark_rows, res]


def adjust(table, mark_row, mark_col):
    min_elem = 99999999
    for i in range(len(table)):
        if i not in mark_row:
            for j in range(len(table[i])):
                if j not in mark_col:
                    min_elem = min(min_elem, table[i][j])

    for i in range(len(table)):
        if i not in mark_row:
            for j in range(len(table[i])):
                table[i][j] -= min_elem

    for j in mark_col:
        for i in range(len(table)):
            table[i][j] += min_elem

    return table


def hungarian(table):  # acttual process of hungarian method
    # for each row find smallest elem and subtract from the row
    # for each col find least value and subtract from the col
    table = minElem(table)

    showTable(table)
    # cover the zeroes with min num of horizontal and vertival lines
    mark_rows, mark_cols, res = cover(table)

    # if num of lines < n, not optimal, else optimal. the pos. of zeroes are allocations
    while (len(mark_cols) + len(mark_rows) < len(table)):

        # select lowest number not covered by line
        # subtract said amount from uncovered rows
        # add said amount to covered cols
        table = adjust(table, mark_rows, mark_cols)
        mark_rows, mark_cols, res = cover(table)
        print(len(mark_cols) + len(mark_rows) - len(table))
    
    return res

def solve(table):
    checkBal(table)
    res = hungarian(table.copy())

    sol = 0
    for val in res:
        i, j = val
        sol += table[i][j]
    
    return sol, res

if __name__ == "__main__":
    # table = getTable()

    table = [
        [5, 8, 7, 6, 6, 7],
        [8, 7, 8, 8, 7, 6],
        [6, 9, 8, 9, 9, 8],
        [7, 5, 6, 6, 6, 7],
        [6, 7, 5, 5, 5, 6],
        [9, 7, 6, 6, 6, 6],
        [5, 6, 7, 8, 9, 7],
        [8, 8, 9, 8, 7, 9]
    ]

    sol, res = solve(table)

    print(f"The optimal cost for the given problem is {sol}, and the assignments are {res}")