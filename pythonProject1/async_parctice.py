import asyncio

async def task(i):
    print("running task ", i)
    await asyncio.sleep(5)
    print("finished task ", i)
    return i


async def main():
    tasks = [task(i) for i in range(5)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())

