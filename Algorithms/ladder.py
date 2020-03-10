def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = [-100000 for el in range(n+1)]
    print(count_steps_td(n, a, d))


def count_steps_td(n, a, d):
    if n == 0:
        return 0
    if n == 1:
        return a[0]
    if d[n] == -100000:
        step1 = count_steps_td(n-1, a, d)
        step2 = count_steps_td(n-2, a, d)
        d[n] = max(a[n-1] + step1, a[n-1] + step2)
    return d[n]


def count_steps_bu():
    input()
    c = p = 0
    for s in input().split():
        p, c = c, max(c, p) + int(s)
    print(c)


if __name__ == '__main__':
    main()
