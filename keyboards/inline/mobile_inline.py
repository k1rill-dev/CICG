# -*- coding: utf-8 -*-
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

tasks = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1️⃣Android Studio1️⃣", callback_data='true')
    ],
    [
        InlineKeyboardButton(text="2️⃣Visual Studio2️⃣", callback_data='false')
    ],
    [
        InlineKeyboardButton(text="3️⃣PyCharm3️⃣", callback_data='false')
    ],
    [
        InlineKeyboardButton(text="4️⃣Notepad ++4️⃣", callback_data='false')
    ]
])

tasks_sen = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1️⃣NotRunning1️⃣", callback_data='false_sen')
    ],
    [
        InlineKeyboardButton(text="2️⃣Running2️⃣", callback_data='false_sen')
    ],
    [
        InlineKeyboardButton(text="3️⃣Suspended3️⃣", callback_data='false_sen')
    ],
    [
        InlineKeyboardButton(text="4️⃣Terminated4️⃣", callback_data='false_sen')
    ],
    [
        InlineKeyboardButton(text="5️⃣ClosedByUser5️⃣", callback_data='false_sen')
    ],
    [
        InlineKeyboardButton(text="6️⃣Error6️⃣", callback_data='true_sen')
    ]
])