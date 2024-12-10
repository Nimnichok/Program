#[easy] Розробити echo-сервер з використанням python socket API, який приймає з'єднання від клієнта
# та повертає клієнту отримані дані.

import socket

from numpy.distutils.command.sdist import sdist


def echo_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Сервер запущено на {host}:{port}. Очікування підключень...")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Підключено клієнта: {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Отримано дані: {data.decode('utf-8')}")
                    conn.sendall(data)

if __name__ == "__main__":
    echo_server()

