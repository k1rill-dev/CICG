# -*- coding: utf-8 -*-
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

tasks = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1️⃣<Window></Window>1️⃣", callback_data='true')
    ],
    [
        InlineKeyboardButton(text="2️⃣Window2️⃣", callback_data='false')
    ],
    [
        InlineKeyboardButton(text="3️⃣Main3️⃣", callback_data='false')
    ],
    [
        InlineKeyboardButton(text="4️⃣Head4️⃣", callback_data='false')
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