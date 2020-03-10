from collections import Counter
import codecs
import requests
import re


def main():
    url = input().rstrip()
    text = ''
    file = requests.get(url)
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + file.text.rstrip()
    while not re.match(r'We.*', text):
        file = requests.get(url)
        url = 'https://stepic.org/media/attachments/course67/3.6.3/' + file.text.rstrip()
        text = url
        print(url)
    print(file.text)


if __name__ == '__main__':
    main()
