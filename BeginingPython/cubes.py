from lxml import etree


def main():
    cubes = input()
    parser = etree.XMLParser()
    root = etree.fromstring(cubes, parser)
    cost = {'red': 0, 'green': 0, 'blue': 0}
    cost[root.attrib['color']] += 1
    cost = count_cost(root, cost, 2)
    print(cost['red'], cost['green'], cost['blue'])


def count_cost(root, cost, price):
    for el in root.findall("cube"):
        cost[el.attrib['color']] += price
        cost = count_cost(el, cost, price + 1)
    return cost


if __name__ == '__main__':
    main()
