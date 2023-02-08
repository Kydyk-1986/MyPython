import logging
import pytube
from aiogram import Bot, Dispatcher, executor, types

api_token = '5807305400:AAGZOnmNFBPXU_PzkPyWkIntMPq5ZzbfKb0'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=api_token)
dp = Dispatcher(bot)

@dp.message_handler()
async def send_video(message: types.Message):
    print(message.text)
    if 'youtube.com' in message.text:
        video = pytube.YouTube(message.text)
        a = video.streams.get_highest_resolution()
        await message.answer(a.url)
        await message.answer('Видеону алдым')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)