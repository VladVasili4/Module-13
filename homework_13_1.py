import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        print(f'Силач {name} поднял шар № {i}.')
        await asyncio.sleep(100/power)
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    sil1 = asyncio.create_task(start_strongman('Pasha', 200))
    sil2 = asyncio.create_task(start_strongman('Denis', 250))
    sil3 = asyncio.create_task(start_strongman('Apollon', 300))
    await sil1
    await sil2
    await sil3

asyncio.run(start_tournament())