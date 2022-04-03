# -*- coding: utf-8 -*-

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

question1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1️⃣Бросить песок в глаза и дать отпор1️⃣", callback_data='answer1')
    ],
    [
        InlineKeyboardButton(text="2️⃣Попытаться уладить конфликт. Завести дружбу2️⃣", callback_data='answer2')
    ],
    [
        InlineKeyboardButton(text="3️⃣Решить, что эта песочница не для меня.Найти другую3️⃣", callback_data='answer3')
    ],
    [
        InlineKeyboardButton(text="4️⃣Честно отстоять свою песочницу4️⃣", callback_data='answer4')
    ]
],resize_keyboard = True)

question2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1️⃣Сделать всё, чтобы получить оценку1️⃣", callback_data='answer1.1')
    ],
    [
        InlineKeyboardButton(text="2️⃣Не напрягаться. Не имееется нужды2️⃣", callback_data='answer2.1')
    ],
    [
        InlineKeyboardButton(text="3️⃣Стать паразитом в чужой сценке3️⃣", callback_data='answer3.1')
    ],
    [
        InlineKeyboardButton(text="4️⃣Собрать свою актерскую команду4️⃣", callback_data='answer4.1')
    ]
])

question3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1️⃣Одолжить у кого-нибудь шпаргалки1️⃣", callback_data='answer1.2')
    ],
    [
        InlineKeyboardButton(text="2️⃣Организовать командную работу на экзамене2️⃣", callback_data='answer2.2')
    ],
    [
        InlineKeyboardButton(text="3️⃣Подготовиться самостоятельно3️⃣", callback_data='answer3.2')
    ],
    [
        InlineKeyboardButton(text="4️⃣Найти готовые шпаргалки4️⃣", callback_data='answer4.2')
    ]
])

question4 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1️⃣Взять то, что останется1️⃣", callback_data='answer1.3')
    ],
    [
        InlineKeyboardButton(text="2️⃣Отказаться. Учеба превышего всего2️⃣", callback_data='answer2.3')
    ],
    [
        InlineKeyboardButton(text="3️⃣Быть только капитаном3️⃣", callback_data='answer3.3')
    ],
    [
        InlineKeyboardButton(text="4️⃣Занять творческую позицию4️⃣", callback_data='answer4.3')
    ]
])

question5 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1️⃣Готовиться, но перестраховаться подарком1️⃣", callback_data='answer1.4')
    ],
    [
        InlineKeyboardButton(text="2️⃣Учердно подготовиться2️⃣", callback_data='answer2.4')
    ],
    [
        InlineKeyboardButton(text="3️⃣Воспользоваться своими знаниями3️⃣", callback_data='answer3.4')
    ],
    [
        InlineKeyboardButton(text="4️⃣Провести диалог с преподавателем4️⃣", callback_data='answer4.4')
    ]
])

question6 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1️⃣Не готовиться. Я - мое резюме.1️⃣", callback_data='answer1.5')
    ],
    [
        InlineKeyboardButton(text="2️⃣Сымпровизировать и сделать ставку на харизму2️⃣", callback_data='answer2.5')
    ],
    [
        InlineKeyboardButton(text="3️⃣Подготовиться: купить новый костюм3️⃣", callback_data='answer3.5')
    ],
    [
        InlineKeyboardButton(text="4️⃣Изучить все о кампании, чтобы не облажать4️⃣", callback_data='answer4.5')
    ]
])

question7 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1️⃣Уйти во фриланс, чтобы не прогибаться1️⃣", callback_data='answer1.6')
    ],
    [
        InlineKeyboardButton(text="2️⃣Сделать все, чтобы меня честно повысили2️⃣", callback_data='answer2.6')
    ],
    [
        InlineKeyboardButton(text="3️⃣Не спорить с начальником3️⃣", callback_data='answer3.6')
    ],
    [
        InlineKeyboardButton(text="4️⃣Попытаться выбить повышение легально4️⃣", callback_data='answer4.6')
    ]
])
dop = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1️⃣Веб-разработка1️⃣", callback_data='web')
    ],
    [
        InlineKeyboardButton(text="2️⃣Десктоп2️⃣", callback_data='desktop')
    ],
    [
        InlineKeyboardButton(text="3️⃣Мобильная разработка3️⃣", callback_data='mobile')
    ]
])