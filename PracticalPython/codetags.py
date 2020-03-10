from urllib import request
import re
from collections import Counter


def main():
    page = request.urlopen('https://stepik.org/media/attachments/lesson/209719/2.html').read().decode('utf-8')
    strs = re.findall(r'<code>(.*?)</code>', page)
    print(strs)
    c = Counter(strs)
    print(c)


if __name__ == '__main__':
    main()
