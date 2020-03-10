import json
from collections import Counter


def main():
    data_json = input()
    classes = json.loads(data_json)
    cnt = Counter()
    gr = {}
    keys = []
    for clas in classes:
        gr[clas["name"]] = set(clas["parents"])
        keys.append(clas["name"])
    keys.sort()
    for cl in gr.keys():
        cos = dfs(gr, cl)
        for i in cos:
            cnt[i] += 1
    for key in keys:
        print(key + ' : ' + str(cnt[key]))


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


if __name__ == '__main__':
    main()
