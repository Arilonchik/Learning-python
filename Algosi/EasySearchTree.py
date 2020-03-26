class BinaryTree:
    def __init__(self, n):
        self.keys = [-1 for _ in range(n)]
        self.left_children = [-1 for _ in range(n)]
        self.right_children = [-1 for _ in range(n)]

    def add_v(self, key, ver, l_c, r_c):
        self.keys[ver] = key
        self.left_children[ver] = l_c
        self.right_children[ver] = r_c

    def in_order(self, v, prev_v):
        if self.left_children[v] != -1:
            self.in_order(self.left_children[v], v)
        if prev_v > v:
            return 'INCORRECT'
        if self.right_children[v] != -1:
            self.in_order(self.right_children[v], v)


def main():
    n = int(input())
    b_t = BinaryTree(n)
    for i in range(n):
        key, l_c, r_c = map(int, input().split())
        b_t.add_v(key, i, l_c, r_c)
    b_t.in_order(0)


if __name__ == '__main__':
    main()
