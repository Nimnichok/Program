#[easy] Розробити echo-сервер з використанням python socket API, який приймає з'єднання від клієнта
# та повертає клієнту отримані дані.

import socket


def echo_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Підключено до сервера {host}:{port}")

        while True:
            message = input("Введіть повідомлення (або 'exit' для виходу): ")
            if message.lower() == 'exit':
                print("Вихід із програми.")
                break

            client_socket.sendall(message.encode('utf-8'))
            data = client_socket.recv(1024)
            print(f"Отримано від сервера: {data.decode('utf-8')}")


if __name__ == "__main__":
    echo_client()
