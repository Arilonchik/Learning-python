def main():
    n = int(input())
    teams = {}
    for _ in range(n):
        result = input().split(';')
        if result[0] not in teams.keys():
            teams[result[0]] = [0, 0, 0, 0, 0]
        if result[2] not in teams.keys():
            teams[result[2]] = [0, 0, 0, 0, 0]
        teams[result[0]][0] += 1
        teams[result[2]][0] += 1
        if result[1] > result[3]:
            teams[result[0]][1] += 1
            teams[result[2]][3] += 1
            teams[result[0]][4] += 3
        if result[1] < result[3]:
            teams[result[0]][3] += 1
            teams[result[2]][1] += 1
            teams[result[2]][4] += 3
        if result[1] == result[3]:
            teams[result[0]][2] += 1
            teams[result[2]][2] += 1
            teams[result[2]][4] += 1
            teams[result[0]][4] += 1
    for key, el in teams.items():
        print(key + ':' + ' '.join(map(str, el)))


if __name__ == '__main__':
    main()
