import requests


def main():
    web = requests.get('https://stepik.org/media/attachments/lesson/209717/1.html')
    py = web.text.count('Python')
    c = web.text.count("C++")
    print(py, c)


if __name__ == '__main__':
    main()
