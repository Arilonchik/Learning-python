import socket
import time


class Client:
    """The interface to work with Server on text protocol"""
    def __init__(self, ip, port, timeout=None):
        self.socket = socket.create_connection((ip, port), timeout=timeout)

    def put(self, server_name, value, timestamp=int(time.time())):
        """ Put data to server"""
        self.socket.sendall(f"put {server_name} {value} {timestamp}".encode('utf8'))
        response = self.socket.recv(1024)
        code, *ans = self._parse_msg(response)
        if code == 'error':
            raise ClientError(ans[0])

    def get(self, name):
        """Get data from server,
        name - server_name that need"""
        self.socket.sendall(f"get {name}".encode('utf8'))
        response = self.socket.recv(1024)
        code, ans = self._parse_msg(response)
        if code == 'error':
            raise ClientError(ans[0])
        return self._parse_dict(ans)

    @staticmethod
    def _parse_msg(bstr):
        """Parsing messages from server"""
        args = bstr.decode("utf8").split('\n')
        return args[0], args[1:]

    @staticmethod
    def _parse_dict(args):
        """Parsing dict answer of information gets from server"""
        ans = {}
        for arg in args:
            if arg:
                key, value, tim = arg.split(' ')
                if key not in ans.keys():
                    ans[key] = []
                ans[key].append((int(tim), float(value)))
            else:
                break
        return ans

    def close_client(self):
        """Closing connection"""
        self.socket.close()


class ClientError(BaseException):
    """All wrong data exception"""
    def __init__(self, text):
        self.txt = text


if __name__ == '__main__':
    client = Client("127.0.0.1", 8888, timeout=15)
    client.get('wrong command test')