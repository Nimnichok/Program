#Модифікувати TCP-сервер з п.1, щоб він працював постійно та обробляв запити від багатьох клієнтів послідовно.
#Для тестування сервера. запустити декілька разів клієнт з пункту 1-а

# Модифікований TCP-сервер
import socket
import threading

def handle_client(conn, addr):
    print(f"Підключено клієнта: {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Отримано дані від {addr}: {data.decode('utf-8')}")
            conn.sendall(data)
    print(f"Клієнт відключився: {addr}")

def echo_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Сервер запущено на {host}:{port}. Очікування підключень...")

        while True:
            conn, addr = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    echo_server()
