def main():
    s, t = (input() for _ in range(2))
    pos = 0
    ans = 0
    while s.find(t, pos) != -1:
        pos = s.find(t, pos) + 1
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
