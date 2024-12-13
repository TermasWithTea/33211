import multiprocessing
import time

def is_perfect_number(n):
    if n < 2:
        return None
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return n if divisors_sum == n else None

def find_perfect_numbers():
    with multiprocessing.Pool() as pool:
        results = pool.map(is_perfect_number, range(1, 10001))
    return [num for num in results if num is not None]

if __name__ == '__main__':
    start_time = time.time()
    perfect_numbers = find_perfect_numbers()
    elapsed_time = time.time() - start_time

    print("Совершенные числа (multiprocessing):", perfect_numbers)
    print(f"Время выполнения (multiprocessing): {elapsed_time:.2f} секунд")