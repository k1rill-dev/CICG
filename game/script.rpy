# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
default me = player_name
define player_name = 0
define right_choice = 0
define prog = 0
define test = 0
define anal = 0
define admin = 0

define gui.dialogue_text_outlines = [(0, "#00000080", 2, 2)]
define gui.interface_text_font = "20976.ttf"
define gui.choice_button_text_idle_color = '#000000'
define gui.choice_text_hover_color = '#000000'
define gui.text_color = "#000000"
define gui.name_xpos = 0.5
define gui.name_xalign = 0.5
define gui.namebox_width = 300
define gui.name_ypos = -22
define gui.namebox_borders = Borders(15, 7, 15, 7)
define gui.namebox_tile = True
define gui.name_text_size = 35
define gui.text_size = 30
define gui.skip_frame_borders = Borders(24, 8, 75, 8)
define gui.notify_frame_borders = Borders(24, 8, 60, 8)
define gui.notify_ypos = 68
define gui.skip_ypos = 15
define config.name = _("Center Invest Career")
define gui.show_name = True
define config.version = "1.0"
define gui.about = _("by BB")

define qr = Character('QR',color="000000")
define mom= Character('Мама', color="#000000")
define bob = Character('Боб', color="#030804")
define tch = Character('Вера Адольфовна', color="#20603d")
define mtch = Character('Айла', color="#c10020")
define rnm = Character('Однокурсница', color="#543b2a")
define scr = Character('Секретарша', color="#543b2a")
define bss = Character('Начальник', color="#1a162a")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene nebo with fade

    "До начала необходимо ответить на один вопрос"

    $ player_name = renpy.input("Как к вам обращаться?")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "человек, который не смог написать имя"

jump born

label born:

    scene child with fade

    "Сегодня мир обрел еще одного героя, и это [player_name]"

jump sand

label sand:

    scene sand with fade

    "В детстве вы были обычным скромным ребенком, который не любил драться и часто плакал по пустякам"

    "В один из обычных солнечных дней, вы замечаете местных хулиганов"

    "Они направляются прямо к вашей песочнице"

    show bob with fade

    bob "Эй, это ты [player_name]?"
    bob "Я тебя уже не в первый раз тут вижу"
    bob "Проваливай отсюда или я покажу тебе где раки зимуют"

    "Что вы предпримите?"
menu:
    "Бросить песок в глаза и дать отпор":
        $ prog += 1
        jump theatre
    "Попытаться уладить конфликт. Завести дружбу":
        $ test += 1
        jump theatre
    "Решить, что эта песочница не для меня.\nНайти другую":
        $ anal += 1
        jump theatre
    "Честно отстоять свою песочницу":
        $ admin += 1
        jump theatre

label theatre:

    scene theatre with fade

    "Каким бы детство не было беззабоным и радостным - оно закончилось"
    "Вы пошли в школу"
    "Успешно обучаясь 7 классов, произошел интересный случай..."
    "На уроке биологии появилась возможность получить оценку, если поставить сценку..."

    show tch with fade

    tch "Здравствуй, [player_name]"
    tch "Я слышала, что ты хотел принять участие в нашей школьной постановке"
    tch "Так ведь?"

menu:
    "Сделать всё, чтобы получить оценку":
        $ prog += 1
        jump exam
    "Не напрягаться. Не имееется нужды":
        $ test += 1
        jump exam
    "Стать паразитом в чужой сценке":
        $ anal += 1
        jump exam
    "Собрать свою актерскую команду":
        $ admin += 1
        jump exam

label exam:

    scene school_class with fade

    "Беззаботное детство незаметно прошло"

    "И вот уже 9 класс, а значит что и ОГЭ не за горами"

    show mtch with fade

    mtch "О. Привет [player_name]"
    mtch "Я тут прямо с занятий иду"
    mtch "А ты вообще собираешься готовиться к экзамену?"

menu:
    "Одолжить у кого-нибудь шпаргалки":
        $ prog += 1
        jump kvn
    "Организовать командную работу на экзамене":
        $ test += 1
        jump kvn
    "Подготовиться самостоятельно":
        $ anal += 1
        jump kvn
    "Найти готовые шпаргалки":
        $ admin += 1
        jump kvn

label kvn:

    scene standup with fade

    "Вы молодец"

    "Вы успешно сдали государственный экзамен и поступили в желаемый колледж"

    "Не успев переступить порог, вас подзывает симпатичная девушка"

    show rnm with fade

    rnm "Привет. Мы же с тобой на одном курсе учимся, да?"
    rnm "Я вот хотела пригласить тебя к нам в КВН-команду"
    rnm "Не отказывайся, будет весело. Заодно и познакомимся поближе"

menu:
    "Взять то, что останется":
        $ prog += 1
        jump exam_fail
    "Отказаться. Учеба превышего всего":
        $ test += 1
        jump exam_fail
    "Быть только капитаном":
        $ anal += 1
        jump exam_fail
    "Занять творческую позицию":
        $ admin += 1
        jump exam_fail

label exam_fail:

    scene school_dvor with fade

    "К сожалению, вы завалили один экзамен в колледже"

    show mom with fade

    mom "как ты мог завалить такой важный экзамен...?"
    mom "ну и как ты собираешься все исправлять"

menu:
    "Готовиться, но перестраховаться подарком":
        $ prog += 1
        jump withboss
    "Учердно подготовиться":
        $ test += 1
        jump withboss
    "Воспользоваться своими знаниями":
        $ anal += 1
        jump withboss
    "Провести диалог с преподавателем":
        $ admin += 1
        jump withboss

label withboss:

    scene centrinv with fade

    "И вот, уже окончены 4 года обучения в колледже"

    "Теперь как дипломированный специалист, вы решаетесь подать резюме в одну компанию"

    "И не зря, вас приглашают на собеседование"

    "На подходе к офису, вы сталкиваетесь с секретаршей"

    show scr with fade

    scr "[player_name], это ты?"
    scr "Давай быстрее, тебя уже заждались"
    scr "Надеюсь ты подготовился"

menu:
    "Не готовиться. Я - мое резюме":
        $ prog += 1
        jump salary
    "Сымпровизировать и сделать ставку на харизму":
        $ test += 1
        jump salary
    "Подготовиться: купить новый костюм":
        $ anal += 1
        jump salary
    "Изучить все о кампании, чтобы не облажать":
        $ admin += 1
        jump salary

label salary:

    scene boss_office with fade

    "Вас успешно взяли на работу"

    "Усердно трудясь, вы считаете, что заслужили повышение зарплаты"

    "Вы пошли в кабинет к начальнику"

    show bss with fade

    bss "Чего хотел? Повышения зарплаты не будет"
    bss "И точка."

menu:
    "Уйти во фриланс, чтобы не прогибаться":
        $ prog += 1
        jump newprof
    "Сделать все, чтобы меня честно повысили":
        $ test += 1
        jump newprof
    "Не спорить с начальником":
        $ anal += 1
        jump newprof
    "Попытаться выбить повышение легально":
        $ admin += 1
        jump newprof

label newprof:

    scene road with fade

    "По-итогу, вас сократили из-за внутренних проблем в кампании"
    "После всего этого, вы потратили очень много сил на освоение новой профессии"

    if prog == max(prog, test, anal, admin):
        "В конце концов, вы стали программистом"
        jump choiceprog
    elif test == max(prog, test, anal, admin):
        "В конце концов, вы решили начать карьеру тестировщика"
        jump tester
    elif anal == max(prog, test, anal, admin):
        "В конце концов, вы решили начать карьеру аналитика"
        jump analitik
    elif admin == max(prog, test, anal, admin):
        "В конце концов, вы решили начать карьеру системного администратора"
        jump adminis

label choiceprog:

    scene prog with fade

    "Перед вами встал вопрос - какой стек выбрать?"

menu:
    "Веб-разработка":
        "В конце концов, вы стали веб-программистом"
        jump webtest
    "Десктоп":
        "В конце концов, вы стали разработчиком разработчиком десктоп приложений"
        jump desktop
    "Мобильная разработка":
        "В конце концов, вы стали разработчиком мобильных приложений"
        jump mobile

label tester:

    "Настал ваш первый рабочий день в новой квалификации"

    "Вы должны протестировать веб-сайт"

    "Какой инструмент будете использовать?"

menu:
    "Selenium":
        $ right_choice += 1
    "Вручную":
        ""
    "Миллениум":
        ""

    "Вам осталось выбрать сервис для запуска легковесной оболочки"

    "Какой из них существует на самом деле?"

menu:
    "Контейнер":
        jump result
    "Docker":
        $ right_choice += 1
        jump result
    "Git push":
        jump result

label analitik:

    scene prog with fade

    "Настал ваш первый рабочий день в новой квалификации"

    "Необходимо осуществить формализацию модели"

    "А что такое собственно формализация?"

menu:
    "Представить в виде формальной системы или исчисления":
        ""

    "Представить в необходимом виде":
        ""

    "Представить программу в виде совокупности объектов":
        $ right_choice += 1
        ""


    "Как в excel таблице отделить целую часть от дробной"

menu:
    ".":
        jump result
    ";":
        jump result
    "Нет правильного ответа":
        $ right_choice += 1
        jump result

label adminis:

    scene prog with fade

    "Настал ваш первый рабочий день в новой квалификации"

    "В один из рабочих дней пришлось настроить сетевое оборудование"

    "Чему равняется адрес сети для префикса 172.30.60.0/20?"

menu:
    "172.30.16.01️":
        ""
    "172.30.32.02":
        ""
    "172.30.48.04":
        $ right_choice += 1

    "Письма из электронной почты скачиваются в устройство пользователя и затем удаляются с сервера"

    "По какому протоколу все осуществлялось?"

menu:
    "POP3":
        $ right_choice += 1
        jump result
    "IMAP":
        jump result
    "MAC":
        jump result


label desktop:

    scene prog with fade

    "Настал ваш первый рабочий день в новой квалификации"

    "И первой твоей задачей стало создание базового WPF-приложения"

    "Какой тег(xaml) является базовым в любом приложении?"

menu:
    "<Window></Window>":
        $ right_choice += 1
    "Main":
        ""
    "Window":
        ""

    "В каком состоянии приложение НЕ может пребывать(UWP C#)?"

menu:
    "Error":
        $ right_choice += 1
        jump result
    "Suspended":
        jump result
    "ClosedByUser":
        jump result

label mobile:

    scene prog with fade

    "Вас взяли на стажировку разработчиком мобильных приложений!"

    "И первой вашей задачей стало создание базового приложения"

    "Как называется среда разработки (Android)?"

menu:
    "PyCharm":
        ""
    "Android Studio":
        $ right_choice += 1
    "Notepad ++":
        ""

    "В каком состоянии приложение НЕ может пребывать?"

menu:
    "Error":
        $ right_choice += 1
        jump result
    "Suspended":
        jump result
    "ClosedByUser":
        jump result


label webtest:

    scene prog with fade

    "Настал ваш первый рабочий день в новой квалификации"

    "Первой вашей задачей стала центровка html-заголовков"

    "Как вы это сделаете?"

menu:
    "<center>":
        $ right_choice += 1
        ""
    "center":
        ""
    "headquaters":
        ""

    "В каком формате решите отправлять защищенные данные?"

menu:
    "Хешируем конфедициальные данные и передаем JSON с файлами":
        $ right_choice += 1
        jump result
    "Передаем JSON с данными":
        jump result
    "Отправляем данные в Google Drive":
        jump result

label result:

if right_choice >= 2 :
    scene yeah with fade
    'Поздравляем всей командой BB. Теперь ты достоин того, чтобы отпраить заявку в "Таланты Центр-Инвеста"'
    'По QR-коду переходи в нашего телеграмм бота, пройди дополнительную историю и заполни заявку на "Таланты Центр-Инвеста"'
    'Спасибо за игру!'
else:
    scene learn with fade
    'Сожалеем, но ваших знаний на данный момент недостаточно'
    'Можем предложить вам пройти пару курсов, перейдя по QR-коду"'
    'Спасибо за игру!'
