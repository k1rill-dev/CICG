from aiogram import types
from keyboards.default.start import start_button, start_staj_button
from loader import dp
from states.state import StateBot
from keyboards.inline.question import *
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InputFile
import matplotlib.pyplot as plt
import psycopg2
from data.config import *

con = psycopg2.connect(
        database="d2hrrbu1311r1b",
        user="gahdttwnarszcm",
        password="f45246e187465ddb5c8e20b62092434faf8d59cbd6404e71d36a536a983a8af1",
        host="ec2-18-214-134-226.compute-1.amazonaws.com",
        port=5432
    )

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS PLAYERS
     (ID SERIAL PRIMARY KEY,
     TG_ID BIGINT NOT NULL UNIQUE,
     NAME VARCHAR (100) NULL,
     PROG_COUNT BIGINT DEFAULT 0,
     TESTER_COUNT BIGINT DEFAULT 0,
     ANALYSE_COUNT BIGINT DEFAULT 0,
     ADMIN_COUNT BIGINT DEFAULT 0,
     PROFESSION VARCHAR (100),
     FINISH VARCHAR (100));''')

con.commit()

@dp.message_handler(text='🚪Начать🚪', state=StateBot.In_Question)
async def bot_quiz(message: types.Message):
    id = [message.from_user.id]
    cur.execute("SELECT * FROM PLAYERS WHERE TG_ID = %s", id)
    flag = cur.fetchall()
    if len(flag) > 0:
        print("есть совпадение")
    else:
        data = [message.from_user.id, message.from_user.full_name]
        cur.execute(
            "INSERT INTO PLAYERS (TG_ID, NAME) VALUES(%s, %s)",
            data)
        con.commit()
        print("Успешно занесено в базу")

    with open('robotic.png', 'rb') as photobot:
        phbot = photobot.read()
        await message.answer_photo(photo=phbot,
                                   caption=f"Вы родились с именем {message.from_user.full_name} 🎂 . В детстве вы были обычным скромным ребенком, который не любил драться и часто плакал по пустякам.🚼 \n\nВ один из обычных солнечных дней, вы замечаете местных хулиганов, которые направляются прямо к песочнице, у которой вы здорово проводите время.😱 \n\nЧто вы предпримите?\n\n ВАЖНО: Каждый ваш выбор влияет на итог сюжета")
    with open('photo.png', 'rb') as photo:
        ph = photo.read()
        await message.answer_photo(photo=ph,reply_markup=question1)


    cur.execute("UPDATE PLAYERS SET PROG_COUNT=0, TESTER_COUNT=0, ANALYSE_COUNT=0, ADMIN_COUNT=0, PROFESSION=null, FINISH=null WHERE TG_ID=%s", id)
    con.commit()
    print("succesful")

@dp.callback_query_handler(text = ["answer1", "answer2","answer3","answer4"], state=StateBot.In_Question)
async def bot_quiz(call: CallbackQuery, state: FSMContext):
    id = [call.from_user.id]
    if call.data == 'answer1':
        cur.execute("UPDATE PLAYERS SET PROG_COUNT = PROG_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer2':
        cur.execute("UPDATE PLAYERS SET TESTER_COUNT = TESTER_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer3':
        cur.execute("UPDATE PLAYERS SET ANALYSE_COUNT = ANALYSE_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer4':
        cur.execute("UPDATE PLAYERS SET ADMIN_COUNT = ADMIN_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    with open('robotic.png', 'rb') as photobot:
        phbot = photobot.read()
        await call.message.answer_photo(photo=phbot,
                                   caption="Каким бы детство не было беззабоным и радостным - оно закончилось, и вы пошли в школу🏫\n\nУспешно обучаясь 7 классов, произошел интересный случай. На биологии появилась возможность получить оценку, если сделать сценку про какой-нибудь материал из четверти (цитогенез, пестики-тычинки, беспозвоночные).🎬 \n\nКак поступите?")
    with open('photo2.jpg', 'rb') as photo2:
        ph2 = photo2.read()
        await call.message.answer_photo(photo=ph2,reply_markup=question2)

    await call.message.delete()


@dp.callback_query_handler(text = ["answer1.1", "answer2.1","answer3.1","answer4.1"], state=StateBot.In_Question)
async def bot_quiz(call: CallbackQuery, state: FSMContext):
    id = [call.from_user.id]
    if call.data == 'answer1.1':
        cur.execute("UPDATE PLAYERS SET PROG_COUNT = PROG_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer2.1':
        cur.execute("UPDATE PLAYERS SET TESTER_COUNT = TESTER_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer3.1':
        cur.execute("UPDATE PLAYERS SET ANALYSE_COUNT = ANALYSE_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer4.1':
        cur.execute("UPDATE PLAYERS SET ADMIN_COUNT = ADMIN_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    with open('robotic.png', 'rb') as photobot:
        phbot = photobot.read()
        await call.message.answer_photo(photo=phbot,
                                   caption="И вот уже 9 класс, а значит что и ОГЭ не за горами. \n\nКак готовиться будете?")
    with open('photo3.jpg', 'rb') as photo3:
        ph3 = photo3.read()
        await call.message.answer_photo(photo=ph3,reply_markup=question3)

    await call.message.delete()


@dp.callback_query_handler(text = ["answer1.2", "answer2.2","answer3.2","answer4.2"], state=StateBot.In_Question)
async def bot_quiz(call: CallbackQuery, state: FSMContext):
    id = [call.from_user.id]
    if call.data == 'answer1.2':
        cur.execute("UPDATE PLAYERS SET PROG_COUNT = PROG_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer2.2':
        cur.execute("UPDATE PLAYERS SET TESTER_COUNT = TESTER_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer3.2':
        cur.execute("UPDATE PLAYERS SET ANALYSE_COUNT = ANALYSE_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer4.2':
        cur.execute("UPDATE PLAYERS SET ADMIN_COUNT = ADMIN_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    with open('robotic.png', 'rb') as photobot:
        phbot = photobot.read()
        await call.message.answer_photo(photo=phbot,
                                   caption="Вы молодец, успешно сдали государственный экзамен и закончили школу с всего одной четверкой по русскому языку🎓 Вы поступили в колледж и там вас пригласили играть в КВН. Какую роль возьмете🤹?")
    with open('photox.png', 'rb') as photox:
        phx = photox.read()
        await call.message.answer_photo(photo=phx,reply_markup=question4)

    await call.message.delete()


@dp.callback_query_handler(text = ["answer1.3", "answer2.3","answer3.3","answer4.3"], state=StateBot.In_Question)
async def bot_quiz(call: CallbackQuery, state: FSMContext):
    id = [call.from_user.id]
    if call.data == 'answer1.3':
        cur.execute("UPDATE PLAYERS SET PROG_COUNT = PROG_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer2.3':
        cur.execute("UPDATE PLAYERS SET TESTER_COUNT = TESTER_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer3.3':
        cur.execute("UPDATE PLAYERS SET ANALYSE_COUNT = ANALYSE_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer4.3':
        cur.execute("UPDATE PLAYERS SET ADMIN_COUNT = ADMIN_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    with open('robotic.png', 'rb') as photobot:
        phbot = photobot.read()
        await call.message.answer_photo(photo=phbot,
                                        caption="К сожалению, вы завалили один экзамен в колледже📉. Что будете делать🤔?")
    with open('photo4.jpg', 'rb') as photo4:
        ph4 = photo4.read()
        await call.message.answer_photo(photo=ph4, reply_markup=question5)

    await call.message.delete()

@dp.callback_query_handler(text = ["answer1.4", "answer2.4","answer3.4","answer4.4"], state=StateBot.In_Question)
async def bot_quiz(call: CallbackQuery, state: FSMContext):
    id = [call.from_user.id]
    if call.data == 'answer1.4':
        cur.execute("UPDATE PLAYERS SET PROG_COUNT = PROG_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer2.4':
        cur.execute("UPDATE PLAYERS SET TESTER_COUNT = TESTER_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer3.4':
        cur.execute("UPDATE PLAYERS SET ANALYSE_COUNT = ANALYSE_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer4.4':
        cur.execute("UPDATE PLAYERS SET ADMIN_COUNT = ADMIN_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    with open('robotic.png', 'rb') as photobot:
        phbot = photobot.read()
        await call.message.answer_photo(photo=phbot,
                                        caption="И вот, уже окончены 4 года обучения в колледже⏳ \n\nТеперь как дипломированный специалист, вы решаетесь подать резюме в одну компанию. И не зря, вас приглашают на собеседование. \nКак вы готовитесь к нему🕴?")
    with open('photo5.png', 'rb') as photo5:
        ph5 = photo5.read()
        await call.message.answer_photo(photo=ph5, reply_markup=question6)

    await call.message.delete()

@dp.callback_query_handler(text = ["answer1.5", "answer2.5","answer3.5","answer4.5"], state=StateBot.In_Question)
async def bot_quiz(call: CallbackQuery, state: FSMContext):
    id = [call.from_user.id]
    if call.data == 'answer1.5':
        cur.execute("UPDATE PLAYERS SET PROG_COUNT = PROG_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer2.5':
        cur.execute("UPDATE PLAYERS SET TESTER_COUNT = TESTER_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer3.5':
        cur.execute("UPDATE PLAYERS SET ANALYSE_COUNT = ANALYSE_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer4.5':
        cur.execute("UPDATE PLAYERS SET ADMIN_COUNT = ADMIN_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    with open('robotic.png', 'rb') as photobot:
        phbot = photobot.read()
        await call.message.answer_photo(photo=phbot,caption="Вас успешно взяли на работу🎉 Усердно трудясь, вы считаете, что заслужили повышение зарплаты и хотите пойти просить начальника об этом. \n\nКак поступите в данной ситуации?")
    with open('photo6.png', 'rb') as photo6:
        ph6 = photo6.read()
        await call.message.answer_photo(photo=ph6, reply_markup=question7)

    await call.message.delete()

@dp.callback_query_handler(text = ["answer1.6", "answer2.6","answer3.6","answer4.6"], state=StateBot.In_Question)
async def bot_quiz(call: CallbackQuery, state: FSMContext):
    id = [call.from_user.id]

    await call.message.answer("По-итогу, вас сократили из-за внутренних проблем в кампании🙁 После всего этого, вы потратили очень много сил на освоение новой профессии.")

    if call.data == 'answer1.6':
        cur.execute("UPDATE PLAYERS SET PROG_COUNT = PROG_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer2.6':
        cur.execute("UPDATE PLAYERS SET TESTER_COUNT = TESTER_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer3.6':
        cur.execute("UPDATE PLAYERS SET ANALYSE_COUNT = ANALYSE_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    if call.data == 'answer4.6':
        cur.execute("UPDATE PLAYERS SET ADMIN_COUNT = ADMIN_COUNT + 1 WHERE TG_ID = %s", id)
        con.commit()
    id = [call.from_user.id]
    cur.execute("SELECT PROG_COUNT,TESTER_COUNT, ANALYSE_COUNT, ADMIN_COUNT FROM PLAYERS where TG_ID=%s;", id)
    datas = cur.fetchall()
    prog = datas[0][0]
    test = datas[0][1]
    anal = datas[0][2]
    admin = datas[0][3]
    # print(f"{prog} -  {type(prog)}")
    labels = 'Ответы за \n\nпрограммиста\n', 'Ответы за \n\nтестировщика\n', 'Ответы за \n\nаналитика\n', 'Ответы за \n\nадминистратора\n'

    values = [prog, test, anal, admin]
    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=labels, autopct='%1.2f%%')
    ax1.axis('equal')
    plt.savefig('saved_figure.png')
    photo = InputFile("saved_figure.png")
    if prog == max(prog, test, anal, admin):
        print(prog)
        print(call.from_user.full_name)
        await call.message.answer_photo(photo=photo, caption='В конце концов, вы стали программистом. Чтобы продолжить - нажмите "🚪Начать🚪"', reply_markup=start_button)

        await StateBot.In_choice_prog.set()
    elif test == max(prog, test, anal, admin):
        print(test)
        await call.message.answer_photo(photo=photo,caption='В конце концов, вы решили начать карьеру тестировщика. Чтобы приступить к стажировке, нажмите "🚪Начать🚪"', reply_markup=start_button)
        await StateBot.In_choice_tester.set()
    elif anal == max(prog, test, anal, admin):
        print(anal)
        await call.message.answer_photo(photo=photo,caption='В конце концов, вы решили начать карьеру аналитика данных. Чтобы приступить к стажировке, нажмите "🚪Начать🚪"', reply_markup=start_button)
        await StateBot.In_choice_an.set()
    elif admin == max(prog, test, anal, admin):
        print(admin)
        await call.message.answer_photo(photo=photo, caption='В конце концов, вы решили начать карьеру системного администратора. Чтобы приступить к стажировке, нажмите "🚪Начать🚪"', reply_markup=start_button)
        await StateBot.In_choice_adm.set()

@dp.message_handler(text='🚪Начать🚪', state=StateBot.In_choice_prog)
async def bot_soru_aska_langly(message: types.Message):
    await message.answer("Перед вами встал вопрос - какой стек выбрать?", reply_markup=dop)
    await StateBot.In_Question.set()

@dp.callback_query_handler(text = ["web", "desktop","mobile"], state=StateBot.In_Question)
async def bot_quiz(call: CallbackQuery, state: FSMContext):
    if call.data == 'web':
        await StateBot.In_choice_web.set()
        await call.message.answer('В конце концов, вы стали веб-программистом. Чтобы продолжить - нажмите "🚪Начать стажировку🚪"', reply_markup=start_staj_button)
    if call.data == 'desktop':
        await StateBot.In_choice_des.set()
        await call.message.answer('В конце концов, вы стали разработчиком разработчиком десктоп приложений. Чтобы продолжить - нажмите "🚪Начать стажировку🚪"',reply_markup=start_staj_button)
    if call.data == 'mobile':
        await StateBot.In_choice_mob.set()
        await call.message.answer('В конце концов, вы стали разработчиком мобильных приложений. Чтобы продолжить - нажмите "🚪Начать стажировку🚪"', reply_markup=start_staj_button)
    await call.message.delete()
