import asyncio
from handlers import dp
from utils.connect import bot



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

