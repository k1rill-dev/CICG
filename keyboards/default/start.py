from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚪Начать🚪")
        ]

    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

start_staj_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚪Начать стажировку🚪")
        ]

    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
