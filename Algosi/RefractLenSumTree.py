class TreeNode:
    def __init__(self, k, p, l_c, r_c):
        self.key = k
        self.parent = p
        self.left_child = l_c
        self.right_child = r_c
        self.rang = 0
        self.count_sum()

    def count_sum(self):
        self.rang = self.key
        if self.left_child is not None:
            self.rang += self.left_child.rang
        if self.right_child is not None:
            self.rang += self.right_child.rang


class SplayTree:
    def __init__(self):
        self.nodes = []
        self.root = None
        self.max_value = -1
        self.last_sum = 0

    def search(self, k, node):
        if self.root is None:
            return False, None
        while node.key != k:
            if k < node.key and node.left_child is not None:
                node = node.left_child
            elif k > node.key and node.right_child is not None:
                node = node.right_child
            else:
                return False, node
        self.splay(node)
        return True, node

    def add(self, k):
        if self.max_value < k:
            self.max_value = k
        fl, node = self.search(k, self.root)

        if not fl:
            new_node = TreeNode(k, node, None, None)
            self.nodes.append(new_node)
            if node is None:
                self.root = new_node
                return
            if k > node.key:
                node.right_child = new_node
            if k < node.key:
                node.left_child = new_node
            self.splay(new_node)

    def check_child(self, v, p):
        if p.left_child == v:
            return 'l'
        if p.right_child == v:
            return 'r'
        return None

    def __zig(self, v, p, variation):
        if self.root == p:
            self.root = v
        else:
            fl = self.check_child(p, p.parent)
            if fl == 'l':
                p.parent.left_child = v
            if fl == 'r':
                p.parent.right_child = v

        v.parent = p.parent
        p.parent = v
        if variation == 'l':
            p.left_child = v.right_child
            if p.left_child is not None:
                p.left_child.parent = p
            v.right_child = p
        if variation == 'r':
            p.right_child = v.left_child
            if p.right_child is not None:
                p.right_child.parent = p
            v.left_child = p

    def __zag(self, v, p, variation):
        if p == self.root:
            self.root = v
        else:
            fl = self.check_child(p, p.parent)
            if fl == 'l':
                p.parent.left_child = v
            if fl == 'r':
                p.parent.right_child = v

        v.parent = p.parent
        p.parent = v
        if variation == 'l':
            p.left_child = v.left_child
            if p.left_child is not None:
                p.left_child.parent = p
            v.right_child = p
        if variation == 'r':
            p.right_child = v.left_child
            if p.right_child is not None:
                p.right_child.parent = p
            v.left_child = p

    def splay(self, v):
        while v.parent is not None:
            p = v.parent
            g_p = p.parent
            fl = self.check_child(v, p)
            if g_p is None:
                self.__zig(v, p, fl)
                p.count_sum()
                v.count_sum()
            else:
                fl_gp = self.check_child(p, g_p)
                if fl == fl_gp:
                    self.__zig(p, g_p, fl)
                    self.__zig(v, p, fl)

                else:
                    self.__zig(v, p, fl)
                    self.__zag(v, v.parent, fl_gp)
                g_p.count_sum()
                p.count_sum()
                v.count_sum()

    def split(self, k, tree_root):
        fl, v = self.search(k, tree_root)

        if v.key <= k:
            right_tree = v.right_child
            v.right_child = None
            right_tree.parent = None
            return v, right_tree

        if v.key > k:
            left_tree = v.left_child
            v.left_child = None
            left_tree.parent = None
            return left_tree, v

    def merge(self, v1, v2):
        if v1 is not None:
            fl, max_u = self.search(self.max_value + 1, v1)
            max_u.right_child = v2
            if v2 is not None:
                v2.parent = max_u
            self.root = max_u
        else:
            self.root = v2

    def remove(self, k):
        fl, v = self.search(k, self.root)
        if fl:
            left, right = self.split(k, self.root)
            left.left_child.parent = None
            left.left_child = None
            self.merge(left.left_child, right)
            self.root = left.left_child
            del left

    def in_order(self, v):
        if v.left_child is not None:
            self.in_order(v.left_child)
        print(v.key, end=' ')
        if v.right_child is not None:
            self.in_order(v.right_child)


def main():
    n = int(input())
    tree = SplayTree()
    for _ in range(n):
        comm, data = input().split()
        if comm == '+':
            tree.add(int(data))
        if comm == '-':
            tree.remove(int(data))
        tree.in_order(tree.root)


if __name__ == '__main__':
    main()
