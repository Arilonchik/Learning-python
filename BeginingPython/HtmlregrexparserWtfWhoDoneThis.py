import requests
import re


def main():
    a = input()
    b = input()
    print(check_pars(a, b))


def check_pars(a, b):
    first_url = requests.get(a)
    if first_url.status_code != 200:
        return 'No'
    urls = re.findall(r'<a href=[\'"](.*.html)[\'"]', first_url.text)
    for link in urls:
        c_doc = requests.get(link)
        if c_doc.status_code != 200:
            continue
        match_urls = re.findall(r'<a href=[\'"](.*.html)[\'"]', c_doc.text)
        if b in match_urls:
            return "Yes"
    return 'No'


if __name__ == '__main__':
    main()
