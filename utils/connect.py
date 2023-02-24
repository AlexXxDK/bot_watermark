from aiogram import Bot, Dispatcher
from .functions import parse_config


main_config = parse_config('main')

bot = Bot(main_config['token'])
dp = Dispatcher()
