import sys

sys.setrecursionlimit(3000)


class SearchTree:
    def __init__(self, n):
        self.keys = [-1 for _ in range(n+1)]
        self.left_children = [-1 for _ in range(n+1)]
        self.right_children = [-1 for _ in range(n+1)]
        self.parent = [-1 for _ in range(n + 1)]

    def search(self, target_key, ver=0):
        if self.keys[ver] == target_key:
            return True, ver
        if self.keys[ver] > target_key:
            if self.keys[self.left_children[ver]] != -1:
                return self.search(target_key, self.left_children[ver])
            else:
                return False, ver
        if self.keys[ver] < target_key:
            if self.keys[self.right_children[ver]] != -1:
                return self.search(target_key, self.right_children[ver])
            else:
                return False, ver

    def __adding(self, key, ver, l_c, r_c):
        self.keys[ver] = key
        self.left_children[ver] = l_c
        self.right_children[ver] = r_c

    def add_v(self, key, ver, l_c, r_c):
        if ver == 0:
            self.__adding(key, ver, l_c, r_c)
            return False
        k, sup_ver = self.search(key)
        if self.keys[sup_ver] > key:
            if ver == self.left_children[sup_ver]:
                self.__adding(key, ver, l_c, r_c)
                return False
        if self.keys[sup_ver] < key:
            if ver == self.right_children[sup_ver]:
                self.__adding(key, ver, l_c, r_c)
                return False
        return True


def main():
    n = int(input())
    b_t = SearchTree(n)
    for i in range(n):
        key, l_c, r_c = map(int, input().split())
        fl = b_t.add_v(key, i, l_c, r_c)
        if fl:
            print("INCORRECT")
            return
    print("CORRECT")


if __name__ == '__main__':
    main()
