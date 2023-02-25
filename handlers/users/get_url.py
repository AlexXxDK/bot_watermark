from utils.connect import dp
from aiogram.types import Message
import requests
from json import loads
from aiogram.utils.markdown import hide_link

@dp.message()
async def get_url(message: Message):
    try:
        url = f"https://api.douyin.wtf/api?url={message}?is_from_webapp=1&sender_device=pc"

        r = requests.get(url=url)
        final_user_url = loads(r.text)['video_data']["nwm_video_url_HQ"]
        final_user_sound = loads(r.text)['music']['play_url']['uri']

        await message.answer(text=f'''Твое видео {final_user_url}, 
        твой звук{final_user_sound}''')

    except:
        await message.answer(text="SOmthing wrong")

