# bot.py
import asyncio
from aiogram import Bot, Dispatcher
from handlers.basic import router
from handlers.callbacks import callback_router 
bot = Bot(token="7300183820:AAE0NReIPFWkz8dPi1fORG0i_Gl2PFIACEg")
dp = Dispatcher()
dp.include_router(router)
dp.include_router(callback_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())




