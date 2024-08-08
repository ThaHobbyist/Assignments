from basic import *
from modi import *

table = [
    [5, 3, 6, 2],
    [4, 3, 9, 1],
    [3, 4, 7, 5]
]

supply = [19, 37, 34]

demand = [16, 18, 31, 25]

res, assign = nwcr(table, supply, demand)

print(res, assign)

assign_table = makeAssignTable(len(supply), len(demand), assign)

print(assign_table)

u, v = genUV(assign_table, table)

print(u, v)

table_ij = genDelIJ(u, v, table, assign_table)

print(table_ij)

optc = checkOptimal(table_ij)

print(optc)

process(table, supply, demand, u, v, assign_table, table_ij)