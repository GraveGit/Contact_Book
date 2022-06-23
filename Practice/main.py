import tkinter as gui#библиотека для работы с графическим интерфейсом
import json #библиотека для работы c json файлами
import os.path  #библиотека для проверки существания БД
from tkinter import messagebox

class App (gui.Tk) :
    def __init__(self):
        super().__init__()
        base_contacks = File.open_base()
        root = gui.Tk() #создание окна gui
        self.title("Контакты") #редактирование заголовка программы
        self.geometry("450x700") #размер окна по умолчанию
        self.config(bg="pale green")
        menu = gui.Menu(self)
        menu.add_command(label='Все контакты', command=self.show_all(base_contacks=base_contacks))
        menu.add_command(label='Добавить контакт', command=File.write_base(base_contacks=base_contacks))
        menu.add_command(label='изменить контакт', command=redact7)
        self.config(menu=menu)
        self.protocol("WM_DELETE_WINDOW", gui.Tk.on_closing)
        self.show_all(base_contacks=base_contacks)

    def show_all(self, base_contacks) :
        for iter in range(int(base_contacks["contacks"]["count_contacks"])+1) :
            print(base_contacks["contacks"][str(iter)]["fio"])
            print(base_contacks["contacks"][str(iter)]["number_phone"])
            self.list = gui.Listbox(self)
            self.scroll = gui.Scrollbar(self, orient=gui.VERTICAL,
                                   command=self.list.yview)
            self.list.config(yscrollcommand=self.scroll.set)
            self.list.insert(0, base_contacks["contacks"][str(iter)]["fio"])
            self.list.pack(side=gui.LEFT)
            self.scroll.pack(side=gui.LEFT, fill=gui.Y)


class File (App):
    def write_base (base_contacks) :
        count_contacks = int(base_contacks["contacks"]["count_contacks"])
        count_contacks += 1
        #fio = input_fio.get()
        #number_phone = input_number.get()

        fio = input()
        number_phone = input()

        base_contacks["contacks"][count_contacks] = { "fio" : fio, "number_phone" : str(number_phone) }
        base_contacks["contacks"]["count_contacks"] = str(count_contacks)
        with open("base.json", "r+", encoding="utf-8") as write_base :
            write_base.truncate(0)
            write_base.seek(0)
            json.dump(base_contacks, write_base, indent = 4)
        messagebox.showinfo("Контакты", "Контакт внесен в\nбазу данных")
    def open_base(self = None) :
        if ( not os.path.isfile("base.json")) : #проверка на сущетвование БД
            messagebox.showerror("Error!", "В базе данных нет контактов.\nВнесите хотя бы один контакт.") #выводит всплывающее окно
            contacks = {
                            "contacks": {
                                "count_contacks": -1
                                }
                            }
            with open("base.json", "x", encoding="utf-8") as base : #открываем файл БД для занесения первого контакта
                json.dump(contacks, base, indent=4)
            self.write_base(contacks)
        else :
            with open("base.json", "r", encoding="utf-8") as base : #открытие файла БД в режиме чтения
                base_contacks = json.load(base)
                return base_contacks




app = App()
app.mainloop()
