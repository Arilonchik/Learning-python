import random

st = 'b'
with open('input_str10_8_words100.txt', 'w') as fh:
    fh.write('100000000\n')
    for _ in range(100000000):
        wr_s = str(random.randint(0, 100000)) + ' ' + (st*100) + '\n'
        fh.write(wr_s)

