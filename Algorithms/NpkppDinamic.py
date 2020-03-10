import bisect

def main():
    n = int(input())
    a = list(map(int, input().split()))
    l, a = min_lds(a, n)
    print(l)
    print(" ".join(a))


def min_lds(a, n):
    d = [-1 for i in range(n + 1)]
    pos = [0 for i in range(n + 1)]
    prev = [0 for i in range(n)]
    pos[n] = -1
    lenght = 0
    d[n] = 1000000001
    for i in range(n):
        j = bisect.bisect_left(d, a[i]) - 1
        if d[j + 1] >= a[i] >= d[j]:
            d[j] = a[i]
            pos[j] = i
            prev[i] = pos[j+1]
            lenght = max(lenght, n - j)
    pos.reverse()
    p = pos[lenght]
    ans = []
    while p != -1:
        ans.append(str(p + 1))
        p = prev[p]
    ans.reverse()
    return lenght, ans



def max_crat():
    n = int(input())
    a = list(map(int, input().split()))
    ans = max_crat(a, n)
    print(ans)
    lenght = [0 for i in range(n)]
    for i in range(n):
        lenght[i] = 1
        for j in range(i):
            if lenght[j] + 1 > lenght[i] and a[i] % a[j] == 0:
                lenght[i] = lenght[j] + 1
    return max(lenght)


if __name__ == '__main__':
    main()
