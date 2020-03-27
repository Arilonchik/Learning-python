import sys

sys.setrecursionlimit(10**5)


class BinaryTree:
    def __init__(self, n):
        self.keys = [-1 for _ in range(n+1)]
        self.left_children = [-1 for _ in range(n+1)]
        self.right_children = [-1 for _ in range(n+1)]
        self.tree_option = None

    def add_v(self, key, ver, l_c, r_c):
        self.keys[ver] = key
        self.left_children[ver] = l_c
        self.right_children[ver] = r_c

    def in_order(self, v, prev_key=(-2**31)-1, prev_v=0):
        if self.left_children[v] != -1:
            prev_key, prev_v = self.in_order(self.left_children[v], prev_key, v)
        if (prev_key > self.keys[v]) or (prev_key == self.keys[v] and self.left_children[v] == prev_v):
            self.tree_option = 'INCORRECT'
            return prev_key, v
        prev_key = self.keys[v]
        if self.right_children[v] != -1:
            prev_key, prev_v = self.in_order(self.right_children[v], self.keys[v], v)
        return prev_key, v


def main():
    n = int(input())
    b_t = BinaryTree(n)
    for i in range(n):
        key, l_c, r_c = map(int, input().split())
        b_t.add_v(key, i, l_c, r_c)
    b_t.in_order(0)
    print(b_t.tree_option or 'CORRECT')


if __name__ == '__main__':
    main()
