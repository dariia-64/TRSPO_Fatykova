#CЕРВЕР
import socket

def main():
    port = 12345  # Порт, на якому працює сервер

    try:
        # Створення серверного сокета
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(("localhost", port))
            server_socket.listen(5)
            print(f"🚀 Сервер запущено на порту {port}. Очікування підключення...")

            while True:
                # Очікуємо підключення клієнта
                client_socket, client_address = server_socket.accept()
                print(f"🔗 Підключено клієнта: {client_address}")

                # Обробка повідомлень
                with client_socket:
                    message = client_socket.recv(1024).decode('utf-8')
                    print(f"📩 Отримано повідомлення від клієнта: {message}")

                    # Генерація відповіді
                    response = f"Привіт, клієнте з {client_address}! Я отримав твоє повідомлення: \"{message}\""
                    client_socket.sendall(response.encode('utf-8'))
                    print("📤 Відповідь надіслано клієнту.")
    except Exception as e:
        print(f"❌ Помилка сервера: {e}")

if __name__ == "__main__":
    main()
