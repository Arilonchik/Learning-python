from bs4 import BeautifulSoup
import re
import os


def parse(page):
    result = [0, 0, 0, 0]
    with open(page, encoding='utf-8') as pg:
        html = pg.read()
    soup = BeautifulSoup(html, 'lxml')
    body = soup.find('div', id='bodyContent')

    for image in body.find_all_next('img'):
        try:
            if int(image['width']) >= 200:
                result[0] += 1
        except KeyError:
            continue

    for h in body.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        if re.match(r'^[ECT].*', h.text):
            result[1] += 1

    i = body.find_next()
    last_tag = i.name
    a_counter = 1

    while i and i.find_parent('div', id='bodyContent'):
        i = i.find_next()

        if i is not None and (i.name == 'ul' or i.name == 'ol') and i.find_parent(['ol', 'ul']) is None:
            result[3] += 1

        if i is None or i.find_parent('a') is not None:
            continue
        if i.name == 'a':
            if last_tag == 'a':
                a_counter += 1
                result[2] = max(result[2], a_counter)
        else:
            a_counter = 1
        last_tag = i.name

    print(result)
    return result


def build_bridge(start_page, end_page):
    graph = build_graph()
    level = {gr: [-1, []] for gr in graph.keys()}
    if level[start_page][0] == -1:
        bfs(start_page, level, graph)
    result = level[end_page][1].copy()
    result.append(end_page)
    print(result)
    return result


def check_pages(page):
    with open(page, encoding="utf-8") as file:
        links = re.findall(r"(?<=/wiki/)[\w()]+", file.read())
        checked_links = []
        for link in links:
            if os.path.exists(f'wiki/{link}'):
                checked_links.append(link)
        return set(checked_links)


def get__statistics(start_page, end_page):
    pages = build_bridge(start_page, end_page)
    pages = list(map(lambda x: 'wiki/' + x, pages))
    statistic = {page: parse(page) for page in pages}
    return statistic


def build_graph():
    dirlist = os.listdir('wiki/')
    graph = {}
    for file in dirlist:
        graph[file] = check_pages(f'wiki/{file}')
    return graph


def bfs(s, lvl, adj):
    lvl[s][0] = 0
    queue = [s]
    while queue:
        v = queue.pop(0)
        for w in adj[v]:
            try:
                if lvl[w][0] == -1:
                    queue.append(w)
                    lvl[w][0] = lvl[v][0] + 1

                    lvl[w][1].append(v)
                    for key in lvl[v][1]:
                        lvl[w][1].append(key)
            except KeyError:
                continue


if __name__ == '__main__':
    parse('wiki/Binyamina_train_station_suicide_bombing')
    mem = get__statistics('Stone_Age', 'Python_(programming_language)')
    print(mem)