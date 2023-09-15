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

# checking for balanced table
def sumOf(ls):
    sum = 0
    for i in ls:
        sum += i
    return sum

if sumOf(supply) == sumOf(demand):
    print("\nThe table is balanced")

    #executing northwest corner rule
    while(i < len(table) and j < len(table[0])):
        if supply[i] < demand[j]:
            res += supply[i] * table[i][j]

            demand[j] -= supply[i]
            i += 1
        else:
            res += demand[j] * table[i][j]

            supply[i] -= demand[j]
            j += 1

    print(f"The basic feasible solution is {res}")
else:
    print("Table is not balanced")