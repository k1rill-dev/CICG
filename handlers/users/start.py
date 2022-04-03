from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start import start_button
from loader import dp
from states.state import StateBot

@dp.message_handler(CommandStart(),state=None)
async def bot_start(message: types.Message):
    await message.answer(f'Привет 👋 {message.from_user.full_name}!\n\nВы попали на проект CICG от команды BB, который в игровой форме поможет вам:\n\n- определиться с вашей проф.ориентацией\n- протестировать вас на предпочитаемую профессию\n- выслать развернутый результат всего тестирования на электронную почту \n\nНажмите "🚪Начать🚪", чтобы приступить к игре 🎮',reply_markup=start_button)
    await StateBot.In_Question.set()


