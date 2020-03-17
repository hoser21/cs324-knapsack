import random

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


def knapsack_db(w, weights, vals):
    t = [[0 for i in range(w + 1)] for j in range(len(vals) + 1)]
    for i in range(1, len(vals) + 1):
        for j in range(1, w + 1):
            if weights[i - 1] > j:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = max(t[i-1][j], t[i-1][j-weights[i-1]] + vals[i-1])
    #print(t)
    return t[len(vals)][w]



def main():
    random.seed(0)
    weights = [random.randint(1, 20) for i in range(30)]    
    vals = [random.randint(1, 50) for i in range(30)] 
    w = 70
    print('Total db: {}'.format(knapsack_db(w, weights, vals)))
    print('Total recursive:', knapsack(w, weights, vals))


if __name__ == "__main__":
    main()