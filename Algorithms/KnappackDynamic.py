def main():
    w_backpack, n = map(int, input().split())
    weights = list(map(int, input().split()))
    print(backpack_max_w(w_backpack, weights))


def backpack_max_w(w_backpack, weights):
    d = [[0 for j in range(w_backpack + 1)] for k in range(len(weights) + 1)]
    for i in range(1, len(weights)+1):
        for w in range(1, w_backpack+1):
            d[i][w] = d[i-1][w]
            if weights[i-1] <= w:
                d[i][w] = max(d[i][w], d[i-1][w - weights[i-1]] + weights[i-1])
    return d[len(weights)][w_backpack]


# Храним только текущую и предыдущу. строки матрицы
def not_mine_backpack():
    vol, n = map(int, input().split())
    weights = [*map(int, input().split())]
    vol1 = vol + 1
    prev, cur = [0] * vol1, [0] * vol1
    for w in weights:
        prev, cur = cur, prev
        for v in range(vol1):
            cur[v] = prev[v] if w > v else max(prev[v], prev[v - w] + w)
    print(cur[-1])


if __name__ == '__main__':
    main()
