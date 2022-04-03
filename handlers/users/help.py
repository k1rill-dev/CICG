from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = (f"Мы, команда BB, представляем игру – симулятор жизни, где, отвечая на вопросы мы определим твою IT специальность🖥\n\nПроект X дает доступ к следующим функциям🧐:\n\n<strong>✅ опредление вашей профессиональной ориентации в сфере IT</strong>\n<strong>✅ тестирование на знание подходящей вам профессии</strong>\n<strong>✅ отправление результата всего тестирования на электронную почту</strong>\n\nКлючевые команды:\n<strong>/start</strong> - начать работу с ботом\n<strong>/help</strong> - получить справку\n\nПосле команды <strong>'/start'</strong> следуйте инструкциям вложенным в сообщения бота👇")
    await message.answer(text)
