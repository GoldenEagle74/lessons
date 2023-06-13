"""
Реализовать чат,
который позволит обмениваться сообщениями только между клиентом и сервером.
Клиент должен получать сообщения сервера в том числе. Сигналом окончания связи служит слово "Пока".
"""
import socket

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print("Сервер запущен. Ожидание подключения клиента...")

        client_socket, client_address = server_socket.accept()
        print("Подключен клиент:", client_address)

        with client_socket:
            while True:
                message = client_socket.recv(1024).decode()
                print("Сообщение от клиента:", message)

                if message.lower() == "пока":
                    break

                response = input("Введите ответное сообщение: ")
                client_socket.send(response.encode())

        print("Соединение закрыто.")

if __name__ == '__main__':
    host = 'localhost'
    port = 12345
    start_server(host, port)

