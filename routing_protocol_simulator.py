import random
import copy

INF = float('inf')

n = int(input("Enter number of routers: "))
min_cost, max_cost = 1, 10
cost = [[0 if i == j else random.randint(min_cost, max_cost) if random.random() < 0.6 else INF
         for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        cost[j][i] = cost[i][j]

def display_table(title, table):
    print(f"\n{title}")
    for i, row in enumerate(table):
        formatted = ['∞' if x == INF else int(x) for x in row]
        print(f"Router {i+1}: {formatted}")

display_table("Generated Cost Matrix:", cost)

distance = copy.deepcopy(cost)
display_table("Initial Routing Tables:", distance)

iteration = 0
updated = True

while updated:
    iteration += 1
    updated = False

    print(f"\n--- Iteration {iteration} ---")
    new_distance = copy.deepcopy(distance)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if cost[i][k] != INF and distance[k][j] != INF:
                    if new_distance[i][j] > cost[i][k] + distance[k][j]:
                        new_distance[i][j] = cost[i][k] + distance[k][j]
                        updated = True

    distance = new_distance
    display_table(f"Routing Tables after Iteration {iteration}:", distance)

print("\nAll routers have converged.")
display_table("Final Routing Tables (Shortest Path Costs):", distance)
