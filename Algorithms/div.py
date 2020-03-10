def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if b > a:
        return gcd(a, b % a)
    if a >= b:
        return gcd(a % b, b)


def gcd_2(a, b):
    return gcd(b, a % b) if b else a


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()