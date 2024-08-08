from sys import maxsize

def travelling_salesman_function(graph, s):
    v = len(graph)
    vertex = [i for i in range(v) if i != s]

    min_path = maxsize
    optimal_tour = []

    while True:
        current_cost = 0
        k = s
        tour = [s]  # Initialize the tour with the starting node

        for i in range(len(vertex)):
            current_cost += graph[k][vertex[i]]
            k = vertex[i]
            tour.append(k)  # Add the visited node to the tour

        current_cost += graph[k][s]
        tour.append(s)  # Complete the tour by returning to the starting node

        if current_cost < min_path:
            min_path = current_cost
            optimal_tour = tour

        if not next_perm(vertex):
            break
    
    return min_path, optimal_tour

def next_perm(l):
    n = len(l)
    i = n - 2

    while i >= 0 and l[i] > l[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = i + 1
    while j < n and l[j] > l[i]:
        j += 1

    j -= 1

    l[i], l[j] = l[j], l[i]
    left = i + 1
    right = n - 1

    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    
    return True

# Input number of nodes
v = int(input("Enter the number of nodes: "))

# Input the graph matrix
graph = []
for i in range(v):
    row = list(map(int, input(f"Enter distances from node {i} to all other nodes (space-separated): ").split()))
    graph.append(row)

# Input the starting node
s = int(input("Enter the starting node: "))

min_cost, tour = travelling_salesman_function(graph, s)

if not tour:
    print("No tour found.")
else:
    print(f"Optimal TSP tour: {', '.join(map(str, tour))}")
    print(f"Minimum TSP cost: {min_cost}")