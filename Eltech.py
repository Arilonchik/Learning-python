import math

while True:
    com = input()
    if com == 'a':
        p, q = map(float, input().split('+j'))
        print('p=', p)
        print('q=j*', q)
        am = math.sqrt((p**2) + q**2)
        print('Am=', am)
        if p > 0:
            psi = math.degrees(math.atan(q/p))
        if p < 0:
            psi = math.degrees(math.atan(q/p)) + 180
        print('psi =', psi)
        print(f'ans={am}*e^j{psi}')
    if com == 'c':
        am, psi = map(float, input().split('e'))
        print('Am=', am)
        print('psi=', psi)
        p = am*(math.cos(math.radians(psi)))
        q = am*(math.sin(math.radians(psi)))
        print(f'p={p}, q={q}')
        print(f'ans = {p} {q}j')