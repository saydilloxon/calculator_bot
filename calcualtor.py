# main.py
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.utils import executor

API_TOKEN = "7335713906:AAElrWtt5uAlm4eCBF0EymukSPgA0D5YK9w"  # <-- Bu yerga bot tokeningni yoz

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Tarixni oddiy faylda saqlaymiz
history = []


@dp.message_handler(commands=['start'])
async def start_cmd(message: Message):
    await message.reply("Salom! Men oddiy kalkulyator botman.\nMisol yozing: 12 + 5")


@dp.message_handler(commands=['history'])
async def show_history(message: Message):
    if history:
        await message.reply("\n".join(history[-10:]))
    else:
        await message.reply("Tarix hozircha bo‘sh.")


@dp.message_handler()
async def calculate(message: Message):
    try:
        result = eval(message.text)
        expression = f"{message.text} = {result}"
        history.append(expression)
        await message.reply(expression)
    except:
        await message.reply("Iltimos to‘g‘ri arifmetik ifoda kiriting. (masalan: 10 + 2)")


if __name__ == "__main__":
    executor.start_polling(dp)
    import asyncio
    async def on_startup(dp):
        await bot.delete_webhook(drop_pending_updates=True)
    executor.start_polling(dp, on_startup=on_startup)
