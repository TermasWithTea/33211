import threading
import time


def is_perfect_number(n, result):
    if n < 2:
        return
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    if divisors_sum == n:
        result.append(n)


def find_perfect_numbers():
    threads = []
    result = []
    for num in range(1, 10001):
        thread = threading.Thread(target=is_perfect_number, args=(num, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result


start_time = time.time()
perfect_numbers = find_perfect_numbers()
elapsed_time = time.time() - start_time

print("Совершенные числа (threading):", perfect_numbers)
print(f"Время выполнения (threading): {elapsed_time:.2f} секунд")