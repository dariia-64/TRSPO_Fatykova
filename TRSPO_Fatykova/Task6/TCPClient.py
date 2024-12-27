import socket
import struct

def main():
    hostname = "localhost"
    port = 8080

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((hostname, port))
            print("✅ Підключено до сервера.")

            for i in range(100):
                # Формування повідомлення
                message = f"Hello Server, message #{i + 1}"
                message_bytes = message.encode('utf-8')

                # Відправлення довжини і самого повідомлення
                client_socket.sendall(struct.pack('!I', len(message_bytes)))  # Довжина повідомлення
                client_socket.sendall(message_bytes)  # Саме повідомлення
                print(f"📤 Надіслано: {message}")

                # Прийом відповіді
                response_length = struct.unpack('!I', client_socket.recv(4))[0]  # Довжина відповіді
                response_bytes = client_socket.recv(response_length)  # Отримання повідомлення
                response = response_bytes.decode('utf-8')
                print(f"📥 Отримано від сервера: {response}")

            print("✅ Клієнт завершив комунікацію.")

    except Exception as e:
        print(f"❌ Помилка клієнта: {e}")

if __name__ == "__main__":
    main()
