import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv
from utils.queue import queue
from utils.mongo import init_mongo, is_admin
from sources.youtube import search_youtube

load_dotenv()
bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
dp = Dispatcher(bot)
init_mongo()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Welcome to the Music Bot! Use /play <song name> to get started.")

@dp.message_handler(commands=['play'])
async def play(message: types.Message):
    query = message.get_args()
    if not query:
        return await message.reply("Please provide a song name. Usage: /play <song>")
    song = search_youtube(query)
    if not song:
        return await message.reply("Song not found.")
    queue.add(song)
    button = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Open Player", url=f"{os.getenv('BASE_WEB_URL')}/play?id={song['id']}")
    )
    await message.reply(f"Added to queue: {song['title']}", reply_markup=button)

@dp.message_handler(commands=['queue'])
async def show_queue(message: types.Message):
    q = queue.get_all()
    if not q:
        return await message.reply("Queue is empty.")
    msg = "\n".join([f"{idx+1}. {s['title']}" for idx, s in enumerate(q)])
    await message.reply(f"Current Queue:\n{msg}")

@dp.message_handler(commands=['skip'])
async def skip_song(message: types.Message):
    skipped = queue.skip()
    if skipped:
        await message.reply(f"Skipped: {skipped['title']}")
    else:
        await message.reply("Queue is empty.")

@dp.message_handler(commands=['broadcast'])
async def broadcast(message: types.Message):
    if not await is_admin(message.from_user.id):
        return await message.reply("You are not authorized to broadcast.")
    from utils.broadcast import broadcast_message
    await broadcast_message(bot, message)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
