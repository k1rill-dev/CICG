from aiogram import types
from keyboards.inline.tester_inline import tasks, tasks_sen
from keyboards.inline.get_mail import get_mail
from loader import dp, bot
from states.state import StateBot
from aiogram.dispatcher import FSMContext
from handlers.users.quiz import cur, con
from mail.googlemail import mail

test_count = 0

@dp.message_handler(text='🚪Начать🚪',state=StateBot.In_choice_tester)
async def bot_test_st(message: types.Message, state: FSMContext):
    await StateBot.In_task_tester.set()
    await message.answer('Настал ваш первый рабочий день в новой квалификации. \n\nВы должны протестировать веб-сайт.\n\nКакой инструмент будете использовать?', reply_markup=tasks)

@dp.callback_query_handler(text = ["true", "false"], state=StateBot.In_task_tester)
async def bot_t(call: types.CallbackQuery, state: FSMContext):
    global test_count
    if call.data == "true":
        await call.message.delete()
        test_count += 1
        await StateBot.In_huaysk_tester.set()
        await call.message.answer("Ещё один рабочий день. \n\nТеперь у вас на очереди тестирование приложения. \n\nКак называются автотесты?")
    elif call.data == "false":
        await call.message.delete()
        await StateBot.In_huaysk_tester.set()
        await call.message.answer("Ещё один рабочий день. \n\nТеперь у вас на очереди тестирование приложения. \n\nКак называются автотесты?")

@dp.message_handler(state=StateBot.In_huaysk_tester)
async def bot_test(message: types.Message, state: FSMContext):
    global test_count
    if message.text == "юнит тесты":
        await message.delete()
        test_count += 1
        await message.answer("Вам осталось выбрать сервис для запуска легковесной оболочки. \n\nКакой из них существует на самом деле?", reply_markup=tasks_sen)
        await StateBot.In_Result_test.set()
    else:
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        await message.answer("Вам осталось выбрать сервис для запуска легковесной оболочки. \n\nКакой из них существует на самом деле?", reply_markup=tasks_sen)
        await StateBot.In_Result_test.set()

@dp.callback_query_handler(text=["true_sen", "false_sen"], state=StateBot.In_Result_test)
async def bot_test_last(call: types.CallbackQuery, state: FSMContext):
    global test_count
    if call.data == "true_sen":
        test_count += 1
        await call.message.delete()
        if test_count >= 0:
            await call.message.answer("Вы показали себя неплохо. \n\nМы считаем, что вы готовы к полноценной работе. " + \
                                      "\n\nЧтобы отправить заявку, заполните анкету по ссылке: \n\nhttps://talents.centrinvest.ru", reply_markup=get_mail)

            counts = ["Q&A Engineer", "Не оффер", call.from_user.id]
            cur.execute("UPDATE PLAYERS SET PROFESSION = %s,FINISH = %s WHERE TG_ID = %s", counts)
            con.commit()

            await StateBot.Set_mail_test.set()
        elif test_count <= -1:
            counts = ["Q&A Engineer", "Не оффер", call.from_user.id]
            cur.execute("UPDATE PLAYERS SET PROFESSION = %s,FINISH = %s WHERE TG_ID = %s", counts)
            con.commit()
            msg = f"К сожалению, вы еще не готовы работать в крупной кампании в качестве тестировщика" + \
                  f"\nОбогатиться знаниями помогут следующие источники:" + \
                  f"\n\nhttps://stepik.org/course/63054?search=991963276" + \
                  f"\n\nhttps://stepik.org/course/92103?search=991963275" + \
                  f"\n\nhttps://stepik.org/course/575?search=991956484"
            await StateBot.Set_mail_test.set()
            await call.message.answer(msg, reply_markup=get_mail)
    elif call.data == "false_sen":
        counts = ["Q&A Engineer", "Не оффер"]
        cur.execute("UPDATE PLAYERS SET PROFESSION = %s,FINISH = %s WHERE ID = ID", counts)
        con.commit()
        msg = f"К сожалению, вы еще не готовы работать в крупной кампании в качестве тестировщика" + \
              f"\nОбогатиться знаниями помогут следующие источники:" + \
              f"\n\nhttps://stepik.org/course/63054?search=991963276" + \
              f"\n\nhttps://stepik.org/course/92103?search=991963275" + \
              f"\n\nhttps://stepik.org/course/575?search=991956484"
        await call.message.answer(msg, reply_markup=get_mail)
        await StateBot.Set_mail_test.set()


@dp.callback_query_handler(text=['mail', 'stope_kuda_gonish'], state=StateBot.Set_mail_test)
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
