def main():
    parents = {}
    n = int(input())
    for _ in range(n):
        a = input().split()
        parents[a[0]] = [] if len(a) == 1 else a[2:]

    q = int(input())
    exceptions = []
    for _ in range(q):
        exc = input()
        exceptions.append(exc)
    for ex in check_useless(exceptions, parents):
        print(ex)


def is_parent(child, parent, par):
    return child == parent or any(map(lambda p: is_parent(p, parent, par), par[child]))


def check_useless(ex, par):
    used = []
    useless = []
    for e in ex:
        for u in used:
            if is_parent(e, u, par):
                useless.append(e)
                break
        used.append(e)
    return useless


if __name__ == '__main__':
    main()
