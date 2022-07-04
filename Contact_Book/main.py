from gui_app import *

app = App()
app.title("Контакты") #редактирование заголовка программы
app.protocol("WM_DELETE_WINDOW", app.on_closing )
app.mainloop()