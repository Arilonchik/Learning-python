import os
import tempfile


class File:
    counter = 0

    def __init__(self, path):
        if not os.path.exists(path):
            open(path, 'w').close()
        self.path = path

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def write(self, st):
        with open(self.path, 'w') as f:
            f.write(st)

    def __add__(self, other):
        new_path = os.path.join(tempfile.gettempdir(), f'temp_file{File.counter}')
        first = self.read()
        second = other.read()
        new_file = File(new_path)
        new_file.write(first + second)
        return new_file

    def __str__(self):
        return self.path

    def __iter__(self):
        with open(self.path, 'r') as f:
            return f.readlines().__iter__()


if __name__ == '__main__':
    fl = File('ke.txt')
    print(fl.read())
    fl.write('sdfgvbfdsdcvf\n')
    fl2 = File('le.txt')
    fl2.write('kcdcidcdcm\n')
    print(fl2.read())
    fl3 = fl + fl2
    print(fl3.read())
    print(fl3)
    for l in fl3:
        print(l)
        print('kek')