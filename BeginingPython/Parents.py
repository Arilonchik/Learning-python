def main():
    classes = {}
    n = int(input())
    for i in range(n):
        cl, *chil = input().split()
        if len(chil) != 0:
            del(chil[0])
        classes[cl] = chil

    q = int(input())
    for i in range(q):
        first, second = input().split()
        print(check(first, second, classes))


def check(first, second, classes):
    if second not in classes.keys() or first not in classes.keys():
        return "No"
    if first == second:
        return "Yes"
    if len(classes[second]) == 0:
        return "No"
    for parent in classes[second]:
        if parent == first:
            return "Yes"
    for parent in classes[second]:
        ans = check(first, parent, classes)
        if ans == "Yes":
            return "Yes"
    return "No"

    # ищем у секонд предка фирст
##############################################


n = int(input())

parents = {}
for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]


def is_parent(child, parent):
    return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))


q = int(input())
for _ in range(q):
    a, b = input().split()
    print("Yes" if is_parent(b, a) else "No")

    
if __name__ == '__main__':
    main()

