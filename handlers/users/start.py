from aiogram.fsm.context import FSMContext
from utils.connect import dp
from aiogram.types import Message
from aiogram.filters import Command




@dp.message(Command(commands="start"))
async def start_command(message: Message, state: FSMContext):
    await message.answer(
        text=f'''Добро пожаловать!
С помощью этого бота вы можете скачать ТикТок видео без водяного знака.

Для начала загрузки просто отправьте ссылку на Тик Ток видео.''',
        parse_mode="HTML",
    )

