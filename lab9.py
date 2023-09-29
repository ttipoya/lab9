from tkinter import *
import tkinter as tk
from tkinter import messagebox

root = Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
wh = w//2
hh = h//2
wh = wh - 200
hh = hh - 200
root.title("Окно авторизации/регистрации")
root.geometry(f'400x300+{wh}+{hh}')
root.resizable(False, False)


canvas = Canvas(bg="#CDB5CD", width=400, height=300)
canvas.pack(anchor=CENTER, expand=1)

canvas.create_line(0, 300, 400, 0, fill="#8B7B8B",width = 200,smooth = TRUE)
canvas.create_rectangle(25, 278, 375, 22, fill="#CDB5CD",outline="#8B7B8B")

log = StringVar()
pas = StringVar()
enabled = IntVar()
def paf(par_ent):
    if enabled.get() == 1:
        par_ent['show'] = NONE
    if enabled.get() == 0:
        par_ent['show'] = '*'
class CreateToolTip(object):
    def __init__(self, widget, text='widget info'):
        self.waittime = 500
        self.wraplength = 180
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None
    def enter(self, event=None):
        self.schedule()
    def leave(self, event=None):
        self.unschedule()
        self.hidetip()
    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)
    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)
    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 30
        y += self.widget.winfo_rooty() + 25
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)
    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()
def da():
    ex = Tk()
    ex.resizable(False, False)
    ex.geometry(f'500x500+{wh}+{hh}')
    messagebox.showinfo("Всё верно", 'Успешная регистрация/авторизация')
def check():
    if (len(log.get()) and len(pas.get())) == 0 or ((len(log.get()) or len(pas.get())) == 0) or (len(pas.get())> 20 or len(pas.get())<8) or log.get().count(' ')> 0 or pas.get().count(' ')> 0:
        messagebox.showerror("Ошибка",'Некорректные данные')
    else:
        root.destroy()
        da()
def reg():
    canvas.create_text(200,85,text="Авторизация/Регистрация",font="Courier 18",fill="#282828")
    canvas.create_text(130,135,text="Логин:",font="Courier 20",fill="#282828")
    log_ent = Entry(font="Courier 15",textvariable=log,bg ="#CDB5CD",fg="#282828")
    canvas.create_window(180, 127, anchor=NW, window=log_ent, width=125, height=20)
    canvas.create_text(123, 175, text="Пароль:", font="Courier 20",fill="#282828")
    par_ent = Entry(root,font="Courier 15",textvariable=pas,bg ="#CDB5CD",show="*")
    canvas.create_window(180, 166, anchor=NW, window=par_ent, width=125, height=20)
    button1_ttp = CreateToolTip(par_ent, 'Введите количество символов от 8 до 20 без пробела')
    enabled_checkbutton = Checkbutton(text="",bg ="#CDB5CD" ,activebackground="#CDB5CD", variable= enabled, command= lambda :paf(par_ent))
    canvas.create_window(310, 166, anchor=NW, window=enabled_checkbutton, width=20, height=20)
    btn = Button(root,text="Авторизация/Регистрация",command=check,bg ="#CDB5CD",fg="#282828",activebackground="#8B7B8B")
    canvas.create_window(110, 210, anchor=NW, window=btn, width=180, height=30)
reg()
mainloop()
