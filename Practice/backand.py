from tkinter import messagebox
import json #библиотека работы с json файлами
import os.path #библиотека для проверки сущетсвования БД

class File ():

    def __init__(self) -> None: #муть какая-то с конструкторами. После добавления некоторые неприятные моменты ушли. Степень нужности не могу сказать
        pass

    def write_base (self, contakt) : #запись в базу данных
        base_contacks = self.open_base() #чтение базы данных и получение директории с уже записанными
        count_contacks = int(base_contacks["contacks"]["count_contacks"]) #получение количества сущетсвующих контактов
        count_contacks += 1 #увеличение сущетсвующих контактов на 1
        base_contacks["contacks"][count_contacks] = contakt #добавление в полученную директорию полученный список с данными контакта
        base_contacks["contacks"]["count_contacks"] = str(count_contacks) #обновление счётчика контактов
        with open("base.json", "r+", encoding="utf-8") as write_base : #запись директории в json файл
            write_base.truncate(0)
            write_base.seek(0)
            json.dump(base_contacks, write_base, indent = 4)
        messagebox.showinfo("Контакты", "Контакт внесен в\nбазу данных")

    def open_base(self) :
        if ( not os.path.isfile("base.json")) : #проверка на сущетвование БД
            messagebox.showerror("Error!", "В базе данных нет контактов.\nВнесите хотя бы один контакт.") #выводит всплывающее окно
            contacks = {
                            "contacks": {
                                "count_contacks": -1
                                }
                            } #создание директории-шаболона БД
            with open("base.json", "x", encoding="utf-8") as base : #создаем файл БД для занесения шаблона БД
                json.dump(contacks, base, indent=4) #запись шаблона в созданный файл БД
            return None #возвращаем 0, так как в БД ничего нет(пустая)
        else :
            with open("base.json", "r", encoding="utf-8") as base : #открытие файла БД в режиме чтения
                base_contacks = json.load(base) #получение директории с контактами
                return base_contacks #возвращение директории с контактами

    def redact_base7 (self, contakt) : #метод редактрирования с предварительном поиском контакта. Не думал еще по поводу оптимизации при внедрении find_contackt()
        base_contacks = self.open_base() #полчучение директории со всеми контактами
        succsess = False
        for iter in range(int(base_contacks["contacks"]["count_contacks"])+1) : #перебор директории с контактами
            if (contakt["old"]["fio"] == base_contacks["contacks"][str(iter)]["fio"]) :#сравнивание с полученным ФИО с ФИО из директории
                base_contacks["contacks"][str(iter)]["fio"] = contakt["new"]["fio"] #суда не добралась реализация вариативности редактирования, поэтому просто старые_данные = новые
                base_contacks["contacks"][str(iter)]["number_phone"] = contakt["new"]["number_phone"]
                succsess = True
                with open("base.json", "r+", encoding="utf-8") as write_base : #запись обновленной директории в БД
                    write_base.truncate(0)
                    write_base.seek(0)
                    json.dump(base_contacks, write_base, indent = 4)
        if (succsess) : #если контакт был найден и отредактирован, то бросам инфо-окно
            messagebox.showinfo("Контакты", "Контакт отредактирован")
            return True
        else : #если нет - то ванинг-окно
            messagebox.showwarning("Ошибка1", "Контакт с таким\nФИО не найден!")
            return False 

    def find_contackt (self, fio) : #метод поиска контакта
        base_contacks = self.open_base() #получение директории с контактами из бд
        for iter in range(int(base_contacks["contacks"]["count_contacks"]) + 1) : #проход по директории
            if (fio == base_contacks["contacks"][str(iter)]["fio"]) : #сравнение полученного ФИО с ФИО из директории
                contakt = { "fio" : base_contacks["contacks"][str(iter)]["fio"], #записываем в список данные найденного контакта
                "number_phone" : base_contacks["contacks"][str(iter)]["number_phone"] }
                return contakt #возвращаем этот список
        return False #если не вернули список, то возвращаем None
