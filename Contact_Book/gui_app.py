from unicodedata import name
from backand import File
import tkinter as gui
from tkinter import ttk, messagebox

class Create_contackt(gui.Toplevel) :
    reget = 1
    window_geometry="500x200"
    font=("Comic Sans MS", 12)
    bg="dark sea green"

    def __init__(self, window_geometry="500x200", font=("Comic Sans MS", 12), bg="dark sea green") :
        self.window_geometry = window_geometry
        self.font = font
        self.bg = bg
        super().__init__()
        self.title("Создание контакта")
        self.geometry(self.window_geometry)
        self.resizable(width=False, height=False)
        label_output = gui.Label(self, text="Заполните поля, а затем нажмите кнопку \"Создать\"", font=self.font)
        label_output.place(relx=0.5, rely=0.15, anchor="center")
        frame_left = gui.Frame(self, bd=0)
        frame_left.place(relx=.01, rely=.3, anchor="nw")
        self.input_1Name = gui.Entry(frame_left, width = 40, bg=self.bg)
        self.input_1Name.insert(0, "Имя")
        self.input_1Name.pack(side=gui.TOP, pady=5)
        self.input_2Name = gui.Entry(frame_left, width = 40, bg=self.bg)
        self.input_2Name.insert(0, "Фамилия")
        self.input_2Name.pack(side=gui.BOTTOM, pady=5)
        frame_right = gui.Frame(self, bd=0)
        frame_right.place(relx=.99, rely=.3, anchor="ne")
        self.input_number = gui.Entry(frame_right, width = 25, bg=self.bg)
        self.input_number.insert(0, "Номер телефона")
        self.input_number.pack(pady=5)
        self.input_mail = gui.Entry(frame_right, width = 25, bg=self.bg)
        self.input_mail.insert(0, "Почта")
        self.input_mail.pack(pady=5)
        button0 = gui.Button(self, text="Отмена", font=self.font, command=self.destroy)
        button0.place(width=80, height=30, relx =0.99, rely = 0.99, anchor="se")

    def form_contackt(self) :
        sleep_var = gui.IntVar()
        self.button = gui.Button(self, text="Создать", command=lambda: sleep_var.set(self.reget))
        self.button.place(relx=.5, rely=.8, anchor="c")
        self.button.wait_variable(sleep_var)
        Name1 = self.input_1Name.get()
        Name2 = self.input_2Name.get()
        number_phone = self.input_number.get()
        mail = self.input_mail.get()
        contackt = { "1Name": Name1, "2Name": Name2, "number_phone": number_phone, "mail": mail }
        return contackt
    
class Redactor_contackta (gui.Toplevel) :
    reget = 1
    window_geometry = "450x300"
    font=("Comic Sans MS", 12)
    bg="dark sea green"
    def __init__(self, contackt_from_base, geometry = "450x300" , font=("Comic Sans MS", 12), bg="dark sea green") :
        super().__init__()
        self.window_geometry = geometry
        self.font=font
        self.bg=bg
        self.title("Редактирование контакта" + contackt_from_base["1Name"] + contackt_from_base["2Name"])
        self.geometry(self.window_geometry)
        self.resizable(width=False, height=False)
        label_3 = gui.Label(self, text="Измените данные контакта и\nнажмите \"Отредактировать\" для сохранения изменений", font=self.font)
        label_3.pack(padx=0, pady=1)
        frame_left = gui.Frame(self, bd=0)
        frame_left.pack(side=gui.LEFT, padx=5)
        self.input_new_1Name = gui.Entry(frame_left, width = 50, bg=self.bg)
        self.input_new_1Name.insert(0, contackt_from_base["1Name"])
        self.input_new_1Name.pack(pady=5)
        self.input_new_2Name = gui.Entry(frame_left, width = 50, bg=self.bg)
        self.input_new_2Name.insert(0, contackt_from_base["2Name"])
        self.input_new_2Name.pack(pady=5)
        frame_right = gui.Frame(self, bd=0)
        frame_right.pack(side=gui.RIGHT, padx=5)
        self.input_number = gui.Entry(frame_right, width = 50, bg=self.bg)
        self.input_number.insert(0, str(contackt_from_base["number_phone"]))
        self.input_number.pack(pady=5)
        self.input_mail = gui.Entry(frame_right, width = 50, bg=self.bg)
        self.input_mail.insert(0, str(contackt_from_base["mail"]))
        self.input_mail.pack(side=gui.RIGHT, pady=5)
        button0 = gui.Button(self, text="Отмена", font=self.font, command=self.destroy)
        button0.place(width=80, height=30, relx =0.99, rely = 0.99, anchor="se")
        
    def form_contackt(self, contackt_from_base) :
        sleep_var = gui.IntVar()
        button = gui.Button(self, text="Отредактировать", font=self.font, bg=self.bg, command=lambda: sleep_var.set(self.reget))
        button.place(relx=.5, rely=.8, anchor="c")
        button.wait_variable(sleep_var)
        new_1Name = self.input_new_1Name.get()
        new_2Name = self.input_new_2Name.get()
        number_phone = self.input_number.get()
        mail = self.input_mail.get()
        contackt = {
        "old" : contackt_from_base,
        "new" : { "1Name" : new_1Name, "2Name" : new_2Name, "number_phone" : str(number_phone), "mail" : mail } }
        return contackt

class Redact_contact7 (gui.Toplevel) :
    reget = 1
    window_geometry = "450x300"
    font=("Comic Sans MS", 12)
    bg="dark sea green"

    def __init__(self, contacks, geometry = "450x300" , font=("Comic Sans MS", 12), bg="dark sea green") :
        super().__init__()
        self.window_geometry = geometry
        self.font = font
        self.bg = bg
        self.title("Редактирование контакта")
        self.geometry("450x300")
        self.resizable(width=True, height=False)
        self.label_1_in_redact_contact_7 = gui.Label(self, text="Выберите контакт для редактирования", font=("Comic Sans MS", 12))
        self.label_1_in_redact_contact_7.pack(padx=0, pady=1)
        self.cb_old_fio = ttk.Combobox(self, values=contacks, font=("Comic Sans MS", 12))
        self.cb_old_fio.insert(0, "Выберите контакт по Имя Фамилия")
        self.option_add('*TCombobox*Listbox.font', ("Comic Sans MS", 12))
        self.cb_old_fio.pack(pady=10)
        self.sleep_var = gui.IntVar()
        self.cb_old_fio.bind("<<ComboboxSelected>>", self.combox_event)
        self.cb_old_fio.wait_variable(self.sleep_var)

    def combox_event(self, event) :
        self.sleep_var.set(1)
        self.cb_old_fio.config(state="disable")
        self.label_1_in_redact_contact_7.destroy()

    def change_contact(self, contackt_from_base):
        label_2 = gui.Label(self, text="Измените данные контакта и\nнажмите \"Отредактировать\" для сохранения изменений", font=("Comic Sans MS", 12))
        label_2.pack(padx=0, pady=1)
        frame_left = gui.Frame(self, bd=0)
        frame_left.pack(side=gui.LEFT, pady=5, padx=10)
        self.input_new_1Name = gui.Entry(frame_left, width = 50, bg="dark sea green")
        self.input_new_1Name.insert(0, contackt_from_base["1Name"])
        self.input_new_1Name.pack(pady=10)
        self.input_new_2Name = gui.Entry(frame_left, width = 50, bg="dark sea green")
        self.input_new_2Name.insert(0, contackt_from_base["2Name"])
        self.input_new_2Name.pack(pady=10)
        frame_right = gui.Frame(self, bd=0)
        frame_right.pack(side=gui.RIGHT, padx=5, pady=10)
        self.input_number = gui.Entry(frame_right, width = 50, bg="dark sea green")
        self.input_number.insert(0, str(contackt_from_base["number_phone"]))
        self.input_number.pack(pady=10)
        self.input_mail = gui.Entry(frame_right, width = 50, bg="dark sea green")
        self.input_mail.insert(0, str(contackt_from_base["mail"]))
        self.input_mail.pack(pady=10)
        button0 = gui.Button(self, text="Отмена", font=("Comic Sans MS", 12), command=self.destroy)
        button0.place(width=80, height=30, relx =0.99, rely = 0.99, anchor="se")

    def form_contact(self, contackt_from_base):
        sleep_var = gui.IntVar()
        button = gui.Button(self, text="Отредактировать", font=("Comic Sans MS", 12), bg="green", command=lambda: sleep_var.set(self.reget))
        button.place(relx=.5, rely=.8, anchor="c")
        button.wait_variable(sleep_var)
        Name1 = self.input_new_1Name.get()
        Name2 = self.input_new_2Name.get()
        number_phone = self.input_number.get()
        mail = self.input_mail.get()
        contakt = {
        "old" : contackt_from_base,
        "new" : { "1Name": Name1, "2Name": Name2, "number_phone": number_phone, "mail": mail } }
        return contakt

class Parameters(gui.Toplevel) :
    main = {'geometry' : str(), 'bg' : str(), 'font_name' : str(), 'font_size' : str() }
    create = {'geometry' : str(), 'bg' : str(), 'font_name' : str(), 'font_size' : str() }
    redact = {'geometry' : str(), 'bg' : str(), 'font_name' : str(), 'font_size' : str() }
    redact7 = {'geometry' : str(), 'bg' : str(), 'font_name' : str(), 'font_size' : str() }
    parametr = {'geometry' : str(), 'bg' : str(), 'font_name' : str(), 'font_size' : str() }
    window = ['Маленькое', 'Среднее', 'Большое']
    bg = ['Офисный белый', 'Офисный темный', 'Успокаивающий зеленый', 'Спортивный красный']
    font_name = ['Офисный обычный', 'Красивый обычный', 'Красивый']
    font_size = ['Маленький', 'Средний', 'Большой']
    now_changes = str()

    def __init__ (self, parameters, win_geometry, bg, font) :
        super().__init__()
        self.main = parameters['main']
        self.create = parameters['create']
        self.redact = parameters['redact']
        self.redact7 = parameters['redact7']
        self.parametr = parameters['parametr']
        self.title("Параметры")
        self.geometry(win_geometry)
        self.resizable(width=False, height=False)
        self.pmen = gui.Menu(self, font=font)
        self.pmen.add_command(label='Главное окно программы', command=self.parameters_main)
        self.pmen.add_command(label='Окно создания контакта', command=self.parameters_creaete)
        self.pmen.add_command(label='Окно редактирования контакта', command=self.parameters_redactor)
        self.pmen.add_command(label='Окно редактирования неизвестного контакта', command=self.parameters_redactor7)
        self.pmen.add_command(label='Окно параметров программы', command=self.parameters_param)
        self.Mmenu = gui.Menu(self, font=font)
        self.Mmenu.add_cascade(menu=self.pmen, label='Изменяемые окна')
        self.config(bg=bg, menu=self.Mmenu)
        self.lb1 = gui.Label(self, bg=bg, font=font, pady=0, justify=gui.CENTER)
        self.lb1.place(relx=.5, rely=.15, anchor='c',)
        self.frm_L = gui.Frame(self, bd=0, bg=bg)
        self.frm_L.place(relx=.01,rely=0.5, anchor='w')
        self.frm_R = gui.Frame(self, bd=0, bg=bg)
        self.frm_R.place(relx=.99,rely=0.5, anchor='e')
        self.lb_gm = gui.Label(self.frm_L, bg=bg, font=(font[0], font[1]-2), text='Размер окна:', anchor='c')
        self.lb_gm.pack(side=gui.TOP)
        self.cb_gm = ttk.Combobox(self.frm_L, font=font, values=self.window)
        self.option_add('*TCombobox*Listbox.font', font)
        self.cb_gm.pack(side=gui.TOP, pady=10)
        self.cb_bg = ttk.Combobox(self.frm_L, font=font, values=self.bg)
        self.cb_bg.pack(side=gui.BOTTOM, pady=10)
        self.lb_bg = gui.Label(self.frm_L, bg=bg, font=(font[0], font[1]-2), text='Цвет фона окна:', anchor='c')
        self.lb_bg.pack(side=gui.BOTTOM)
        self.lb_fnt_n = gui.Label(self.frm_R, bg=bg, font=(font[0], font[1]-2), text='Шрифт:', anchor='c')
        self.lb_fnt_n.pack(side=gui.TOP)
        self.cb_fnt_n = ttk.Combobox(self.frm_R, font=font, values=self.font_name)
        self.cb_fnt_n.pack(side=gui.TOP, pady=10)
        self.cb_fnt_s = ttk.Combobox(self.frm_R, font=font, values=self.font_size)
        self.cb_fnt_s.pack(side=gui.BOTTOM, pady=10)
        self.lb_fnt_s = gui.Label(self.frm_R, bg=bg, font=(font[0], font[1]-2), text='Размер шрифта:', anchor='c')
        self.lb_fnt_s.pack(side=gui.BOTTOM)
        self.save = gui.Button(self, command=lambda:self.save_message(bg=bg, font=font), font=font, text='Сохранить')
        self.save.place(relx=.5, rely=.85, anchor='c')
        self.save_and_quit = gui.Button(self, command=lambda:self.save_quit(bg=bg, font=font), font=font, text='Сохранить и выйти')
        self.save_and_quit.place(relx=.85, rely=.95, anchor='c')
        self.sleep_var = gui.IntVar()
        self.parameters_main()
        self.save.wait_variable(self.sleep_var)

    def save_quit (self, bg, font) :
        self.sleep_var.set(1)
        self.save_and_quit.config(state='disable')
        self.save_message(bg=bg, font=font)


    def save_message (self, bg, font) :
        self.lb2 = gui.Label(self, bg=bg, font=font, text='Данные сохранены')
        self.lb2.place(relx=.5, rely=.95, anchor='c')
        self.after(5000, lambda: self.lb2.destroy())
        self.save.config(state='disable')
        self.change(window=self.now_changes)

    def reload_comboboxs (self, insert) :
        self.cb_gm.delete(0, 'end')
        self.cb_bg.delete(0, 'end')
        self.cb_fnt_n.delete(0, 'end')
        self.cb_fnt_s.delete(0, 'end')

        self.cb_gm.insert(0, insert['geometry'])
        self.cb_bg.insert(0, insert['bg'])
        self.cb_fnt_n.insert(0, insert['font_name'])
        self.cb_fnt_s.insert(0, insert['font_size'])

    def change (self, window) :
        if window == 'main' :
            self.main['geometry'] = self.cb_gm.get()
            self.main['bg'] = self.cb_bg.get()
            self.main['font_name'] = self.cb_fnt_n.get()
            self.main['font_size'] = self.cb_fnt_s.get()
        if window == 'create' :
            self.create['geometry'] = self.cb_gm.get()
            self.create['bg'] = self.cb_bg.get()
            self.create['font_name'] = self.cb_fnt_n.get()
            self.create['font_size'] = self.cb_fnt_s.get()
        if window == 'redact' :
            self.redact['geometry'] = self.cb_gm.get()
            self.redact['bg'] = self.cb_bg.get()
            self.redact['font_name'] = self.cb_fnt_n.get()
            self.redact['font_size'] = self.cb_fnt_s.get()
        if window == 'redact7' :
            self.redact7['geometry'] = self.cb_gm.get()
            self.redact7['bg'] = self.cb_bg.get()
            self.redact7['font_name'] = self.cb_fnt_n.get()
            self.redact7['font_size'] = self.cb_fnt_s.get()
        if window == 'parametr' :
            self.parametr['geometry'] = self.cb_gm.get()
            self.parametr['bg'] = self.cb_bg.get()
            self.parametr['font_name'] = self.cb_fnt_n.get()
            self.parametr['font_size'] = self.cb_fnt_s.get()
    
    def parameters_main (self) :
        self.save.config(state='normal')
        self.reload_comboboxs(insert=self.main)
        self.lb1.config(text='''Редактирование главного окна программы.\nИзмените значения полей на нужные и нажмите "Сохранить"''')
        self.now_changes = 'main'

    def parameters_creaete (self) :
        self.save.config(state='normal')
        self.reload_comboboxs(insert=self.create)
        self.lb1.config(text='''Редактирование окна создания контакта.\nИзмените значения полей на нужные и нажмите "Сохранить"''')
        self.now_changes = 'create'
    
    def parameters_redactor (self) :
        self.save.config(state='normal')
        self.reload_comboboxs(insert=self.redact)
        self.lb1.config(text='''Редактирование окна редактирования контакта.\nИзмените значения полей на нужные и нажмите "Сохранить"''')
        self.now_changes = 'redact'

    def parameters_redactor7 (self) :
        self.save.config(state='normal')
        self.reload_comboboxs(insert=self.redact7)
        self.lb1.config(text='''Редактирование окна редактирования заранее неизвестного контакта.\nИзмените значения полей на нужные и нажмите "Сохранить"''')
        self.now_changes = 'redact7'

    def parameters_param (self) :
        self.save.config(state='normal')
        self.reload_comboboxs(insert=self.parametr)
        self.lb1.config(text='''Редактирование окна параметров.\nИзменения вступят после перезапуска окна.\nИзмените значения полей на нужные и нажмите "Сохранить"''')
        self.now_changes = 'parametr'

    def call_return_parameters (self) :
        parameters = dict()
        parameters['main'] = self.main
        parameters['create'] = self.create
        parameters['redact'] = self.redact
        parameters['redact7'] = self.redact7
        parameters['parametr'] = self.parametr
        return parameters

class App (gui.Tk, File) :
    main = {'geometry' : '500x700', 'bg' : 'pale green', 'font' : ['Script' , 12] }
    create = {'geometry' : '500x350', 'bg' : 'pale green', 'font' : ['Comic Sans MS' , 12] }
    redact = {'geometry' : '475x350', 'bg' : 'pale green', 'font' : ['Comic Sans MS' , 12] }
    redact7 = {'geometry' : '475x350', 'bg' : 'pale green', 'font' : ['Comic Sans MS' , 12] }
    parametr = {'geometry' : '550x400', 'bg' : 'pale green', 'font' : ['Comic Sans MS' , 12] }

    def __init__(self):
        super().__init__()
        self.load_from() #получение из конфигурационого файла значений параметров окон
        self.menu = gui.Menu(self)
        self.menu.add_command(label='Все контакты', command=self.show_all)
        self.menu.add_command(label='Добавить контакт', command=self.create_contakt)
        self.menu.add_command(label='Изменить контакт', command=self.redact_contact7)
        self.menu.add_command(label='Параметры', command=self.call_parameters)
        self.config(menu=self.menu, bg=self.main['bg'])
        self.geometry(self.main['geometry'])
        self.list = gui.Listbox(self, font=self.main['font'], bg=self.main['bg'], width=25)
        self.scroll = gui.Scrollbar(self, orient=gui.VERTICAL, command=self.list.yview)
        self.list.config(yscrollcommand=self.scroll.set)
        self.list.pack(side=gui.LEFT, fill=gui.Y)
        self.scroll.pack(side=gui.LEFT, fill=gui.Y)
        self.list.bind('<<ListboxSelect>>', self.on_selection)
        self.show_all()
        self.label_1Name = gui.Label(self, text="Имя:", bd=0, bg=self.main['bg'])
        self.entry_1Name = gui.Entry(self, width=20, font=self.main['font'], bg="gray")
        self.label_2Name = gui.Label(self, text="Фамилия:", bd=0, bg=self.main['bg'])
        self.entry_2Name = gui.Entry(self, width=20, font=self.main['font'], bg="gray")
        self.lable_number = gui.Label(self, text="Номер телефона:", bd=0, bg=self.main['bg'])
        self.entry_number = gui.Entry(self, width=20, font=self.main['font'], bg="gray")
        self.lable_mail = gui.Label(self, text="Почта:", bd=0, bg=self.main['bg'])
        self.entry_mail = gui.Entry(self, width=20, font=self.main['font'], bg="gray")
        self.label_1Name.pack(pady=20)
        self.entry_1Name.pack()
        self.label_2Name.pack(pady=20)
        self.entry_2Name.pack()
        self.lable_number.pack(pady=20)
        self.entry_number.pack()
        self.lable_mail.pack(pady=20)
        self.entry_mail.pack()
    
    def load_from (self) :
        Rparameters = self.work_configure(state='read')
        if not Rparameters :
            Rparameters = self.work_configure(state='read')
        self.main = Rparameters['main']
        self.create = Rparameters['create']
        self.redact = Rparameters['redact']
        self.redact7 = Rparameters['redact7']
        self.parametr = Rparameters['parametr']

    def create_contakt(self) :
        cc=Create_contackt(window_geometry=self.create['geometry'], bg=self.create['bg'], font=self.create['font'])
        contakt = dict()
        while True :
            contakt = cc.form_contackt()
            if (self.write_base(contakt=contakt)) :
                cc.destroy()
                break
            else :
                cc.reget = 0
        self.show_all()

    def PKM_menu(self, event) :
        index_select = self.list.curselection()
        ordinat = event.y_root
        for y in range(700) :
            index_return = self.list.nearest(y=y)
            if (index_select[0] == index_return) :
                ordinat = y + ( event.y_root - event.y)
                break
        self.contackt_menu.post(event.x_root, ordinat)

    def show_all(self) :
        base_contacks = self.open_base()
        self.list.delete(0, "end")
        if(not base_contacks) : 
            messagebox.showinfo("Контакты", "База данных пуста!\nСоздайте хотя бы один контакт!")
            return None
        contacks = list()
        for iter in range(len(base_contacks)) :
            self.list.insert("end", base_contacks[iter]["1Name"] + " " + base_contacks[iter]["2Name"])
            contacks.append( base_contacks[iter]["1Name"] + base_contacks[iter]["2Name"] )
        return contacks

    def on_selection(self, even) :
        index = self.list.curselection()
        contackt = self.find_contackt(index=index[0])
        if (contackt) :
            self.show_contakt(contackt=contackt)
        else :
            self.show_all()
            messagebox.showerror("Ошибка!", "Контакт не был найден в базе данных.\nСписок контактов был обновлен.\nПовторите выбор контакта.")

    def show_contakt(self, contackt=None, update=True) :
        self.contackt_menu = gui.Menu(self.menu, tearoff=0)
        self.contackt_menu.add_command(label='Редактирование контакта', command= lambda: self.redactor_contackta(contackt=contackt))
        self.contackt_menu.add_command(label='Удаление контакта', command= lambda: self.remove_contackt(contackt=contackt))
        self.list.bind('<Button-3>', self.PKM_menu)
        self.entry_1Name.config(state="normal")
        self.entry_2Name.config(state="normal")
        self.entry_number.config(state="normal")
        self.entry_mail.config(state="normal")
        self.entry_1Name.delete(0, "end")
        self.entry_2Name.delete(0, "end")
        self.entry_number.delete(0, "end")
        self.entry_mail.delete(0, "end")
        if(update):
            self.entry_1Name.insert(0, contackt["1Name"])
            self.entry_2Name.insert(0, contackt["2Name"])
            self.entry_number.insert(0, str(contackt["number_phone"]))
            if (contackt["mail"] != ""):
                self.entry_mail.insert(0, contackt["mail"])
        self.entry_1Name.config(state="readonly")
        self.entry_2Name.config(state="readonly")
        self.entry_number.config(state="readonly")
        self.entry_mail.config(state="readonly")

    def redactor_contackta(self, contackt) :
        contackt_from_base = self.find_contackt(Name1=contackt["1Name"], Name2=contackt["2Name"])
        rc = Redactor_contackta(contackt_from_base=contackt_from_base, geometry=self.redact['geometry'], bg=self.redact['bg'], font=self.redact['font'])
        rcontackt = dict()
        while True :
            rcontackt = rc.form_contackt(contackt_from_base=contackt_from_base)
            if (self.redact_base(contakt=rcontackt)) :
                rc.destroy()
                break
            else :
                rc.reget = 0
        self.show_all()
        self.show_contakt(contackt=rcontackt["new"])

    def redact_contact7(self, geometry = redact7['geometry'], bg = redact7['bg'], font=redact7['font']) :
        contacks = self.show_all()
        rc7 = Redact_contact7(contacks = contacks, geometry=geometry, bg=bg, font=font)
        contakt_0_in_redact_contact7 = self.find_contackt(index=rc7.cb_old_fio.current())
        rc7.change_contact(contackt_from_base = contakt_0_in_redact_contact7)
        rcontackt = dict()
        while True :
            rcontackt = rc7.form_contact(contackt_from_base = contakt_0_in_redact_contact7)
            if (self.redact_base(contakt=rcontackt)) :
                rc7.destroy()
                break
            else :
                rc7.reget = 0
        self.show_all()

    def remove_contackt(self, contackt) :
        if (self.remove_from_base(contackt)) :
            messagebox.showinfo("Удаление контакта", "Контакт успешно удален")
            self.show_all()
            self.show_contakt(update=False)
        else :
            messagebox.showerror("Ошибка", "При удалении произошла ошибка.\nКонтакт не удален")
            self.show_all()

    def num_to_user (self, var) :
        Rvar = dict()
        if var['bg'] == 'pale green' :
            Rvar['bg'] = 'Успокаивающий зеленый'
        elif var['bg'] == 'gray94' : #цвет окна по умолчанию
            Rvar['bg'] = 'Офисный белый'
        elif var['bg'] == 'gray' :
            Rvar['bg'] = 'Офисный темный'
        else : Rvar['bg'] = 'Спортивный красный'
        if var['font'][0] == 'Comic Sans MS' :
            Rvar['font_name'] = 'Красивый обычный'
        elif var['font'][0] == 'Times New Roman' :
            Rvar['font_name'] = 'Офисный обычный'
        else : Rvar['font_name'] = 'Красивый'
        if var['font'][1] == 12 :
            Rvar['font_size'] = 'Средний'
        elif var['font'][1] == 14 :
            Rvar['font_size'] = 'Большой'
        else : Rvar['font_size'] = 'Маленький'
        return Rvar

    def call_parameters (self) :
        Tmain = dict()
        Tcreate = dict()
        Tredact = dict()
        Tredact7 = dict()
        Tparametr = dict()

        Tmain = self.num_to_user(var=self.main)
        if self.main['geometry'] == '500x700' :
            Tmain['geometry'] = 'Маленькое'
        elif self.main['geometry'] == '600x700' :
            Tmain['geometry'] = 'Среднее'
        else : Tmain['geometry'] = 'Большое'
        
        Tcreate = self.num_to_user(var=self.create)
        if self.create['geometry'] == '475x350' :
            Tcreate['geometry'] = 'Среднее'
        elif self.create['geometry'] == '550x450' :
            Tcreate['geometry'] = 'Большое'
        else : Tcreate['geometry'] = 'Маленькое'
        
        Tredact = self.num_to_user(var=self.redact)
        if self.redact['geometry'] == '475x350' :
            Tredact['geometry'] = 'Среднее'
        elif self.redact['geometry'] == '550x450' :
            Tredact['geometry'] = 'Большое'
        else : Tredact['geometry'] = 'Маленькое'
        
        Tredact7 = self.num_to_user(var=self.redact7)
        if self.redact7['geometry'] == '475x350' :
            Tredact7['geometry'] = 'Среднее'
        elif self.redact7['geometry'] == '550x450' :
            Tredact7['geometry'] = 'Большое'
        else : Tredact7['geometry'] = 'Маленькое'
        
        Tparametr = self.num_to_user(var=self.parametr)
        if self.parametr['geometry'] == '550x400' :
            Tparametr['geometry'] = 'Маленькое'
        elif self.parametr['geometry'] == '600x450' :
            Tparametr['geometry'] = 'Среднее'
        else : Tparametr['geometry'] = 'Большое'
        
        Textparameters = {'main' : Tmain, 'create' : Tcreate, 'redact' : Tredact, 'redact7' : Tredact7, 'parametr' : Tparametr}
        pm = Parameters(parameters=Textparameters, win_geometry=self.parametr['geometry'], bg=self.parametr['bg'], font=self.parametr['font'])
        Rparameters = pm.call_return_parameters()
        self.load_user_to_num_params(Rparameters=Rparameters)
        pm.destroy()

    def load_user_to_num_params(self, Rparameters) :
#   MAIN
        reloadapp = True
        if Rparameters['main']['geometry'] == 'Маленькое' :
            if self.main['geometry'] == '500x700' : reloadapp = False
            self.main['geometry'] = '500x700'
        elif Rparameters['main']['geometry'] == 'Среднее' :
            if self.main['geometry'] == '600x700' : reloadapp = False
            self.main['geometry'] = '600x700'
        else :
            if self.main['geometry'] == '700x850' : reloadapp = False
            self.main['geometry'] = '700x850'

        if Rparameters['main']['bg'] == 'Успокаивающий зеленый' :
            self.main['bg'] = 'pale green'
        elif Rparameters['main']['bg'] == 'Офисный белый' :
            self.main['bg'] = 'gray94'
        elif Rparameters['main']['bg'] == 'Спортивный красный' :
            self.main['bg'] = 'red'
        else : self.main['bg'] = 'gray'

        if Rparameters['main']['font_name'] == 'Красивый обычный' :
            self.main['font'][0] = 'Comic Sans MS'
        elif Rparameters['main']['font_name'] == 'Офисный обычный' :
            self.main['font'][0] = 'Times New Roman'
        else : self.main['font'][0] = 'Script'

        if Rparameters['main']['font_size'] == 'Средний' :
            self.main['font'][1] = 12
        elif Rparameters['main']['font_size'] == 'Большой' :
            self.main['font'][1] = 14
        else : self.main['font'][1] = 10
#   CREATE
        if Rparameters['create']['geometry'] == 'Маленькое' :
            self.create['geometry'] = '500x350'
        elif Rparameters['create']['geometry'] == 'Среднее' :
            self.create['geometry'] = '550x450'
        else : self.create['geometry'] = '600x500'

        if Rparameters['create']['bg'] == 'Успокаивающий зеленый' :
            self.create['bg'] = 'pale green'
        elif Rparameters['create']['bg'] == 'Офисный белый' :
            self.create['bg'] = 'gray94'
        elif Rparameters['create']['bg'] == 'Спортивный красный' :
            self.create['bg'] = 'red'
        else : self.create['bg'] = 'gray'

        if Rparameters['create']['font_name'] == 'Красивый обычный' :
            self.create['font'][0] = 'Comic Sans MS'
        elif Rparameters['create']['font_name'] == 'Офисный обычный' :
            self.create['font'][0] = 'Times New Roman'
        else : self.create['font'][0] = 'Script'

        if Rparameters['create']['font_size'] == 'Средний' :
            self.create['font'][1] = 12
        elif Rparameters['create']['font_size'] == 'Большой' :
            self.create['font'][1] = 14
        else : self.create['font'][1] = 10
#   REDACT
        if Rparameters['redact']['geometry'] == 'Маленькое' :
            self.redact['geometry'] = '500x350'
        elif Rparameters['redact']['geometry'] == 'Среднее' :
            self.redact['geometry'] = '550x450'
        else : self.redact['geometry'] = '600x500'

        if Rparameters['redact']['bg'] == 'Успокаивающий зеленый' :
            self.redact['bg'] = 'pale green'
        elif Rparameters['redact']['bg'] == 'Офисный белый' :
            self.redact['bg'] = 'gray94'
        elif Rparameters['redact']['bg'] == 'Спортивный красный' :
            self.redact['bg'] = 'red'
        else : self.redact['bg'] = 'gray'

        if Rparameters['redact']['font_name'] == 'Красивый обычный' :
            self.redact['font'][0] = 'Comic Sans MS'
        elif Rparameters['redact']['font_name'] == 'Офисный обычный' :
            self.redact['font'][0] = 'Times New Roman'
        else : self.redact['font'][0] = 'Script'

        if Rparameters['redact']['font_size'] == 'Средний' :
            self.redact['font'][1] = 12
        elif Rparameters['redact']['font_size'] == 'Большой' :
            self.redact['font'][1] = 14
        else : self.redact['font'][1] = 10
#   REDACT7
        if Rparameters['redact7']['geometry'] == 'Маленькое' :
            self.redact7['geometry'] = '500x350'
        elif Rparameters['redact7']['geometry'] == 'Среднее' :
            self.redact7['geometry'] = '550x450'
        else : self.redact7['geometry'] = '600x500'

        if Rparameters['redact7']['bg'] == 'Успокаивающий зеленый' :
            self.redact7['bg'] = 'pale green'
        elif Rparameters['redact7']['bg'] == 'Офисный белый' :
            self.redact7['bg'] = 'gray94'
        elif Rparameters['redacy7']['bg'] == 'Спортивный красный' :
            self.redact7['bg'] = 'red'
        else : self.redact7['bg'] = 'gray'

        if Rparameters['redact7']['font_name'] == 'Красивый обычный' :
            self.redact7['font'][0] = 'Comic Sans MS'
        elif Rparameters['redact7']['font_name'] == 'Офисный обычный' :
            self.redact7['font'][0] = 'Times New Roman'
        else : self.redact7['font'][0] = 'Script'

        if Rparameters['redact7']['font_size'] == 'Средний' :
            self.redact7['font'][1] = 12
        elif Rparameters['redact7']['font_size'] == 'Большой' :
            self.redact7['font'][1] = 14
        else : self.redact7['font'][1] = 10
#   PARAMETR
        if Rparameters['parametr']['geometry'] == 'Маленькое' :
            self.parametr['geometry'] = '550x400'
        elif Rparameters['parametr']['geometry'] == 'Среднее' :
            self.parametr['geometry'] = '600x450'
        else : self.parametr['geometry'] = '650x500'

        if Rparameters['parametr']['bg'] == 'Успокаивающий зеленый' :
            self.parametr['bg'] = 'pale green'
        elif Rparameters['parametr']['bg'] == 'Офисный белый' :
            self.parametr['bg'] = 'gray94'
        elif Rparameters['parametr']['bg'] == 'Спортивный красный' :
            self.parametr['bg'] = 'red'
        else : self.parametr['bg'] = 'gray'

        if Rparameters['parametr']['font_name'] == 'Красивый обычный' :
            self.parametr['font'][0] = 'Comic Sans MS'
        elif Rparameters['parametr']['font_name'] == 'Офисный обычный' :
            self.parametr['font'][0] = 'Times New Roman'
        else : self.parametr['font'][0] = 'Script'

        if Rparameters['parametr']['font_size'] == 'Средний' :
            self.parametr['font'][1] = 12
        elif Rparameters['parametr']['font_size'] == 'Большой' :
            self.parametr['font'][1] = 14
        else : self.parametr['font'][1] = 10

        parameters = {'main' : self.main, 'create' : self.create, 'redact' : self.redact, 'redact7' : self.redact7, 'parametr' : self.parametr}
        self.work_configure(state='write', Rparameters=parameters)

        if reloadapp :
           if messagebox.askquestion('Контакты', '''Были измененены параметры\nглавного окна программы. Для применения\nизменений необходим перезапуск приложения.\nВыйти из программы?''') == 'yes' :
                self.destroy()
                exit(0)
        else :
            messagebox.showinfo('Контакты', 'Изменения успешно применены!')

    def on_closing(self):
        if (messagebox.askquestion("Выход", "Вы действительно хотите выйти?") == "yes") :
            self.destroy()
            exit(0)