import socket

def tcp_server():
    host = '127.0.0.1'  # Локальний хост
    port = 12345         # Порт для зв'язку

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Очікуємо 1 клієнта

    print(f"Сервер запущено на {host}:{port}. Очікуємо підключення...")

    conn, addr = server_socket.accept()
    print(f"Клієнт підключився: {addr}")

    while True:
        # Отримання повідомлення від клієнта
        data = conn.recv(1024).decode('utf-8')
        if not data or data.lower() == 'exit':
            print("Клієнт завершив з'єднання.")
            break
        print(f"Клієнт: {data}")

        # Надсилання відповіді
        server_message = input("Сервер: ")
        conn.send(server_message.encode('utf-8'))
        if server_message.lower() == 'exit':
            print("Сервер завершує з'єднання.")
            break

    conn.close()
    server_socket.close()

def tcp_client():
    host = '127.0.0.1'  # Локальний хост
    port = 12345         # Порт для зв'язку

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(f"Підключено до сервера {host}:{port}")

    while True:
        # Надсилання повідомлення серверу
        client_message = input("Клієнт: ")
        client_socket.send(client_message.encode('utf-8'))
        if client_message.lower() == 'exit':
            print("Клієнт завершує з'єднання.")
            break

        # Отримання відповіді від сервера
        data = client_socket.recv(1024).decode('utf-8')
        if not data or data.lower() == 'exit':
            print("Сервер завершив з'єднання.")
            break
        print(f"Сервер: {data}")

    client_socket.close()

if __name__ == "__main__":
    print("Оберіть режим роботи:")
    print("1. Сервер")
    print("2. Клієнт")
    choice = input("Введіть 1 або 2: ")

    if choice == '1':
        tcp_server()
    elif choice == '2':
        tcp_client()
    else:
        print("Неправильний вибір. Перезапустіть програму.")

