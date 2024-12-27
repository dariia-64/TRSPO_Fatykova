import concurrent.futures
import queue
import time

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


# Функція для обробки черги чисел і підрахунку кроків
def process_queue(number_queue, result_queue):
    while not number_queue.empty():
        number = number_queue.get()
        steps = collatz_steps(number)
        result_queue.put(steps)


# Основна функція
def main():
    start_time = time.time()

    # Кількість потоків (можна змінити)
    num_threads = 8

    # Створення черг
    number_queue = queue.Queue()
    result_queue = queue.Queue()

    # Заповнення черги числами від 1 до 10 000 000
    for i in range(1, 10000001):
        number_queue.put(i)

    # Створення пулу потоків для обчислень
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Створення і запуск потоків
        futures = [executor.submit(process_queue, number_queue, result_queue) for _ in range(num_threads)]

        # Очікування завершення всіх потоків
        concurrent.futures.wait(futures)

    # Підрахунок середньої кількості кроків
    total_steps = 0
    num_results = result_queue.qsize()

    while not result_queue.empty():
        total_steps += result_queue.get()

    average_steps = total_steps / num_results

    end_time = time.time()

    print(f"Середня кількість кроків: {average_steps}")
    print(f"Час виконання: {end_time - start_time:.2f} секунд")


if __name__ == "__main__":
    main()