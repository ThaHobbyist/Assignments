print("Sayantani Karmakar: 20CS8024")
#input the table
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

# initialise the iterators
i = 0
j = 0
res = 0

# function definitions
def sumOf(ls):
    sum = 0
    for i in ls:
        sum += i
    return sum

def getMinElem(table, supply, demand):
    m = [99999999999999, 0, 0]
    for i in range(len(table)):
        if supply[i] == 0:
            continue
        else:
            for j in range(len(table[0])):
                if demand[j] == 0:
                    continue
                else:
                    if (table[i][j] < m[0]):
                        m = [table[i][j], i, j]
                    else:
                        pass
    return m


# checking for balanced table
if sumOf(supply) == sumOf(demand):
    print("\nTable is balanced")
    res = 0
    while(sumOf(supply) != 0 and sumOf(demand) != 0):
        m, i, j = getMinElem(table, supply, demand)
        if supply[i] < demand[j]:
            res += supply[i] * table[i][j]

            demand[j] -= supply[i]
            supply[i] = 0
        else:
            res += demand[j] * table[i][j]

            supply[i] -= demand[j]
            demand[j] = 0

    print(f"\nThe basic feasible solution is {res}")
else:
    print("table is not balanced")

