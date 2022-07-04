from tkinter import messagebox
import re
import json
import os.path

#valid of mail by Oleg

class File (): 

    def work_configure (self, state = 'read', Rparameters = None) :
        if state == 'read' :
            if ( not os.path.isfile('parameters.json')) :
                parameters = { 'main' : {'geometry' : '500x700', 'bg' : 'pale green', 'font' : ['Script' , 12] },
                            'create' : {'geometry' : '500x350', 'bg' : 'pale green', 'font' : ['Comic Sans MS' , 12] },
                            'redact' : {'geometry' : '500x350', 'bg' : 'pale green', 'font' : ['Comic Sans MS' , 12] },
                            'redact7' : {'geometry' : '500x350', 'bg' : 'pale green', 'font' : ['Comic Sans MS' , 12] },
                            'parametr' : {'geometry' : '550x400', 'bg' : 'pale green', 'font' : ['Comic Sans MS' , 12] } }
                with open('parameters.json', 'x', encoding='utf-8') as conf : #открываем файл БД для занесения шаблона БД
                    json.dump(parameters, conf, indent=4)
                return None
            else :
                with open('parameters.json', 'r', encoding='utf-8') as conf : #открытие файла БД в режиме чтения
                    Rparametes = json.load(conf)
                    return Rparametes
        if state == 'write' :
            with open('parameters.json', 'r+', encoding='utf-8') as conf :
                conf.truncate(0)
                conf.seek(0)
                json.dump(Rparameters, conf, indent = 4)


    def open_base(self) :
        if ( not os.path.isfile("base.json")) : #проверка на сущетвование БД
            messagebox.showerror("Error!", "В базе данных нет контактов.\nВнесите хотя бы один контакт.") #выводит всплывающее окно
            contacks = []
            with open("base.json", "x", encoding="utf-8") as base : #открываем файл БД для занесения шаблона БД
                json.dump(contacks, base, indent=4)
            return None
        else :
            with open('base.json', "r", encoding="utf-8") as base : #открытие файла БД в режиме чтения
                base_contacks = json.load(base)
                return base_contacks

    def validating_data(self, name1=None, name2=None, number=None, mail=None) :
        validate = list()
        if(name1):
            if( name1.find("Имя") != -1) : validate.append(False)
            else: validate.append(True)
        if(name2):
            if( name2.find("Фамилия") != -1) : validate.append(False)
            else: validate.append(True)
        if(number):
            if( number.isdigit()) : validate.append(True)
            elif (number[0] == '+'):
                number = number.replace("+", "")
                if( number.isdigit()) : validate.append(True)
                else : validate.append(False) #регулярные выражения питон почта
            else : validate.append(False)
        if (mail):
            pattern = '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
            if re.search(pattern, mail):
                validate.append(True)
            else:
                validate.append(False)
        return validate
     
    def write_base (self, contakt ) :
        Rvalidate = self.validating_data(name1=contakt["1Name"], name2=contakt["2Name"], number=contakt["number_phone"], mail = contakt["mail"])
        if(not Rvalidate[0]) :
            messagebox.showerror("Ошибка", "Имя контакта не может\nсодержать слово \"Имя\"") 
            return False
        if(not Rvalidate[1]) :
            messagebox.showerror("Ошибка", "Фамилиия контакта не может содержать\nслово \"Фамилия\"") 
            return False
        if(not Rvalidate[2]) :
            messagebox.showerror("Ошибка", "Номер контакта не может содержать\nслово \"Номер телефона\",\nа так же другие символы кроме\nцифр и +")
            return False
        if(not Rvalidate[3]) :
            messagebox.showerror("Ошибка", "Неправильный вид почтового адреса") 
            return False
        base_contacks = self.open_base()
        find = self.find_contackt(Name1=contakt["1Name"], Name2=contakt["2Name"])
        if (find) :
            messagebox.showerror("Ошибка", "Уже существует контакт\nс такими же Имя Фамилия")
            return False
        base_contacks.append(contakt)
        with open("base.json", "r+", encoding="utf-8") as write_base :
            write_base.truncate(0)
            write_base.seek(0)
            json.dump(base_contacks, write_base, indent = 4)
        messagebox.showinfo("Контакты", "Контакт внесен в\nбазу данных")
        return True

    def redact_base (self, contakt) :
        Rvalidate = self.validating_data(name1=contakt["new"]["1Name"], name2=contakt["new"]["2Name"], number=contakt["new"]["number_phone"], mail = contakt["new"]["mail"])
        if(not Rvalidate[0]) :
            messagebox.showerror("Ошибка", "Имя контакта не может\nсодержать слово \"Имя\"") 
            return False
        if(not Rvalidate[1]) :
            messagebox.showerror("Ошибка", "Фамилиия контакта не может содержать\nслово \"Фамилия\"") 
            return False
        if(not Rvalidate[2]) :
            messagebox.showerror("Ошибка", "Номер контакта не может содержать\nслово \"Номер телефона\",\nа так же другие символы кроме\nцифр и +")
            return False
        if(not Rvalidate[3]) :
            messagebox.showerror("Ошибка", "Неправильный вид почтового адреса") 
            return False
        base_contacks = self.open_base()
        iter = contakt["old"]["number_contackt"]
        if(iter >= 0): succsess = True
        else :
            succsess = self.find_contackt(Name1=contakt["old"]["1Name"], Name2=contakt["old"]["2Name"])
            iter = succsess["number_contackt"]
        if (succsess) :
            base_contacks[iter]["1Name"] = contakt["new"]["1Name"]
            base_contacks[iter]["2Name"] = contakt["new"]["2Name"]
            base_contacks[iter]["number_phone"] = contakt["new"]["number_phone"]
            base_contacks[iter]["mail"] = contakt["new"]["mail"]
            with open("base.json", "r+", encoding="utf-8") as write_base :
                write_base.truncate(0)
                write_base.seek(0)
                json.dump(base_contacks, write_base, indent = 4)
            messagebox.showinfo("Контакты", "Контакт отредактирован")
            return True
        else : 
            messagebox.showwarning("Ошибка!", "Контакт с такими\nИменем и Фамилией не найден!")
            return False

    def find_contackt (self, Name1=None, Name2=None, index=-1 ) :
        base_contacks = self.open_base()
        if(index>=0) :
            contakt = { "1Name" : base_contacks[index]["1Name"],
                "2Name" : base_contacks[index]["2Name"],
                "number_phone" : base_contacks[index]["number_phone"],
                "mail" : base_contacks[index]["mail"],
                "number_contackt" : index }
            return contakt
        for iter in range(len(base_contacks)) :
            if (Name1 == base_contacks[iter]["1Name"] and Name2 == base_contacks[iter]["2Name"]) :
                contakt = { "1Name" : base_contacks[iter]["1Name"],
                "2Name" : base_contacks[iter]["2Name"],
                "number_phone" : base_contacks[iter]["number_phone"],
                "mail" : base_contacks[iter]["mail"],
                "number_contackt" : iter }
                return contakt

    def remove_from_base(self, contackt) :
        base_contacks = self.open_base()
        while contackt :
            number_contackt = contackt["number_contackt"]
            if(number_contackt >= 0) :
                count_contacks = len(base_contacks)
                base_contacks[number_contackt] = base_contacks[count_contacks-1]
                del base_contacks[count_contacks-1]
                with open("base.json", "r+", encoding="utf-8") as write_base :
                    write_base.truncate(0)
                    write_base.seek(0)
                    json.dump(base_contacks, write_base, indent = 4)
                return True
            else :
                return False
        
if (__name__ == "__main__ ") :
    file = File()
    #file.write_base(contakt={"fio" : "", "number_phone" : ""})
    print(file.open_base())
    file.redact_base(contakt={
    "old" : {
        "1Name": "kadnvqr;nv",
        "2Name" : "iwkxl",
        "number_phone": "\u041d\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430",
        "mail" : "",
        "number_contackt" : 1
    },
    "new" : {
        "1Name": "Имя",
        "2Name" : "Фамилия",
        "number_phone": "+79215978523",
        "mail" : "-"
    }
    })
    print(file.open_base())

if (__name__ == "__main__") :
    file = File()
    file.find_contackt(Name1="Nikita", Name2="Yarovoi")