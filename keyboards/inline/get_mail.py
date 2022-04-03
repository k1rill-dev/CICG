# -*- coding: utf-8 -*-
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

get_mail = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Получить статистику на почту", callback_data='mail')
    ],
[
        InlineKeyboardButton(text="Завершить игру", callback_data='stope_kuda_gonish')
    ]
])