import socket

def start_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print("Подключено к серверу.")

        while True:
            message = input("Введите сообщение: ")
            client_socket.send(message.encode())

            if message.lower() == "пока":
                break

            response = client_socket.recv(1024).decode()
            print("Ответ от сервера:", response)

        print("Соединение закрыто.")

if __name__ == '__main__':
    host = 'localhost'
    port = 12345
    start_client(host, port)

