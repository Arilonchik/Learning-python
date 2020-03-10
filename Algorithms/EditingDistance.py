from functools import lru_cache
import sys

def main():
    a = input()
    b = input()
    print(editting_distance(a, b))


def editting_distance(a, b):
    n = len(a)
    m = len(b)
    d = [[0 for el in range(n + 1)] for g in range(m + 1)]
    d[0] = [el for el in range(n+1)]
    for k in range(m+1):
        d[k][0] = k
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            c = diff(a[j-1], b[i-1])
            d[i][j] = min(min(d[i-1][j] + 1, d[i][j-1] + 1), d[i-1][j-1] + c)
    return d[m][n]


def diff(a, b):
    if a != b:
        return 1
    else:
        return 0
##############
# Практика


def edit_distanse(s1, s2):
    n=1
    m=2
    # d = [[0]*n] * m - неправильный способ инициализировать матрицу все строчки будут ссылками на первую
    d1 = [[0]*n for _ in range(m)]  # парвильный способ
    @lru_cache(maxsize=None)
    def d(i, j):
        if i == 0 or j == 0:
            return max(i, j)
        else:
            return min(d(i, j-1)+1,
                       d(i-1, j) + 1,
                       d(i-1, j-1) + (s1[i-1] != s2[j-1]))

    return d(len(s1), len(s2))


if __name__ == '__main__':
    sys.setrecursionlimit(10000)    # Меняем ограничение глубины рекурсии
    main()
