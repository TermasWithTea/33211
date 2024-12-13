import asyncio
import time


async def is_perfect_number(n):
    if n < 2:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n


async def find_perfect_numbers():
    perfect_numbers = []
    tasks = [is_perfect_number(num) for num in range(1, 10001)]
    results = await asyncio.gather(*tasks)

    for num, result in zip(range(1, 10001), results):
        if result:
            perfect_numbers.append(num)

    return perfect_numbers


start_time = time.time()
perfect_numbers = asyncio.run(find_perfect_numbers())
elapsed_time = time.time() - start_time

print("Совершенные числа (asyncio):", perfect_numbers)
print(f"Время выполнения (asyncio): {elapsed_time:.2f} секунд")
