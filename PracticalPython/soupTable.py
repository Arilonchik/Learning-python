from bs4 import BeautifulSoup
import requests


def main():
    response = requests.get('https://stepik.org/media/attachments/lesson/209723/5.html')
    soup = BeautifulSoup(response.text, 'lxml')
    table = soup.table
    table_rows = table.find_all('tr')
    sum = 0
    for tr in table_rows:
        td = tr.find_all('td')
        for i in td:
            sum += int(i.text)
        print(sum)


if __name__ == '__main__':
    main()
