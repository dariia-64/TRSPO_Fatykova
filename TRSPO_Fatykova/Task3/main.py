import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Функція для обчислення кількості кроків до виродження числа в 1
def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

# Глобальні змінні для підрахунку кількості кроків і оброблених чисел
lock = threading.Lock()
total_steps = 0
processed_numbers = 0

# Функція для обробки чисел з діапазону
def process_range(start, end):
    global total_steps, processed_numbers
    local_steps = 0
    local_count = 0

    for number in range(start, end):
        local_steps += collatz_steps(number)
        local_count += 1

    # Атомарне оновлення глобальних змінних
    with lock:
        total_steps += local_steps
        processed_numbers += local_count

# Основна функція
def main():
    global total_steps, processed_numbers

    start_time = time.time()

    # Кількість потоків (можна змінити)
    num_threads = 8

    # Діапазон чисел
    start_number = 1
    end_number = 10_000_001

    # Розбиття діапазону на частини для потоків
    step = (end_number - start_number) // num_threads

    # Використання ThreadPoolExecutor для запуску потоків
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(process_range, start_number + i * step, start_number + (i + 1) * step)
                   for i in range(num_threads)]

        # Очікування завершення всіх потоків
        for future in futures:
            future.result()

    # Підрахунок середньої кількості кроків
    average_steps = total_steps / processed_numbers

    end_time = time.time()

    print(f"Середня кількість кроків: {average_steps}")
    print(f"Час виконання: {end_time - start_time:.2f} секунд")

if __name__ == "__main__":
    main()
