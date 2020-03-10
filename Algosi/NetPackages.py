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
        if len(buf) <= buf_size:
            if buf[0] <= packet['start_time']:
                if buf[-1] < packet['start_time']:
                    print(packet['start_time'])
                    buf.append(packet['start_time'] + packet['duration'])
                else:
                    print(buf[-1])
                    buf.append(buf[-1] + packet['duration'])
                if len(buf) > buf_size:
                    buf.popleft()
            else:
                print(-1)


if __name__ == '__main__':
    main()
