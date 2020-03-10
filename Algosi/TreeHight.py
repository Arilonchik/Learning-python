import sys


sys.setrecursionlimit(20000)


def check_height(r):
    height = 1
    for child in children[r]:
        height = max(height, 1 + check_height(child))
    return height


children = {i: [] for i in range(int(input()))}
for key, value in enumerate(map(int, input().split())):
    if value != -1:
        children[value].append(key)
    else:
        root = key
print(check_height(root))
