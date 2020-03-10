from collections import deque


def main():
    buf_size, num_pac = map(int, input().split())
    packs = deque()
    for _ in range(num_pac):
        st, dur = map(int, input().split())
        packet = {'start_time': st, 'duration': dur}
        packs.append(packet)
    proc(packs, buf_size)


def proc(packets, buf_size):
    buf = deque()
    while len(packets):
        packet = packets.popleft()
        if len(buf) == 0:
            print(packet['start_time'])
            buf.append(packet['start_time'] + packet['duration'])
            continue
        if len(buf) == buf_size:
            if buf[0] <= packet['start_time']:
                if buf[-1] < packet['start_time']:
                    print(packet['start_time'])
                    buf.append(packet['start_time'] + packet['duration'])
                else:
                    print(buf[-1])
                    buf.append(buf[-1] + packet['duration'])
                buf.popleft()
            else:
                print(-1)
            continue
        if len(buf) < buf_size:
            if buf[-1] < packet['start_time']:
                print(packet['start_time'])
                buf.append(packet['start_time'] + packet['duration'])
            else:
                print(buf[-1])
                buf.append(buf[-1] + packet['duration'])


if __name__ == '__main__':
    main()



####################################
import sys
from collections import deque

if __name__ == '__main__':
    reader = (map(int, s.split()) for s in sys.stdin)
    size, n = next(reader)
    times = deque()
    for a, d in reader:
        while times and times[0] <= a:
            times.popleft()
        if len(times) < size:
            if times:
                a = max(a, times[-1])
            print(a)
            times.append(a+d)
        else:
            print(-1)
