def fib(n):
    prev, cur = 0, 1
    for i in range(1,n):
        prev, cur = cur, prev + cur
    return cur


def fib_n(n):
    prev, cur = 0, 1
    for i in range(1, n):
        prev, cur = cur, (prev + cur) % 10
    return cur


def fib_mod(n, m):
    an = [0, 1]
    prev, cur = 0, 1
    for i in range(2, n+1):
        prev, cur = cur, (prev + cur) % m
        an.append(cur)
        if prev == 0 and cur == 1:
            an.pop(len(an)-1)
            an.pop(len(an)-1)
            return an[n % (len(an))]
    return cur%m

def main():
    n = int(input())
    # m = int(input())
    # print(fib_mod(n, m))
    print(fib(31))


if __name__ == "__main__":
    main()
    # 1 2 3 4 5 6 7 8
    # 1 1 2 3 5 8 13 21