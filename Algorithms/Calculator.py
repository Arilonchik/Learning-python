def main():
    n = int(input())
    a, b = count_k(n)
    print(a)
    print(' '.join(map(str, b)))


def count_k(n):
    d = [0 for el in range(n + 1)]
    pos = [0 for el in range(n + 1)]
    pos[1] = -1
    for i in range(1, n+1):
        s = [i+1, i*2, i*3]
        for j in range(3):
            if s[j] <= n:
                if d[s[j]] == 0 or d[i] + 1 < d[s[j]]:
                    d[s[j]] = d[i] + 1
                    pos[s[j]] = i
    ans = [n]
    p = pos[n]
    while p != -1:
        ans.append(p)
        p = pos[p]
    ans.reverse()
    return d[n], ans


if __name__ == '__main__':
    main()
