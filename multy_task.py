import asyncio
import concurrent.futures
from multiprocessing import Pool, cpu_count

def cpu_bound_task(n):
    """Una funzione che simula un lavoro CPU-intensive."""
    result = sum(i * i for i in range(n))
    return result

async def async_worker(n, loop):
    """Un worker asincrono che delega il lavoro a un processo separato."""
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_bound_task, n)
        return result

async def main():
    """Funzione principale asincrona."""
    loop = asyncio.get_event_loop()
    tasks = [
        async_worker(10_000_000, loop),
        async_worker(20_000_000, loop),
        async_worker(30_000_000, loop),
    ]
    results = await asyncio.gather(*tasks)
    print("Risultati:", results)

if __name__ == "__main__":
    asyncio.run(main())
