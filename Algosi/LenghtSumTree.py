import sys

sys.setrecursionlimit(300000)


class AvlTree:

    def __init__(self, n):
        self.last_sum = 0
        self.keys = []
        self.left_child = [-1 for _ in range(n + 1)]
        self.right_child = [-1 for _ in range(n + 1)]
        self.parent = [-1 for _ in range(n + 1)]
        self.root = -1
        self.max_value = -1
        self.sum = [0 for _ in range(n + 1)]

    def __count_sum(self, v):
        if self.left_child[v] != -1:
            left = self.sum[self.left_child[v]]
        else:
            left = 0
        if self.right_child[v] != -1:
            right = self.sum[self.right_child[v]]
        else:
            right = 0
        self.sum[v] = self.keys[v] + left + right

    def search(self, k, v):
        if self.root == -1:
            return False, -1
        if self.keys[v] == k:
            self.splay(v)
            return True, self.root
        if k < self.keys[v] and self.left_child[v] != -1:
            return self.search(k, self.left_child[v])
        if k > self.keys[v] and self.right_child[v] != -1:
            return self.search(k, self.right_child[v])
        return False, v

    def add(self, k):
        if self.max_value < k:
            self.max_value = k
        if self.root == -1:
            self.keys.append(k)
            index = len(self.keys) - 1
            self.root = index
            self.sum[index] = k
            return
        fl, v = self.search(k, self.root)
        if not fl:
            self.keys.append(k)
            index = len(self.keys) - 1
            self.parent[index] = v
            if k < self.keys[v]:
                self.left_child[v] = index
            if k > self.keys[v]:
                self.right_child[v] = index
            self.sum[index] = k
            self.splay(index)

    def __zig(self, v, p, variation):
        if p == self.root:
            self.root = v
        else:
            fl = self.check_child(p, self.parent[p])
            if fl == 'l':
                self.left_child[self.parent[p]] = v
            if fl == 'r':
                self.right_child[self.parent[p]] = v

        self.parent[v] = self.parent[p]
        self.parent[p] = v
        if variation == 'l':
            self.left_child[p] = self.right_child[v]
            if self.parent[self.left_child[p]] != -1:
                self.parent[self.left_child[p]] = p
            self.right_child[v] = p
        if variation == 'r':
            self.right_child[p] = self.left_child[v]
            if self.parent[self.right_child[p]] != -1:
                self.parent[self.right_child[p]] = p
            self.left_child[v] = p

    def __zag(self, v, p, variation):
        if p == self.root:
            self.root = v
        else:
            fl = self.check_child(p, self.parent[p])
            if fl == 'l':
                self.left_child[self.parent[p]] = v
            if fl == 'r':
                self.right_child[self.parent[p]] = v

        self.parent[v] = self.parent[p]
        self.parent[p] = v
        if variation == 'l':
            self.left_child[p] = self.right_child[v]
            if self.parent[self.left_child[p]] != -1:
                self.parent[self.left_child[p]] = p
            self.right_child[v] = p
        if variation == 'r':
            self.right_child[p] = self.left_child[v]
            if self.parent[self.right_child[p]] != -1:
                self.parent[self.right_child[p]] = p
            self.left_child[v] = p

    def splay(self, v):
        while self.parent[v] != -1:
            p = self.parent[v]
            g_p = self.parent[p]
            fl = self.check_child(v, p)
            if g_p == -1:
                self.__zig(v, p, fl)
                self.__count_sum(p)
                self.__count_sum(v)
            else:
                fl_gp = self.check_child(p, g_p)
                if fl == fl_gp:
                    self.__zig(p, g_p, fl)
                    self.__zig(v, p, fl)

                else:
                    self.__zig(v, p, fl)
                    self.__zag(v, self.parent[v], fl_gp)
                self.__count_sum(g_p)
                self.__count_sum(p)
                self.__count_sum(v)

    def check_child(self, v, p):
        if self.left_child[p] == v:
            return 'l'
        if self.right_child[p] == v:
            return 'r'
        return None

    def split(self, k, rot, ver=None):
        if self.root == -1:
            return -1, -1
        if ver is None:
            ver = self.root
        fl, v = self.search(k, ver)
        if not fl:
            self.splay(v)
        if self.keys[v] < k:
            right_tree = self.right_child[v]
            self.right_child[v] = -1
            self.parent[right_tree] = -1
            return v, right_tree

        if self.keys[v] > k:
            left_tree = self.left_child[v]
            self.left_child[v] = -1
            self.parent[left_tree] = -1
            return left_tree, v

        if self.keys[v] == k:
            if rot == 'l':
                right_tree = self.right_child[v]
                self.right_child[v] = -1
                self.parent[right_tree] = -1
                return v, right_tree
            if rot == 'r':
                left_tree = self.left_child[v]
                self.left_child[v] = -1
                self.parent[left_tree] = -1
                return left_tree, v

    def merge(self, v1, v2):
        if v1 != -1:
            fl, max_u = self.search(self.max_value + 1, v1)
            self.splay(max_u)
            self.right_child[max_u] = v2
            if v2 != -1:
                self.parent[v2] = max_u
            self.root = max_u
        else:
            self.root = v2

    def remove(self, k):
        fl, v = self.search(k, self.root)
        if fl:
            self.splay(v)
            left = self.left_child[v]
            right = self.right_child[v]
            self.parent[left] = -1
            self.parent[right] = -1
            self.left_child[v] = -1
            self.right_child[v] = -1
            if left == -1:
                self.root = right
            elif right == -1:
                self.root = left
            else:
                self.merge(left, right)

    def summary(self, l, r):
        l_left, l_right = self.split(l-1, 'l')
        if l_left != -1:
            self.__count_sum(l_left)
        if l_right != -1:
            self.__count_sum(l_right)
        r_left, r_right = self.split(r, 'l', l_right)
        if r_left != -1:
            self.__count_sum(r_left)
        if r_right != -1:
            self.__count_sum(r_right)
        s = self.sum[r_left]

        self.merge(r_left, r_right)
        self.merge(l_left, self.root)
        self.last_sum = s
        return s

    def in_order(self, v):
        if len(self.keys) == 0:
            return
        if self.left_child[v] != -1:
            self.in_order(self.left_child[v])
        print(self.keys[v], end=' ')
        if self.right_child[v] != -1:
            self.in_order(self.right_child[v])


def main():
    n = int(input())
    tree = AvlTree(n)
    commands = {'+': tree.add, '-': tree.remove, '?': tree.search}
    for i in range(n):
        com, *inp = input().split()
        inp[0] = (tree.last_sum + int(inp[0])) % 1000000001
        #inp[0] = int(inp[0])
        #print('inp =', com, inp[0])
        if com == '?':
            fl, v = tree.search(inp[0], tree.root)
            print('Found' if fl else 'Not found')
        if com == '+':
            tree.add(inp[0])
        if com == '-':
            tree.remove(inp[0])
        if com == 's':
            #inp[1] = int(inp[1])
            inp[1] = (tree.last_sum + int(inp[1])) % 1000000001
            #print('inp =', inp[1])
            print(tree.summary(inp[0], inp[1]))
        #tree.in_order(tree.root)
        #print('')
        #print(tree.last_sum, 'last_sum')


if __name__ == '__main__':
    main()
