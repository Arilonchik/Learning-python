def main():
    s = input()
    a = input()
    b = input()
    print(check(s, a, b))


def check(s, a, b):
    counter = 0
    while a in s and counter < 1000:
        counter += 1
        s = s.replace(a, b)
    return counter if counter <= 999 else "Impossible"


if __name__ == '__main__':
    main()
