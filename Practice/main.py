import tkinter as gui#библиотека для работы с графическим интерфейсом
import json #библиотека для работы c json файлами
import os.path  #библиотека для проверки существания БД
from tkinter import messagebox


def open_file() : #функция открытия БД при запуске приложения
    if ( not os.path.isfile("base.json")) : #проверка на сущетвование БД
        messagebox.showerror("Error!", "В базе данных нет контактов.\nВнесите хотя бы один контакт.") #выводит всплывающее окно
        fio = input()
        print("Введите номер телефона " + fio)
        number_phone = input() #c реализацией бд есть нюансы, поэтому тут не идеально все.
        count_contacks = '0'
        contacks = { "contacks":  { "count_contacks" : count_contacks, count_contacks : { "fio" : fio, "number_phone": str(number_phone) } } }
        with open("base.json", "x", encoding="utf-8") as base : #открываем файл БД для занесения первого контакта
            file = json.dump(contacks, base, indent=4)
        print("Если хотите продолжить добавление контактов то, нажмите 1, если нет то - 0.")
        wish = input()
        if(wish) :
            write_file() #переход к функции добавления контактов
    with open("base.json", "r", encoding="utf-8") as base : #открытие файла БД в режиме чтения
        file = json.load(base)
        return file #возвращение в функцию объекта, который содержит в себе файл грубо говоря
    

def write_file () : #функция записи контактов в БД
    window1 = gui.Toplevel()
    window1.title("Создание контакта")
    window1.geometry("450x300")
    window1.resizable(width=True, height=False)
    
    label_output = gui.Label(window1, text="Заполните поля, а затем нажмите кнопку \"Создать\"", font=("Comic Sans MS", 12))
    label_output.pack(padx=0, pady=1)

    fio_text = gui.StringVar()
    fio_text.set("FIO")
    input_fio = gui.Entry(window1, width = 50, bg="dark sea green", textvariable = fio_text)
    input_fio.pack(pady=10)

    input_number = gui.Entry(window1, width = 50, bg="dark sea green")
    input_number.insert(0, "Номер телефона")
    input_number.pack(pady=11)

    button0 = gui.Button(window1, text="Отмена", font=("Comic Sans MS", 12), bg="orange red", command=window1.destroy)
    button0.place(width=80, height=30, relx =0.99, rely = 0.99, anchor="se")

    sleep_var = gui.IntVar()
    button = gui.Button(window1, text="Создать", font=("Comic Sans MS", 12), bg="green", command=lambda: sleep_var.set(1))
    button.place(relx=.5, rely=.8, anchor="c")
    button.wait_variable(sleep_var)

    with open("base.json", "r+", encoding="utf-8") as write_base :
        file = json.load(write_base)
        count_contacks = int(file["contacks"]["count_contacks"])
        count_contacks += 1
        str(count_contacks)
        fio = input_fio.get()
        number_phone = input_number.get()
        file["contacks"][count_contacks] = { "fio" : fio, "number_phone" : str(number_phone) }
        file["contacks"]["count_contacks"] = count_contacks
        write_base.truncate(0)
        write_base.seek(0)
        json.dump(file, write_base, indent = 4)
    messagebox.showinfo("Контакты", "Контакт внесен в\nбазу данных")
    window1.destroy()
    window1.mainloop()

def show_all() :
    pass

def redact7() :
    pass
def redact() :
    pass

def on_closing():
    if messagebox.askokcancel("Выход", "Вы действительно хотите выйти?"):
        root.destroy()
        exit(0)


root = gui.Tk() #создание окна gui
root.title("Контакты") #редактирование заголовка программы
root.geometry("450x700") #размер окна по умолчанию
root.config(bg="pale green")

menu = gui.Menu(root)
menu.add_command(label='Все контакты', command=show_all)
menu.add_command(label='Добавить контакт', command=write_file)
menu.add_command(label='Изменить контакт', command=redact7)
root.config(menu=menu)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop() #запуск непрерывного обновления окна программы до завершения ее работы каким-либо образом"""
