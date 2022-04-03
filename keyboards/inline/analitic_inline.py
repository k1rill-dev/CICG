# -*- coding: utf-8 -*-

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

tasks = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1️⃣Представить в виде формальной системы или исчисления1️⃣", callback_data='true')
    ],
    [
        InlineKeyboardButton(text="2️⃣Не знаю...2️⃣", callback_data='false')
    ],
    [
        InlineKeyboardButton(text="3️⃣Представить в необходимом виде3️⃣", callback_data='false')
    ],
    [
        InlineKeyboardButton(text="4️⃣Что такое формализация?4️⃣", callback_data='false')
    ]
])

tasks_sen = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1️⃣:1️⃣", callback_data='false_sen')
    ],
    [
        InlineKeyboardButton(text="2️⃣ ; 2️⃣", callback_data='false_sen')
    ],
    [
        InlineKeyboardButton(text="3️⃣ . 3️⃣", callback_data='false_sen')
    ],
    [
        InlineKeyboardButton(text="4️⃣нет правильного ответа4️⃣", callback_data='true_sen')
    ]
])