# -*- coding: utf-8 -*-
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

tasks = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='1️⃣Selenium1️⃣', callback_data='true')
    ],
    [
        InlineKeyboardButton(text='2️⃣Вручную2️⃣', callback_data='false')
    ],
    [
        InlineKeyboardButton(text='3️⃣Миллениум3️⃣', callback_data='false')
    ]

])

tasks_sen = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='1️⃣Контейнер1️⃣', callback_data='false_sen')
    ],
    [
        InlineKeyboardButton(text='2️⃣Docker2️⃣', callback_data='true_sen')
    ],
    [
        InlineKeyboardButton(text='3️⃣Только git push3️⃣', callback_data='false_sen')
    ]

])