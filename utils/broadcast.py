from aiogram import Bot
from utils.mongo import get_all_users

async def broadcast_message(bot: Bot, message):
    users = await get_all_users()
    for user in users:
        try:
            await bot.copy_message(chat_id=user["user_id"], from_chat_id=message.chat.id, message_id=message.message_id)
        except Exception as e:
            print(f"Failed to send to {user['user_id']}: {e}")