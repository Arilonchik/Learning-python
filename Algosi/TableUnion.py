import sys
sys.setrecursionlimit(10000)


def main():
    n, m = map(int, input().split())
    parent = [i for i in enumerate(map(int, input().split()))]
    max_value = max(parent, key=lambda x: x[1])[1]
    for _ in range(m):
        t1, t2 = map(int, input().split())
        t1 -= 1
        t2 -= 1
        # из t2 в t1
        main_table = find(t1, parent)
        add_table = find(t2, parent)
        if main_table[0] == add_table[0]:
            print(max_value)
            continue
        current_value = main_table[1] + add_table[1]
        parent[main_table[0]] = (main_table[0], current_value)
        parent[add_table[0]] = (main_table[0], 0)
        if max_value < current_value:
            max_value = current_value
        print(max_value)


def find(i, parent):
    if parent[i][0] != i:
        parent[i] = find(parent[i][0], parent)
    return parent[i]


if __name__ == '__main__':
    main()
