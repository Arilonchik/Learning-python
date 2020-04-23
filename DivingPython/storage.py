import argparse
import sys
import os
import tempfile
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--value')
    parser.add_argument('-k', '--key')
    namespace = parser.parse_args(sys.argv[1:])
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    #storage_path = 'file.data'
    if os.path.exists(storage_path):
        with open(storage_path, 'r') as f:
            storage = json.load(f)
            if namespace.value is None:
                try:
                    print(', '.join(storage[namespace.key]))
                except KeyError:
                    print('Empty key')
                return
            else:
                if namespace.key in storage.keys():
                    storage[namespace.key].append(str(namespace.value))
                else:
                    storage[namespace.key] = [str(namespace.value)]
            f.close()
    else:
        storage = {namespace.key: [str(namespace.value)]}
    with open(storage_path, 'w') as f:
        json.dump(storage, f)


if __name__ == '__main__':
    main()
