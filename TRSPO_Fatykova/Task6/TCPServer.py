import socket
import struct

def main():
    port = 8080

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(("localhost", port))
            server_socket.listen(1)
            print(f"🚀 Сервер запущено на порту {port}. Очікування підключення...")

            client_socket, client_address = server_socket.accept()
            print(f"🔗 Підключено клієнта: {client_address}")

            with client_socket:
                for i in range(100):
                    # Прийом довжини повідомлення
                    message_length = struct.unpack('!I', client_socket.recv(4))[0]

                    # Прийом самого повідомлення
                    message_bytes = client_socket.recv(message_length)
                    message = message_bytes.decode('utf-8')
                    print(f"📩 Отримано від клієнта: {message}")

                    # Формування відповіді
                    response = f"Message {i + 1} received"
                    response_bytes = response.encode('utf-8')

                    # Відправлення довжини і самого повідомлення
                    client_socket.sendall(struct.pack('!I', len(response_bytes)))  # Довжина відповіді
                    client_socket.sendall(response_bytes)  # Саме повідомлення
                    print(f"📤 Надіслано відповідь клієнту: {response}")

            print("✅ Сервер завершив комунікацію.")

    except Exception as e:
        print(f"❌ Помилка сервера: {e}")

if __name__ == "__main__":
    main()
