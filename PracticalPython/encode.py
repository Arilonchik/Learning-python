def main():
    cl = {_: [] for _ in range(1, 12)}
    with open('f1.txt') as fh:
        for line in fh.readlines():
            student = line.split('\t')
            cl[int(student[0])].append(int(student[2]))
    for i in range(1, 12):
        if len(cl[i]) != 0:
            print(i, round(sum(cl[i]) / len(cl[i]), 5))
        else:
            print(i, '-')


if __name__ == '__main__':
    main()
