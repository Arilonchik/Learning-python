import sys


def binary_search(a, bi):
    left = 0
    right = len(a)-1
    while left <= right:
        m = (left + right) // 2
        if a[m] == bi:
            return m
        elif a[m] > bi:
            right = m-1
        else:
            left = m + 1
    return -2


def main():
    n, *a = map(int, input().split())
    k, *b = map(int, input().split())
    indexes = []
    for i in range(k):
        j = binary_search(a, b[i])
        indexes.append(j + 1)
    print(' '.join(map(str, indexes)))
#################################
# Практика


def main2():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *xs = next(reader)
    k, *queries = next(reader)
    for query in queries:
        print(find_pos(xs, query), end=" ")


def find_pos(xs, query):
    # Invariant: lo <= pos < hi
    lo, hi = 0, len(xs)
    while lo < hi:
        mid = (lo + hi) // 2
        if query < xs[mid]:
            hi = mid       # [lo, mid)
        elif query > xs[mid]:
            lo = mid + 1      # [mid+1 hi]
        else:
            return mid + 1
    return -1
    # try:
    #     return xs.index(query) + 1
    # except ValueError:
    #     return -1


def test():
    pass

if __name__ == '__main__':
    main2()
