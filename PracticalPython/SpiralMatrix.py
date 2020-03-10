def main():
    n = int(input())
    matrix = [[None for _ in range(n)] for m in range(n)]
    i = 0
    j = 0
    flag = ['gor+', 'ver+', 'gor-', 'ver-']
    flag_index = 0
    for number in range(1, n**2 + 1):
        if matrix[i][j] is None:
            if flag[flag_index % len(flag)] == 'gor+':
                matrix[i][j] = number
                j += 1
                if j == len(matrix[0]):
                    flag_index += 1
                    j -= 1
            if flag[flag_index % len(flag)] == 'ver+':
                matrix[i][j] = number
                i += 1
                if i == len(matrix):
                    flag_index += 1
                    i -= 1
            if flag[flag_index % len(flag)] == 'gor-':
                matrix[i][j] = number
                j -= 1
                if j == -1:
                    flag_index += 1
                    j += 1
            if flag[flag_index % len(flag)] == 'ver-':
                matrix[i][j] = number
                i -= 1
                if i == -1:
                    flag_index += 1
                    i += 1
        else:
            if flag[flag_index % len(flag)] == 'gor+':
                flag_index += 1
                j -= 1
                i += 1
                matrix[i][j] = number
                i += 1
            elif flag[flag_index % len(flag)] == 'ver+':
                flag_index += 1
                i -= 1
                j -= 1
                matrix[i][j] = number
                j -= 1
            elif flag[flag_index % len(flag)] == 'gor-':
                flag_index += 1
                j += 1
                i -= 1
                matrix[i][j] = number
                i -= 1
            elif flag[flag_index % len(flag)] == 'ver-':
                flag_index += 1
                i += 1
                j += 1
                matrix[i][j] = number
                j += 1
    for r in matrix:
        print(' '.join(map(str, r)))


if __name__ == '__main__':
    main()
