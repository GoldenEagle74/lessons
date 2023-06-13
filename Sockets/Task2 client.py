import socket

def start_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print("Подключено к серверу.")

        while True:
            filename = input("Введите название файла: ")

            if not filename:
                break

            try:
                with open(filename, 'r') as file:
                    file_content = file.read()
                    client_socket.sendall(file_content.encode())
            except FileNotFoundError:
                print(f"Файл '{filename}' не найден")
                continue

            response = client_socket.recv(4096).decode()
            print("Ответ от сервера:")
            print(response)

        print("Соединение закрыто.")

if __name__ == '__main__':
    host = 'localhost'
    port = 12345
    start_client(host, port)
