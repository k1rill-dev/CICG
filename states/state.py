# -- coding: utf-8 --
from aiogram.dispatcher.filters.state import StatesGroup, State

class StateBot(StatesGroup):
    In_Question = State()
    In_Result = State()
    In_Result_test = State()
    In_Result_adm = State()
    In_Result_an = State()


    In_choice_prog = State()
    In_choice_web = State()
    In_choice_des = State()
    In_choice_mob = State()
    In_choice_adm = State()
    In_choice_an = State()
    In_choice_tester = State()

    In_task = State()
    In_huaysk = State()

    In_task_des = State()
    In_huaysk_des = State()

    In_task_mob = State()
    In_huaysk_mob = State()

    In_task_tester = State()
    In_huaysk_tester = State()

    In_task_adm = State()
    In_huaysk_adm = State()

    In_task_an = State()
    In_huaysk_an = State()

    Get_mail_web = State()
    Get_mail_des = State()
    Get_mail_mob = State()
    Get_mail_adm = State()
    Get_mail_test = State()
    Get_mail_an = State()

    Set_mail_web = State()
    Set_mail_des = State()
    Set_mail_mob = State()
    Set_mail_adm = State()
    Set_mail_test = State()
    Set_mail_an = State()