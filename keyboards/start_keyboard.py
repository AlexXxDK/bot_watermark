from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

builder = InlineKeyboardBuilder()

start = InlineKeyboardButton(text='''''', callback_data="start")

builder.row(start)



start_keyboard = builder.as_markup()
