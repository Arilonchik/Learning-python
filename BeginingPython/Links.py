import requests
import re


def main():
    web = input().rstrip()
    text = requests.get(web).text
    tags = re.findall(r'<a.*href=["\']?(.*)?["\']', text)
    links = []
    print(tags)
    for el in tags:
        a = re.search(r'(\w*://)?([\w]?[\d\w\.\-]*)', el)
        if a is not None and re.match(r'\w', a.group(2)):
            links.append(a.group(2))
    links = list(set(links))
    links.sort()
    for ans in links:
        print(ans)


if __name__ == '__main__':
    main()