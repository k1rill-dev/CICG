# -*- coding: utf-8 -*-
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

tasks = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='1️⃣<center>1️⃣', callback_data='true')
    ],
    [
        InlineKeyboardButton(text='2️⃣center2️⃣', callback_data='false')
    ],
    [
        InlineKeyboardButton(text='3️⃣Не знаю3️⃣', callback_data='false')
    ]

])

tasks_sen = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='1️⃣Хешируем конфедициальные данные и передаем JSON с файлами1️⃣', callback_data='true_sen')
    ],
    [
        InlineKeyboardButton(text='2️⃣Передаем JSON с данными2️⃣', callback_data='false_sen')
    ],
    [
        InlineKeyboardButton(text='3️⃣Отправляем данные в Google Drive3️⃣', callback_data='false_sen')
    ],
    [
        InlineKeyboardButton(text='4️⃣Разработаю свой способ передачи данных4️⃣', callback_data='false_sen')
    ]
])