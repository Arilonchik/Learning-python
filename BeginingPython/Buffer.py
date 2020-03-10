class Buffer:
    def __init__(self):
        self.current_part = []

    def add(self, *a):
        self.current_part.extend(a)
        while len(self.current_part) >= 5:
            print(sum(self.current_part[0:5]))
            self.current_part = self.current_part[5::]

    def get_current_part(self):
        return self.current_part


if __name__ == '__main__':
    buf = Buffer()
    buf.add(1, 2, 3)
    print(buf.get_current_part())  # вернуть [1, 2, 3]
    buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
    print(buf.get_current_part())  # вернуть [6]
    buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
    print(buf.get_current_part() ) # вернуть []
    buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
    print(buf.get_current_part())  # вернуть [1]