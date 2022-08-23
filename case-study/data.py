import asyncio
import time
import random
import websockets
import json

paymentTypes = ["cash", "bitcoin"]
namesArray = ['Nilay', 'Nuriye', 'Neyzen', 'Nejdet']


async def show_time(websocket):
    while True:
        qty = random.randrange(1, 4)
        total = random.randrange(10, 500)

        payType = paymentTypes[random.randrange(0, 2)]
        name = namesArray[random.randrange(0, 4)]
        spent = random.randrange(1, 150)
        year = random.randrange(2016, 2022)
        # create a new data point
        point_data = {
            'quantity': qty,
            'total': total,

            'payType': payType,
            'Name': name,
            'Spent': spent,
            'Year': year,
            'x': time.time()
        }
        await websocket.send(json.dumps(point_data))
        await asyncio.sleep(random.random() * 2 + 1)


async def main():
    async with websockets.serve(show_time, "localhost", 5678):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())