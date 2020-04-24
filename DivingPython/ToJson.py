import functools
import json


def to_json(func):
    @functools.wraps(func)
    def warped(*args):
        return json.dumps(func(*args))
    return warped


@to_json
def get_data(a, f, v, d):
    return {
        'data': 42,
        a: 234
        }


if __name__ == '__main__':
    print({
        'data': 42
        })
    print(get_data('sdfg', '', '', ''))
    print(get_data.__name__)
