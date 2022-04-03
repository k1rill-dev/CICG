from aiogram import types
from keyboards.inline.get_mail import get_mail
from keyboards.inline.mobile_inline import tasks, tasks_sen
from loader import dp, bot
from states.state import StateBot
from aiogram.dispatcher import FSMContext
from handlers.users.quiz import cur, con
from mail.googlemail import mail

mob_count = 0

@dp.message_handler(text="🚪Начать стажировку🚪",state=StateBot.In_choice_mob)
async def bot_web(message: types.Message, state: FSMContext):
    await StateBot.In_task_mob.set()
    await message.answer('Вас взяли на стажировку разработчиком мобильных приложений! И первой твоей задачей в первый рабочий день стало это - создать базовое приложение. Как называется среда разработки(Android)?', reply_markup=tasks)

@dp.callback_query_handler(text = ["true", "false"], state=StateBot.In_task_mob)
async def bot_g(call: types.CallbackQuery, state: FSMContext):
    global mob_count
    if call.data == "true":
        await call.message.answer("Во время работы над проектом, вам надо получить данные из базы данных. Итак, вопрос, как правильно составить SQL-запрос из таблицы count в столбец counts, где кол-во должна быть равна 5(СУБД - PostgreSQL)?")
        mob_count+=1
        await StateBot.In_huaysk_mob.set()
        await call.message.delete()
    elif call.data == "false":
        await call.message.answer("Во время работы над проектом, вам надо получить данные из базы данных. Итак, вопрос, как правильно составить SQL-запрос из таблицы count в столбец counts, где кол-во должна быть равна 5(СУБД - PostgreSQL)?")
        await StateBot.In_huaysk_mob.set()
        await call.message.delete()

@dp.message_handler(state=StateBot.In_huaysk_mob)
async def bot_game(message: types.Message, state: FSMContext):
    global mob_count
    if message.text == "SELECT counts FROM count WHERE count = 5" or message.text == "select counts from count where count = 5":
        mob_count+=1
        await message.answer("Ура, проект движется к финишу, осталось совсем чуть-чуть! Но тут еще одна проблема - в каком состоянии приложение НЕ может пребывать?", reply_markup=tasks_sen)
        await StateBot.In_task_mob.set()
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    else:
        await message.answer("Ура, проект движется к финишу, осталось совсем чуть-чуть! Но тут еще одна проблемка - в каком состоянии приложение НЕ может пребывать?",reply_markup=tasks_sen)
        await StateBot.In_task_mob.set()
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)


@dp.callback_query_handler(text=["true_sen", "false_sen"], state=StateBot.In_task_mob)
async def bot_g(call: types.CallbackQuery, state: FSMContext):
    global mob_count
    if call.data == "true_sen":
        mob_count+=1
        await call.message.delete()
        if mob_count ==3:
            counts = ["Разработчик мобилок", "Оффер", call.from_user.id]
            cur.execute("UPDATE PLAYERS SET PROFESSION = %s,FINISH = %s WHERE TG_ID = %s", counts)
            con.commit()
            await call.message.answer("Вы показали себя неплохо. \n\nМы считаем, что вы готовы к полноценной работе. " + \
                                      "\n\nЧтобы отправить заявку, заполните анкету по ссылке: \n\nhttps://talents.centrinvest.ru", reply_markup=get_mail)
            await StateBot.Set_mail_mob.set()
        elif mob_count <= 2:
            counts = ["Разработчик мобилок", "Не оффер", call.from_user.id]
            cur.execute("UPDATE PLAYERS SET PROFESSION = %s,FINISH = %s WHERE TG_ID = %s", counts)
            con.commit()
            msg = f"К сожалению, вы еще не готовы работать в крупной кампании в качестве тестировщика" + \
                  f"\nОбогатиться знаниями помогут следующие источники:" + \
                  f"\n\nhttps://stepik.org/course/89217?search=991952084" + \
                  f"\n\nhttps://stepik.org/course/4792?search=991952082" + \
                  f"\n\nhttps://stepik.org/course/90684?search=991909308"
            await call.message.answer(msg)
            await StateBot.Set_mail_mob.set()
            await call.message.answer(msg,reply_markup=get_mail)
    elif call.data == "false_sen":
        counts = ["Разработчик мобилок", "Не оффер", call.from_user.id]
        cur.execute("UPDATE PLAYERS SET PROFESSION = %s,FINISH = %s WHERE TG_ID = %s", counts)
        con.commit()
        msg = f"К сожалению, вы еще не готовы работать в крупной кампании в качестве тестировщика" + \
              f"\nОбогатиться знаниями помогут следующие источники:" + \
              f"\n\nhttps://stepik.org/course/89217?search=991952084" + \
              f"\n\nhttps://stepik.org/course/4792?search=991952082" + \
              f"\n\nhttps://stepik.org/course/90684?search=991909308"
        await call.message.answer(msg, reply_markup=get_mail)
        await StateBot.Set_mail_adm.set()


@dp.callback_query_handler(text=['mail', 'stope_kuda_gonish'], state=StateBot.Set_mail_adm)
async def bot_gm(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'mail':
        await call.message.answer("Напишите свою почту пожалуйста")
        await StateBot.Get_mail_adm.set()
    if call.data == 'stope_kuda_gonish':
        await state.finish()
        await call.message.answer("Спасибо за игру!")

@dp.message_handler(state=StateBot.Get_mail_adm)
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
               f"\nКоличество очков программиста:{p}"+ \
               f"\nКоличество очков тестировщика:{t}" + \
               f"\nКоличество очков аналитика:{a}" + \
               f"\nКоличество очков администратора:{an}" + \
                f"\nИтоговая специальность: {prof}"+ \
                f"\n{fin}"
    try:
        mail(msg_mail, message.text)
        await message.answer("Сообщение успешно отправлено")
        await state.finish()
    except Exception:
        await message.answer("Неправильная почта!")