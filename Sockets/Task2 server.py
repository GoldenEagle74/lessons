"""
Разработайте приложение, которое будет запрашивать у пользователя название файла,
а затем отправлять содержимое этого файла серверу. Сервер будет выводить сообщение, подсчитывать количество слов и возвращать ответ.
Протестируйте на test.txt
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
                data = client_socket.recv(4096).decode()
                if not data:
                    break

                file_content = ""
                while True:
                    file_content += data
                    if len(data) < 4096:
                        break
                    data = client_socket.recv(4096).decode()

                word_count = len(file_content.split())
                response = f"Получено содержимое файла:\n{file_content}\nКоличество слов: {word_count}"
                client_socket.send(response.encode())

        print("Соединение закрыто.")

if __name__ == '__main__':
    host = 'localhost'
    port = 12345
    start_server(host, port)

