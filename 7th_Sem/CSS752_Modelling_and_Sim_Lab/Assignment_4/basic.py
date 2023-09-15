# Least Cost Method

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

    supply = []
    print("\nEnter the supply values:")
    supply = list(map(int, input().split()))
    if len(supply) != r:
        print("Incorrect number of elements")
        exit(1)

    demand = []
    print("\nEnter the demand values:")
    demand = list(map(int, input().split()))
    if len(demand) != c:
        print("Incorrect number of elements")
        exit(1)

    return table, supply, demand

def getTableTmp():
    table = [
        [5, 3, 6, 2],
        [4, 3, 9, 1],
        [3, 4, 7, 5]
    ]

    supply = [19, 37, 34]
    demand = [16, 18, 31, 25]

    return [table, supply, demand]

def getSum(ls):
    sum = 0
    for i in ls:
        sum += i
    return sum

def getMinElem(table, supply, demand):
    res = []
    m = 999999
    for i in range(len(table)):
        if supply[i] == 0:
            continue
        else:
            for j in range(len(table[0])):
                if demand[j] == 0:
                    continue
                else:
                    if (table[i][j] < m):
                        m = table[i][j]
                        res = [[i, j]]
                    elif (table[i][j] == m):
                        tmp = [i, j]
                        res.append(tmp)
                    else:
                        pass
    return res

def lcm(table, supply, demand):
    r = len(table)
    c = len(table[0])

    table_assign = [[0] * c] * r
    if getSum(supply) == 0 and getSum(demand) == 0:
        return 0
    else:
        res = 99999999999
        me = getMinElem(table, supply, demand)

        for coord in me:
            i, j = coord
            if supply[i] <= demand[j]:
                tdemnd = demand.copy()
                tsupp = supply.copy()
                tdemnd[j] -= supply[i]
                tsupp[i] = 0
                st = (table[i][j] * supply[i]) + lcm_rec(table, tsupp, tdemnd)
                if st < res:
                    res = st
                    supply = tsupp
                    demand = demand
                    
                else:
                    pass
            elif demand[j] < supply[i]:
                tdemnd = demand.copy()
                tsupp = supply.copy()
                tsupp[i] -= demand[j]
                tdemnd[j] = 0
                st = (table[i][j] * demand[j]) + lcm(table, tsupp, tdemnd)

                if st < res:
                    res = st
                    supply = tsupp
                    demand = tdemnd
                    
                else:
                    pass
        return res

def nwcr(table, supply, demand):
    #executing northwest corner rule
    assign = []
    i = 0
    j = 0
    res = 0
    while(i < len(table) and j < len(table[0])):
        if supply[i] < demand[j]:
            res += supply[i] * table[i][j]

            demand[j] -= supply[i]
            assign.append([supply[i], i, j])
            i += 1
        else:
            res += demand[j] * table[i][j]

            supply[i] -= demand[j]
            assign.append([demand[j], i, j])
            j += 1
    return res, assign

def isBal(table, supply, demand):
    if getSum(supply) != getSum(demand):
        print("Table is not balanced")

        print("\nBalancing Table....\n")
        if getSum(demand) < getSum(supply):
            for i in range(len(table)):
                table[i].append(0)
            demand.append(getSum(supply) - getSum(demand))
        elif getSum(supply) < getSum(demand):
            tmp = [0] * len(table[0])
            table.append(tmp)
            supply.append(getSum(demand) - getSum(supply))
    else:
        print("Table is Balanced\n")

if __name__ == '__main__':
    table, supply, demand = getTableTmp()

    isBal(table, supply, demand)
    res, assign = lcm_rec(table, supply.copy(), demand.copy())
    print(f"Initial feasible solution is {res}")
