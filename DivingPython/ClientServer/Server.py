import asyncio
import re


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.err = 'error\n{}\n'
        self.ok = 'ok\n{}\n'

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def process_data(self, data):
        comm, *args = data.split(' ')
        print(f'Comand {comm} args {args}')
        try:
            if comm == 'put':
                return self._put(args[0], args[1], args[2])
            if comm == 'get':
                if len(args) > 1:
                    raise KeyError
                return self._get(args[0])
        except (IndexError, KeyError):
            pass
        return self.err.format('wrong command')

    def _put(self, key, value, timestamp):
        if not (re.match(r'\d+', value) and re.match(r'\d', timestamp)):
            return self.err.format('wrong values')
        if key not in metrics.keys():
            metrics[key] = []
        deletable = None
        for item in metrics[key]:
            if item[1] == timestamp:
                deletable = item
        if deletable:
            metrics[key].remove(deletable)
        metrics[key].append((value, timestamp))
        print(metrics)
        return self.ok.format('\n')

    def _get(self, key):
        try:
            answer_args = ''
            if key == '*':
                for key in metrics.keys():
                    for value in metrics[key]:
                        answer_args += f'{key} {value[0]} {value[1]}\n'
            else:
                for value in metrics[key]:
                    answer_args += f'{key} {value[0]} {value[1]}\n'
        except KeyError:
            pass
        return self.ok.format(answer_args)


metrics = {}
loop = asyncio.get_event_loop()
coro = loop.create_server(
    ClientServerProtocol,
    '127.0.0.1', 8888
)

server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()