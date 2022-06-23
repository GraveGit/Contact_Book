import tkinter as tk
from tkinter import *  # библиотека для работы с графическим интерфейсом
from tkinter.scrolledtext import ScrolledText
import json  # библиотека для работы c json файлами
import os.path  # библиотека для проверки существания БД
from tkinter import messagebox


def open_file():  # функция открытия БД при запуске приложения
    print("кнопка работает")
    # выводит всплывающее окно
    messagebox.showinfo("Результат нажатия кнопки",
                        "Была нажата кнопка\n это результат ее нажатия\nтак же был выведен текст в консоль")
    if (not os.path.isfile("base.json")):  # проверка на сущетвование БД
        print("В базе данных нет контактов. Внесите хотя бы один контакт. Введите ФИО контакта.")
        fio = input()
        print("Введите номер телефона " + fio)
        # c реализацией бд есть нюансы, поэтому тут не идеально все.
        number = input()
        contacts = {"contacts": [
            {"fio": "Alexander Sergeevich", "number_phone": "+7922229999"}]}
        # открываем файл БД для занесения первого контакта
        with open("base.json", "x", encoding="utf-8") as base:
            file = json.dump(contacts, base, indent=4)
        print("Если хотите продолжить добавление контактов то, нажмите 1, если нет то - 0.")
        wish = input()
        if(wish):
            write_file()  # переход к функции добавления контактов
    with open("base.json", "r", encoding="utf-8") as base:  # открытие файла БД в режиме чтения
        file = json.load(base)
        return file  # возвращение в функцию объекта, который содержит в себе файл грубо говоря


def write_file():  # функция записи контактов в БД
    pass

#file = open_file()
# print(file)
# print(file["contacks"])
# print(file["contacks"]["fio"])


root = Tk()  # создание окна gui
root.title("Contacks")  # редактирование заголовка программы
root.geometry("450x700")  # размер окна по умолчанию

btn_all = Button(root, text="Показать все контакты", font=(
    "Proxima Nova", 18), command=open_file)  # создание кнопки
# добавление кнопки в окно программы со смещением по Y-ку на 10 единиц
btn_all.pack(pady=10)

st = ScrolledText(root, width=50,  height=10)
st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
st.insert(tk.INSERT, "Hello")


root.mainloop()  # запуск непрерывного обновления окна программы до завершения ее работы каким-либо образом
