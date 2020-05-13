import requests
from datetime import datetime


# Global vars of current date and access token of vk
curr_date = datetime.today()
token = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'


def calculate(uid):
    """ Count friends ages"""
    try:
        if uid is not int:
            user = requests.get(f'https://api.vk.com/method/users.get?v=5.71&access_token={token}&user_ids={uid}')
            uid = user.json()['response'][0]['id']
        users_friends_data = requests.get(f'https://api.vk.com/method/friends.get?v=5.71&access_token={token}&user_id={uid}&fields=bdate')
    except KeyError:
        return []
    friends = users_friends_data.json()['response']['items']
    ages = {}
    for friend in friends:
        try:
            b_day = friend['bdate']
            d, m, y = map(int, b_day.split('.'))
            b_date = datetime(y, m, d)
            age = curr_date.year - b_date.year - ((curr_date.month, curr_date.day) < (b_date.month, b_date.day))
            if age not in ages.keys():
                ages[age] = 0
            ages[age] += 1
        except (KeyError, ValueError):
            continue
    result = []
    for age, count in ages.items():
        result.append((age, count))
    result.sort(key=lambda x: x[1], reverse=1)
    return result


if __name__ == '__main__':
    res = calculate('iuogj')
    print(res)
