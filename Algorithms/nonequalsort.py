def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = count_sort(a, n)
    print(s)


def count_sort(a, n):
    b = {el: 0 for el in range(11)}
    for i in range(n):
        b[a[i]] += 1
    ans = ''
    for key in b.keys():
        ans += (str(key) + ' ') * b[key]
    return ans


if __name__ == '__main__':
    main()
