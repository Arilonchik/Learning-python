import heapq


def main():
    n_proc, m_task = map(int, input().split())
    tasks = list(map(int, input().split()))
    procs = [(0, i) for i in range(n_proc)]
    heapq.heapify(procs)
    for task in tasks:
        proc = heapq.heappop(procs)
        print(proc[1], proc[0])
        proc = (proc[0] + task, proc[1])
        heapq.heappush(procs, proc)


if __name__ == '__main__':
    main()
