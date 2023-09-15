def makeNonDegen(table, supply, demand, table_assign):
    pass
    # get independent locations
    # allocate a small value at the smallest cost out of the independent locations

def makeZeroTable(r, c):
    table = []

    for i in range(r):
        table.append([])
        for j in range(c):
            table[i].append(0)

    return table

def makeAssignTable(r, c, assign):
    table_assign = makeZeroTable(r, c)
    
    for it in assign:
        val, i, j = it
        table_assign[i][j] = val
    
    return table_assign

def numNull(ar):
    num = 0
    for i in ar:
        if i == None: 
            num += 1
    return num

def checkIndependent(table_assign):
    r = len(table_assign)
    c = len(table_assign[0])

    elim_row = []
    elim_col = []
    for i in range(r):
        cnt = 0
        for j in range(c):
            if table_assign[i][j] != 0:
                cnt += 1
        if cnt < 2:
            elim_row.append(i)
    
    for j in range(c):
        cnt = 0
        for i in range(r):
            if table_assign[i][j] != 0:
                cnt += 1
        if cnt < 2:
            elim_col.append(j)
    
    mc = 100
    for i in range(r):
        if i not in elim_row:
            cnt = 0
            for j in range(c):
                if j not in elim_col and table_assign[i][j] != 0:
                    cnt += 1
            mc = min(cnt, mc)
        
    for j in range(c):
        if j not in elim_col:
            cnt = 0
            for i in range(r):
                if i not in elim_row and table_assign[i][j] != 0:
                    cnt += 1
            mc = min(cnt, mc)
    
    if mc >= 2:
        return False
    else:
        return True

def genUV(table_assign, table):
    r = len(table_assign)
    c = len(table_assign[0])

    u = [None] * r
    v = [None] * c

    max_r = 0

    mu = -1
    for i in range(r):
        cnt = 0
        for j in range(c):
            if table_assign[i][j] != 0:
                cnt += 1
        if cnt > max_r:
            mu = i
            max_r = cnt

    mv = -1
    max_c = 0
    for j in range(c):
        cnt = 0
        for i in range(r):
            if table[i][j] != 0:
                cnt += 1
        if cnt > max_c:
            mv = j
            max_c = cnt
    
    if max_r >= max_c:
        u[mu] = 0
        i = mu
        j = -1
        while numNull(u) > 0 and numNull(v) > 0:
            for t in range(len(table_assign[i])):
                if table_assign[i][t] != 0 and v[t] == None:
                    v[t] = table[i][t] - u[i]
                    j = t
            
            for t in range(len(table_assign)) and u[t] == None:
                if table_assign[t][j] != 0:
                    u[t] = table[t][j] - v[t]
                    i = t

    else:
        v[mv] = 0
        j = mv
        i = -1
        while numNull(u) > 0 and numNull(v) > 0:
            for t in range(len(table_assign)):
                if table_assign[t][j] != 0 and u[t] == None:
                    u[t] = table[t][j] - v[t]
                    i = t

            for t in range(len(table_assign[i])):
                if table_assign[i][t] != 0 and v[t] == None:
                    v[t] = table[i][t] - u[i]
                    j = t
    return [u, v]

def genDelIJ(u, v, table, table_assign):
    r = len(table_assign)
    c = len(table_assign[0])

    table_ij = makeZeroTable(r, c)

    for i in range(r):
        for j in range(c):
            if table_assign[i][j] == 0:
                val = table[i][j] - (u[i] + v[j])
                table_ij[i][j] = val
    
    return table_ij

def checkOptimal(table_ij):
    m = 9999

    for row in table_ij:
        for elem in row:
            if elem != 0:
                m = min(m, elem)
    res = 0
    if m > 0:
        res = 1 # optimal 
    elif m >= 0:
        res = 2 # optimal but other solutions exist
    else:
        res = 3 # not optimal
    
    return res

def process(table, supply, demand, u, v, table_assign, table_ij):
    # get minimum value of delta ij
    r = 0
    c = 0
    m = 0

    for i in range(len(table_ij)):
        for j in range(len(table_ij[0])):
            if table_ij[i][j] < m:
                m = table_ij[i][j]
                r = i
                c = j
    
    # make loop with allocated items
    elim_col = []
    elim_row = []

    for i in range(len(table)):
        cnt = 0
        for j in range(len(table[0])):
            if table_assign[i][j] != 0 or (i == r and j == c):
                cnt += 1
        if cnt < 2:
            elim_row.append(i)
    
    for j in range(len(table[0])):
        cnt = 0
        for i in range(len(table)):
            if table_assign[i][j] != 0 or (i == r and j == c):
                cnt += 1
        if cnt < 2:
            elim_col.append(j)
    
    loop = [[r, c]]

    i = r
    j = 0
    while(len(loop) != 4):
        pass
    
    print(loop)
        

    # allocate + and - to the cells in the loop

    # get minimum allocated value from - cells

    # execute + and - opetations on the respective cells with the selected value


def modi(table, supply, demand, assign):
    r = len(table)
    c = len(table[0])
    table_assign = makeAssignTable(r, c, assign)
    
    if len(assign) == r+c-1 and checkIndependent(table_assign):
        print("It is non degenerate solution")
    else:
        print("It is degenerate solution\nConverting into non degenerate")
        # makeNonDegen(table, supply, demand, table_assign.copy())
    
