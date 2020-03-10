def main():
    """
    The whole algorithm is built on a stack of brackets. Opening brackets are adding to it during iteration.
    The check happens this way: if the last opening bracket is the same type as the current one closing =>
    iteration continues, otherwise return 'false'.
    If at the end the stack of opening brackets is not empty => return 'false'
    : return: true / false
    :return: true/false
    """
    stack = []
    for bracket in input():
        if bracket in ['(', '[', '{']:
            stack.append(bracket)
        elif bracket in [')', ']', '}']:
            if len(stack) == 0:
                return 'false'
            top = stack.pop()
            if (bracket == '}' and top != '{') or \
                    (bracket == ')' and top != '(') or \
                    (bracket == ']' and top != '['):
                return 'false'
    return 'true' if len(stack) == 0 else 'false'


if __name__ == '__main__':
    print(main())
