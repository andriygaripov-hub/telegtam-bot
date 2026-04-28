from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import os

# Токен і Chat ID беремо з Environment Variables
TOKEN = os.getenv("8774959139:AAGRqhkUALP0MQeWbwBPUhSWs6ZPmXq9bwk")
CHAT_ID = os.getenv("-1003967191246")

bot = Bot(token=TOKEN)
scheduler = AsyncIOScheduler()

# Повідомлення
async def freezer_alert():
    await bot.send_message(chat_id=CHAT_ID, text="❄️ Запуск спіральних фрізерів №1-7 о 05:00")

async def multivac_alert():
    await bot.send_message(chat_id=CHAT_ID, text="✅ Перевірка Multivac 245 (кулінарний цех)")

# Планування задач
scheduler.add_job(freezer_alert, 'cron', hour=5, minute=0)

# З 08:00 кожні 2 години до 02:00
for h in list(range(8, 24, 2)) + [0, 2]:
    scheduler.add_job(multivac_alert, 'cron', hour=h, minute=0)

async def main():
    scheduler.start()
    while True:
        await asyncio.sleep(1)

if name == "__main__":
    asyncio.run(main())