from backand import File #подключение нашего подмодуля с классом для работы с файлами и данными
import tkinter as gui #подключение графической библиотеки
from tkinter import messagebox #подключение метода из графической библиотеки для создания всплывающих окон
from tkinter import ttk #метод из графической библиотеки для создания выпадающего списка


class App (gui.Tk, File) :

    def show_all(self) :
        base_contacks = self.open_base() #получаем директорию с контактами из БД
        if(not base_contacks) : return None #если директория пустая, то функция завершает работу
        self.list.delete(0, "end") #перед добавлением новой информации, удаляем старую
        contacks = list() #инициализация списка контактов
        for iter in range(int(base_contacks["contacks"]["count_contacks"])+1) :
            self.list.insert(0, base_contacks["contacks"][str(iter)]["fio"]) #вывод ФИО контактов в главное окно
            contacks.append(base_contacks["contacks"][str(iter)]["fio"]) #заполнение списка контактов
        return contacks #возврат в функцию сформированного списка контактов из фИО
    
    def show_contakt(self, contackt) : #показ выбранного контакта. в аргумент получаем список с его данными
        frame = gui.Frame(self, bg="red")
        frame.pack(side=gui.RIGHT, fill=gui.Y)

    def on_selection(self, even) : #функция обработки двойного клика(выбора) по контакту(-а)
        fio = self.list.get(self.list.curselection()) #функция возвращает ФИО контакта, который выбрали и записывает в переменную
        contackt = self.find_contackt(fio=fio) #обращаемся к фукнции поиска контакта по ФИО.
        if (contackt) : #если фукнци поиска вернула данные контакта, а не None, 
            self.show_contakt(contackt=contackt) #то передаем эти данные в функцию показа контакта
        else :
            self.show_all() #иначе обновляем список всех контактов (он устарел и был выбран удаленный или незаписанный контакт или еще какой-то баг)
            messagebox.showerror("Ошибка!", "Контакт не был найден в\n базе данных. Список контактов был обновлен.\nПовторите выбор контакта.") #бросаем ошибку пользователю
            
    def __init__(self): #метод инициализации класса
        super().__init__() #функия переопредления метода базового класса
        menu = gui.Menu(self) #создаем меню
        menu.add_command(label='Все контакты', command=self.show_all) #добавляем три пунка в меню
        menu.add_command(label='Добавить контакт', command=self.create_contakt)
        menu.add_command(label='Изменить контакт', command=self.redact_contact7)
        self.config(menu=menu) #добавляем меню в главное окно
        self.list = gui.Listbox(self, font=("Comic Sans MS", 12), bg="pale green", width=20) #создаем поле для вывода всех контактов
        self.scroll = gui.Scrollbar(self, orient=gui.VERTICAL, command=self.list.yview) #создаем полосу прокрутки, если контакты не помещаются на экран
                                #можно создать и горизонтальную, но это хотелось бы сделать ее динамической. Поэтому сначала основные задачи, а затем украшение
        self.list.config(yscrollcommand=self.scroll.set) #соединение полосы прокрутки со списком контактов
        self.list.pack(side=gui.LEFT, fill=gui.Y) #добавление списка контактов на главное окно, а затем
        self.scroll.pack(side=gui.LEFT, fill=gui.Y) #полосы прокрутки
        self.list.bind('<Double-Button-1>', self.on_selection) #метод считывания двойного клика по контакту и вызова обрабатывающей функции
        self.show_all() #вызов функции показа всех контактов

    def create_contakt(self) : #медот создания контакта
        window1 = gui.Toplevel() #создание вторичного окна
        window1.title("Создание контакта") 
        window1.geometry("450x300")
        window1.resizable(width=True, height=False) #запрет на изменение высоты втор. окна
        label_output = gui.Label(window1, text="Заполните поля, а затем нажмите кнопку \"Создать\"", font=("Comic Sans MS", 12))
        label_output.pack(padx=0, pady=1) #создание, а затем добавление на втор. окно вспомогательной надписи
        fio_text = gui.StringVar() #создание тех. стринговой переменной
        fio_text.set("FIO") #настройка значения тех. переменной
        input_fio = gui.Entry(window1, width = 50, bg="dark sea green", textvariable = fio_text) #создание поля ввода инмени
        input_fio.pack(pady=10) #размещение поля ввода имени на втор. окне
        input_number = gui.Entry(window1, width = 50, bg="dark sea green") #создание поля ввода номера телефона
        input_number.insert(0, "Номер телефона") #вставка пояснительно текста в поле
        input_number.pack(pady=11) #размещение поля ввода на втор. окне
        button0 = gui.Button(window1, text="Отмена", font=("Comic Sans MS", 12), bg="orange red", command=window1.destroy) #создание кнопки "отмена" для корректного выхода из окна
        button0.place(width=80, height=30, relx =0.99, rely = 0.99, anchor="se") #добавление кнопки на втор. окно
        sleep_var = gui.IntVar() #создание тех. интовой переменной
        button = gui.Button(window1, text="Создать", font=("Comic Sans MS", 12), bg="green", command=lambda: sleep_var.set(1)) #создание кнопки создания контакта
        button.place(relx=.5, rely=.8, anchor="c") #размещение кнопки контакта
        button.wait_variable(sleep_var) #функция ожидания, пока не нажмется копка "создать"
        fio = input_fio.get() #получение введенных данных в переменные
        number_phone = input_number.get()
        contakt = { "fio" : fio, "number_phone" : str(number_phone)} #создание списка из полученных данных
        self.write_base(contakt=contakt) #вызов функции записи данных в БД с передачей их в параметры
        self.show_all() #вызов функции показа всех контактов для обновления списка после добавления
        window1.destroy() #разрушение втор. окна
        window1.mainloop() #циклическое обновление втор. окна

    def redact_contact7(self) : #функция редактирования с предварительным выбором контакта 
        window2 = gui.Toplevel() #создание вторичного окна
        window2.title("Редактирование контакта") 
        window2.geometry("450x300")
        window2.resizable(width=True, height=False)
        label_output = gui.Label(window2, text="Заполните поля, а затем\nнажмите кнопку \"Отредактировать\"", font=("Comic Sans MS", 12))
        label_output.pack(padx=0, pady=1)
        contacks = self.show_all() #получение списка из ФИО всех контактов из БД
        cb_old_fio = ttk.Combobox(window2, values=contacks, font=("Comic Sans MS", 12)) #создание выпадающего списка
        cb_old_fio.insert(0, "Укажите текущее ФИО") #вставка пояснительного текста
        self.option_add('*TCombobox*Listbox.font', ("Comic Sans MS", 12)) #редактирование шрифтов в выпадающем списке
        cb_old_fio.pack(pady=10) #добавление выпадающего списка на втор. окно
        var_new_fio = gui.BooleanVar() #попытка реализовать вариативность редактирования
        var_new_phone = gui.BooleanVar()
        input_new_fio = gui.Entry(window2, width = 50, bg="dark sea green")
        input_new_fio.insert(0, "Новое ФИО")
        input_new_fio.pack(pady=10)
        check_new_fio = gui.Checkbutton(window2, text="Изменить ФИО", variable=input_new_fio.destroy)
        check_new_fio.select()
        check_new_fio.pack(pady=10)
        input_number = gui.Entry(window2, width = 50, bg="dark sea green")
        input_number.insert(0, "Новый номер телефона")
        input_number.pack(pady=11)
        button0 = gui.Button(window2, text="Отмена", font=("Comic Sans MS", 12), bg="orange red", command=window2.destroy)
        button0.place(width=80, height=30, relx =0.99, rely = 0.99, anchor="se")
        sleep_var = gui.IntVar()
        button = gui.Button(window2, text="Отредактировать", font=("Comic Sans MS", 12), bg="green", command=lambda: sleep_var.set(1))
        button.place(relx=.5, rely=.8, anchor="c")
        while True : #защита от неправильно введоного текущего фИО контакта, чтобы окно редактирования не закрывалось
            button.wait_variable(sleep_var)
            old_fio = cb_old_fio.get()
            if (var_new_fio) :
                new_fio = input_new_fio.get()
            else :
                new_fio = old_fio
            number_phone = input_number.get()
            contakt = {
            "old" : { "fio" : str(old_fio), "number_phone" : str(number_phone) },
            "new" : { "fio" : str(new_fio), "number_phone" : str(number_phone) } }
            if (self.redact_base7(contakt=contakt)) : break
            else : sleep_var.set(0)
        self.show_all()
        window2.destroy()
        window2.mainloop()
        messagebox.showinfo("Контакты" , "Контакт успешно\nотредактирован!")

    def on_closing(self):
        if messagebox.askokcancel("Выход", "Вы действительно хотите выйти?"):
            self.destroy() #закрытие главного окна
            exit(0) #завершение логических процессов. Закрыть так, чтоб прям навярника.
