import requests
import json


def main():
    with open('f1.txt', 'r') as fh, open('answer.txt', 'w') as ans:
        for number in fh:

            url = "http://numbersapi.com/" + number.rstrip() + '/math'
            params = {
                'json': 'true',
            }
            js_data = requests.get(url, params=params).text
            if json.loads(js_data)["found"]:
                ans.write('Interesting\n')
            else:
                ans.write('Boring\n')


if __name__ == '__main__':
    main()
