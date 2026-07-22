from itertools import permutations

def tsp(graph):
    n = len(graph)
    min_cost = float('inf')
    best_path = []

    for path in permutations(range(1, n)):
        cost = 0
        k = 0

        for j in path:
            cost += graph[k][j]
            k = j

        cost += graph[k][0]

        if cost < min_cost:
            min_cost = cost
            best_path = [0] + list(path) + [0]

    return min_cost, best_path

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cost, path = tsp(graph)

print("Optimal Path:", path)
print("Minimum Cost:", cost)