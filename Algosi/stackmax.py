def main():
    q = int(input())
    main_stack = []
    max_stack = []
    for _ in range(q):
        com = input().split()
        if com[0] == 'push':
            main_stack.append(int(com[1]))
            if len(max_stack) == 0:
                max_stack.append(int(com[1]))
            elif int(com[1]) > max_stack[-1]:
                max_stack.append(int(com[1]))
            else:
                max_stack.append(max_stack[-1])
        if com[0] == 'pop':
            main_stack.pop()
            max_stack.pop()
        if com[0] == 'max':
            print(max_stack[-1])


if __name__ == '__main__':
    main()
