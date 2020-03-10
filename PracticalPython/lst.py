def main():
    matrix = []
    while True:
        try:
            row = [int(i) for i in input().split()]
        except ValueError:
            break
        matrix.append(row)
    ans =[]
    for row in range(len(matrix)):
        ans.append([])
        for col in range(len(matrix[row])):
            i = row
            j = col
            new_element = matrix[(i+1) % len(matrix)][j] + matrix[(i-1) % len(matrix)][j] + matrix[i][(j+1) % len(matrix[row])] + matrix[i][(j - 1) % len(matrix[row])]
            ans[row].append(new_element)
    for r in ans:
        print(' '.join(map(str, r)))


if __name__ == '__main__':
    main()
