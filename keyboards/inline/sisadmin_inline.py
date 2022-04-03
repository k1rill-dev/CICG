# -*- coding: utf-8 -*-

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

tasks = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1️⃣172.30.16.01️⃣", callback_data='false')
    ],
    [
        InlineKeyboardButton(text="2️⃣172.30.32.02️⃣", callback_data='false')
    ],
    [
        InlineKeyboardButton(text="3️⃣172.30.0.03️⃣", callback_data='false')
    ],
    [
        InlineKeyboardButton(text="4️⃣172.30.48.04️⃣", callback_data='true')
    ]
])

tasks_sen = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1️⃣IMAP1️⃣", callback_data='false_sen')
    ],
    [
        InlineKeyboardButton(text="2️⃣SMTP2️⃣", callback_data='false_sen')
    ],
    [
        InlineKeyboardButton(text="3️⃣POP33️⃣", callback_data='true_sen')
    ],
    [
        InlineKeyboardButton(text="4️⃣MAC4️⃣", callback_data='false_sen')
    ]
])