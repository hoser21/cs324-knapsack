def knapsack_r(w, weights, vals, index):
    if index >= len(weights):
        return 0
    if w - weights[index] < 0:
        return knapsack_r(w, weights, vals, index + 1)
    return max(knapsack_r(w - weights[index], weights, vals, index + 1) + vals[index],
        knapsack_r(w, weights, vals, index + 1))


def knapsack(w, weights, vals):
    if len(weights) != len(vals):
        return -1
    if w < 0:
        return -1
    for i in range(len(weights)):
        if weights[i] < 0 or vals[i] < 0:
            return -1
    return knapsack_r(w, weights, vals, 0)


def main():
    weights = [1, 2, 3, 1]
    vals = [6, 10, 12, 7]
    w = 5
    print(knapsack(w, weights, vals))

if __name__ == "__main__":
    main()