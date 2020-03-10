def main():
    stack = []
    mistake = 0
    bracket_stack = []
    counter = 0
    for bracket in input():
        counter += 1
        mistake += 1
        if bracket in ['(', '[', '{']:
            stack.append(bracket)
            bracket_stack.append(counter)
        elif bracket in [')', ']', '}']:
            if len(stack) == 0:
                return mistake
            top = stack.pop()
            if (bracket == '}' and top != '{') or \
                    (bracket == ')' and top != '(') or \
                    (bracket == ']' and top != '['):
                return mistake
            bracket_stack.pop()
    return 'Success' if len(stack) == 0 else bracket_stack[0]


if __name__ == '__main__':
    print(main())
