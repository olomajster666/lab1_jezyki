from functools import lru_cache


def knapsack_procedural(weights, values, capacity):
    n = len(weights)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    max_value = dp[n][capacity]

    w = capacity
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    return max_value, selected_items





@lru_cache(maxsize=None)
def knapsack_recursive(n, capacity, weights, values):
    if n == 0 or capacity == 0:
        return 0

    if weights[n - 1] > capacity:
        return knapsack_recursive(n - 1, capacity, weights, values)

    else:
        take_item = values[n - 1] + knapsack_recursive(n - 1, capacity - weights[n - 1], weights, values)
        leave_item = knapsack_recursive(n - 1, capacity, weights, values)
        return max(take_item, leave_item)


def knapsack_functional(weights, values, capacity):
    n = len(weights)

    max_value = knapsack_recursive(n, capacity, tuple(weights), tuple(values))

    selected_items = []
    w = capacity

    for i in range(n, 0, -1):
        if knapsack_recursive(i, w, tuple(weights), tuple(values)) != knapsack_recursive(i - 1, w, tuple(weights),
                                                                                         tuple(values)):
            selected_items.append(i - 1)
            w -= weights[i - 1]

    return max_value, selected_items



weights = [2, 3, 4, 5]
values = [3, 4, 5, 8]
capacity = 5


print("=== Proceduralne podejście (Programowanie dynamiczne) ===")
max_value_proc, selected_items_proc = knapsack_procedural(weights, values, capacity)
print(f"Maksymalna wartość: {max_value_proc}")
print(f"Wybrane przedmioty: {selected_items_proc}")


print("\n=== Funkcyjne podejście (Rekurencja z memoizacją) ===")
max_value_func, selected_items_func = knapsack_functional(weights, values, capacity)
print(f"Maksymalna wartość: {max_value_func}")
print(f"Wybrane przedmioty: {selected_items_func}")
