from aiogram import types
from keyboards.inline.analitic_inline import tasks, tasks_sen
from loader import dp
from states.state import StateBot
from aiogram.dispatcher import FSMContext
from mail.googlemail import mail
from handlers.users.quiz import cur, con
from keyboards.inline.get_mail import get_mail

anal_count = 0

@dp.message_handler(text='🚪Начать🚪', state=StateBot.In_choice_an)
async def bot_an_st(message: types.Message, state: FSMContext):
    await message.answer('Настал ваш первый рабочий день в новой квалификации. Вам выпала задача выбрать все значения из таблицы Orders. Как это можно сделать?')
    await StateBot.In_huaysk_an.set()

@dp.message_handler(state=StateBot.In_huaysk_an)
async def bot_an(message: types.Message, state: FSMContext):
    global anal_count
    if message.text == "SELECT * FROM Orders":
        anal_count += 1
        await message.answer("Необходимо осуществить формализацию модели. А что такое собственно формализаиция?", reply_markup=tasks)
        await StateBot.In_task_an.set()
        await message.delete()
    else:
        await message.answer("Необходимо осуществить формализацию модели. А что такое собственно формализаиция?", reply_markup=tasks)
        await StateBot.In_task_an.set()
        await message.delete()

@dp.callback_query_handler(text = ["true", "false"], state=StateBot.In_task_an)
async def bot_ann(call: types.CallbackQuery, state: FSMContext):
    global anal_count
    if call.data == "true":
        await call.message.delete()
        anal_count += 1
        await StateBot.In_Result.set()
        await call.message.answer("Как в excel таблице отделить целую часть от дробной?", reply_markup=tasks_sen)
    elif call.data == "false":
        await StateBot.In_Result.set()
        await call.message.delete()
        await call.message.answer("Как в excel таблице отделить целую часть от дробной?", reply_markup=tasks_sen)


@dp.callback_query_handler(text=["true_sen", "false_sen"], state=StateBot.In_Result)
async def bot_an_last(call: types.CallbackQuery, state: FSMContext):
    global anal_count
    if call.data == "true_sen":
        anal_count += 1
        if anal_count >= 2:
            counts = ["Аналитик", "Оффер", call.from_user.id]
            cur.execute("UPDATE PLAYERS SET PROFESSION = %s,FINISH = %s WHERE TG_ID = %s", counts)
            con.commit()
            await call.message.answer("Вы показали себя неплохо. \n\nМы считаем, что вы готовы к полноценной работе. \n\nЧтобы отправить заявку, заполните анкету по ссылке: \n\nhttps://talents.centrinvest.ru", reply_markup=get_mail)
            await StateBot.Set_mail_an.set()
        elif anal_count <= 1:
            counts = ["Аналитик", "Не оффер", call.from_user.id]
            cur.execute("UPDATE PLAYERS SET PROFESSION = %s,FINISH = %s WHERE TG_ID = %s", counts)
            con.commit()
            msg = f"К сожалению, вы еще не готовы работать в крупной кампании в качестве тестировщика" + \
                  f"\nОбогатиться знаниями помогут следующие источники:" + \
                  f"\n\nhttps://stepik.org/course/96145?search=991959224" + \
                  f"\n\nhttps://stepik.org/course/102480?search=991959217" + \
                  f"\n\nhttps://stepik.org/course/129?search=991959212"
            await call.message.answer(msg, reply_markup=get_mail)
            await StateBot.Set_mail_an.set()
    elif call.data == "false_sen":
        counts = ["Аналитик", "Не оффер", call.from_user.id]
        cur.execute("UPDATE PLAYERS SET PROFESSION = %s,FINISH = %s WHERE TG_ID = %s", counts)
        con.commit()
        msg = f"К сожалению, вы еще не готовы работать в крупной кампании в качестве тестировщика" + \
              f"\nОбогатиться знаниями помогут следующие источники:" + \
              f"\n\nhttps://stepik.org/course/96145?search=991959224" + \
              f"\n\nhttps://stepik.org/course/102480?search=991959217"+ \
              f"\n\nhttps://stepik.org/course/129?search=991959212"
        await call.message.answer(msg, reply_markup=get_mail)
        await StateBot.Set_mail_an.set()

@dp.callback_query_handler(text=['mail', 'stope_kuda_gonish'], state=StateBot.Set_mail_an)
async def bot_gm(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'mail':
        await call.message.answer("Напишите свою почту пожалуйста")
        await StateBot.Get_mail_an.set()
    if call.data == 'stope_kuda_gonish':
        await state.finish()
        await call.message.answer("Спасибо за игру!")

@dp.message_handler(state=StateBot.Get_mail_an)
async def bot_sm(message: types.Message, state: FSMContext):
    id = [message.from_user.id]
    cur.execute("SELECT NAME, PROG_COUNT, TESTER_COUNT, ANALYSE_COUNT, ADMIN_COUNT FROM PLAYERS WHERE TG_ID = %s", id)
    raws = cur.fetchall()
    p = raws[0][1]
    t = raws[0][2]
    a = raws[0][3]
    an = raws[0][4]
    cur.execute("SELECT PROFESSION, FINISH FROM PLAYERS WHERE TG_ID = %s", id)
    raws_t = cur.fetchall()
    prof = raws_t[0][0]
    fin = raws_t[0][1]
    msg_mail = "Ваша статистика по результатам игры:" + \
               f"\nИмя::{raws[0][0]}" + \
               f"\nКоличество очков программиста:{p}" + \
               f"\nКоличество очков тестировщика:{t}" + \
               f"\nКоличество очков аналитика:{a}" + \
               f"\nКоличество очков администратора:{an}" + \
               f"\nИтоговая специальность: {prof}" + \
               f"\n{fin}"
    try:
        mail(msg_mail, message.text)
        await message.answer("Сообщение успешно отправлено")
        await state.finish()
    except Exception:
        await message.answer("Неправильная почта!")