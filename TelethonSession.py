
import asyncio
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

API_ID = 2184829
API_HASH = "6930b92388baabff4cb4a1d377085035"

async def main():
    bot = TelegramClient(StringSession(), API_ID, API_HASH)
    await bot.start()
    ss = bot.session.save()
    await bot.send_message("me", f"`{ss}`")
    print(ss)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())