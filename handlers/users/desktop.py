from aiogram import types
from keyboards.inline.des_inline import tasks, tasks_sen
from loader import dp, bot
from states.state import StateBot
from keyboards.inline.get_mail import get_mail
from aiogram.dispatcher import FSMContext
from mail.googlemail import mail
from handlers.users.quiz import cur, con

des_count = 0

@dp.message_handler(text="🚪Начать стажировку🚪",state=StateBot.In_choice_des)
async def bot_web(message: types.Message, state: FSMContext):
    await StateBot.In_task_des.set()
    await message.answer('Вас взяли на стажировку разработчиком десктопных приложений! И первой твоей задачей в первый рабочий день стало это - создать базовое WPF приложение. Какой тег(xaml) является базовым в любом приложении?', reply_markup=tasks)

@dp.callback_query_handler(text = ["true", "false"], state=StateBot.In_task_des)
async def bot_g(call: types.CallbackQuery, state: FSMContext):
    global des_count
    if call.data == "true":
        await call.message.answer("Во время работы над проектом, тебе надо получить данные из базы данных. Итак, вопрос, как правильно составить SQL-запрос из таблицы PRICES в столбец price, где цена должна быть равна 12000(СУБД - PostgreSQL)?")
        des_count+=1
        await StateBot.In_huaysk_des.set()
        await call.message.delete()
    elif call.data == "false":
        await call.message.answer("Во время работы над проектом, тебе надо получить данные из базы данных. Итак, вопрос, как правильно составить SQL-запрос из таблицы PRICES в столбец price, где цена должна быть равна 12000(СУБД - PostgreSQL)?")
        await StateBot.In_huaysk_des.set()
        await call.message.delete()

@dp.message_handler(state=StateBot.In_huaysk_des)
async def bot_game(message: types.Message, state: FSMContext):
    global des_count
    if message.text == "SELECT * FROM PRICES WHERE price = 12000" or message.text == "select * from PRICES where price = 12000":
        des_count+=1
        await message.answer("Ура, проект движется к финишу, осталось совсем чуть-чуть! Но тут еще одна проблема - в каком состоянии приложение НЕ может пребывать(UWP C#)?", reply_markup=tasks_sen)
        await StateBot.In_task_des.set()
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    else:
        await message.answer("Ура, проект движется к финишу, осталось совсем чуть-чуть! Но тут еще одна проблемка - в каком состоянии приложение НЕ может пребывать(UWP C#)?",reply_markup=tasks_sen)
        await StateBot.In_task_des.set()
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)


@dp.callback_query_handler(text=["true_sen", "false_sen"], state=StateBot.In_task_des)
async def bot_g(call: types.CallbackQuery, state: FSMContext):
    global des_count
    if call.data == "true_sen":
        des_count+=1
        await call.message.delete()
        if des_count ==3:
            counts = ["Десктоп разработчик", "Оффер", call.from_user.id]
            cur.execute("UPDATE PLAYERS SET PROFESSION = %s,FINISH = %s WHERE TG_ID = %s", counts)
            con.commit()
            await call.message.answer("Вы молодец и показали себя с хорошей стороны! Отправь заявку на https://talents.centrinvest.ru", reply_markup=get_mail)
            await StateBot.Set_mail_des.set()
        elif des_count <= 2:
            counts = ["Десктоп разработчик", "Не оффер", call.from_user.id]
            cur.execute("UPDATE PLAYERS SET PROFESSION = %s,FINISH = %s WHERE TG_ID = %s", counts)
            con.commit()
            msg = f"К сожалению, вы еще не готовы работать в крупной кампании в качестве тестировщика" + \
                  f"\nОбогатиться знаниями помогут следующие источники:" + \
                  f"\n\nhttps://stepik.org/course/82867?search=991966439" + \
                  f"\n\nhttps://stepik.org/course/58852?search=991965119" + \
                  f"\n\nhttps://stepik.org/course/99426?search=991965122"
            await call.message.answer(msg, reply_markup=get_mail)
            await StateBot.Set_mail_des.set()
    elif call.data == "false_sen":
        counts = ["Десктоп разработчик", "Не оффер", call.from_user.id]
        cur.execute("UPDATE PLAYERS SET PROFESSION = %s,FINISH = %s WHERE TG_ID = %s", counts)
        con.commit()
        msg = f"К сожалению, вы еще не готовы работать в крупной кампании в качестве тестировщика" + \
              f"\nОбогатиться знаниями помогут следующие источники:" + \
              f"\n\nhttps://stepik.org/course/82867?search=991966439" + \
              f"\n\nhttps://stepik.org/course/58852?search=991965119" + \
              f"\n\nhttps://stepik.org/course/99426?search=991965122"
        await call.message.answer(msg, reply_markup=get_mail)
        await StateBot.Set_mail_des.set()


@dp.callback_query_handler(text=['mail', 'stope_kuda_gonish'], state=StateBot.Set_mail_des)
async def bot_gm(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'mail':
        await call.message.answer("Напишите свою почту пожалуйста")
        await StateBot.Get_mail_des.set()
    if call.data == 'stope_kuda_gonish':
        await state.finish()
        await call.message.answer("Спасибо за игру!")

@dp.message_handler(state=StateBot.Get_mail_des)
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