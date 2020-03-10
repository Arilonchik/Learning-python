def main():
    n = int(input())
    mas = list(map(int, input().split()))
    m = int(input())
    left_stack = [mas[j] for j in range(m)]
    right_stack = []
    max_left = max(left_stack)
    max_right = []
    maximus = [max_left]
    for i in range(m, n):
        if len(right_stack) == 0:
            for _ in range(len(left_stack)):
                num = left_stack.pop()
                right_stack.append(num)
                if len(max_right) == 0:
                    max_right.append(num)
                else:
                    max_right.append(max(num, max_right[-1]))
            max_right.pop()
            right_stack.pop()
            left_stack.append(mas[i])
            max_left = mas[i]
            if len(max_right):
                maximus.append(max(max_right[-1], max_left))
            else:
                maximus.append(max_left)
        else:
            max_right.pop()
            right_stack.pop()
            left_stack.append(mas[i])
            max_left = max(max_left, mas[i])
            if len(max_right):
                maximus.append(max(max_right[-1], max_left))
            else:
                maximus.append(max_left)
    print(' '.join(map(str, maximus)))


if __name__ == '__main__':
    main()
