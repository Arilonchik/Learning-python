import requests
import json
from operator import itemgetter

def main():
    client_id = '16848ccaf567a61ecdae'
    client_secret = 'f0ab9ac4e660afd0b1b7bc7c34e6cbf8'
    token_j = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                            data={
                                "client_id": client_id,
                                "client_secret": client_secret
                                })
    token = json.loads(token_j.text)['token']
    with open('f1.txt', 'r') as fh, open('answer.txt', 'w') as ans:
        headers = {"X-Xapp-Token": token}
        painters = {}
        for idp in fh:
            res = requests.get(f"https://api.artsy.net/api/artists/{idp.rstrip()}", headers=headers)
            paint = json.loads(res.text, encoding='utf-8')
            painters[paint['sortable_name']] = paint['birthday']
        painters = sorted(painters.items(), key=itemgetter(1, 0))
        for p in painters:
            print(p[0])


if __name__ == '__main__':
    main()
