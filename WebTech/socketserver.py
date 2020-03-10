import socket
import threading


def server(conn):
    data = conn.recv(1024)
    if data.decode() == 'close': return
    conn.send(data)
    conn.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', 2222))
    s.listen(10)
    while True:
        conn, addr = s.accept()
        th = threading.Thread(target=server, args=(conn,))
        th.start()