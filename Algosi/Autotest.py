def main():
    fl = 1
    n, e, d = map(int, input().split())
    parent = [i for i in range(n+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        parent[find(b, parent)] = find(a, parent)
    for _ in range(d):
        a, b = map(int, input().split())
        par_a = find(a, parent)
        par_b = find(b, parent)
        if par_a == par_b:
            fl = 0
            break
    print(fl)


def find(i, p):
    if p[i] != i:
        p[i] = find(p[i], p)
    return p[i]


if __name__ == '__main__':
    main()
