from itertools import product
from random import randint
import re
from tkinter import *
from tkinter import ttk


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
def close(error):
    error.grab_release()
    error.destroy()
def da():
    ex = Tk()
    ud = Toplevel()
    ud.attributes("-topmost", True)
    ex.resizable(False, False)
    ud.resizable(False, False)
    ex.geometry(f'500x500+{wh}+{hh}')
    ud.geometry(f'300x100+{wh+100}+{hh+200}')
    canvas = Canvas(ud, bg="#CDB5CD", width=300, height=100)
    canvas.pack(anchor=CENTER, expand=1)
    canvas.create_line(0, 300, 400, 0, fill="#8B7B8B", width=200, smooth=TRUE)
    canvas.create_text(150, 35, text="Вы успешно прошли\nавторизацию/регистрацию", font="Courier 10", fill="#282828")
    ud.grab_set()
    btn = Button(ud, text="Закрыть", command=lambda: close(ud), bg="#CDB5CD", fg="#282828",
                 activebackground="#8B7B8B")
    canvas.create_window(60, 60, anchor=NW, window=btn, width=180, height=30)
def check():
    if (len(log.get()) and len(pas.get())) == 0 or (len(log.get()) or len(pas.get())) == 0:
        error = Toplevel()
        error.attributes("-topmost", True)
        error.resizable(False, False)
        error.title("ВНИМАНИЕ")
        error.geometry(f'300x100+{wh+50}+{hh+100}')
        canvas = Canvas(error, bg="#CDB5CD", width=400, height=300)
        canvas.pack(anchor=CENTER, expand=1)
        canvas.create_line(0, 300, 400, 0, fill="#8B7B8B", width=200, smooth=TRUE)
        canvas.create_text(155,35, text="НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ", font="Courier 15", fill="#282828")
        btn = Button(error, text="Закрыть", command = lambda: close(error), bg="#CDB5CD", fg="#282828",
                     activebackground="#8B7B8B")
        canvas.create_window(60, 60, anchor=NW, window=btn, width=180, height=30)
        error.grab_set()
    else:
        root.destroy()
        da()
def reg():
    canvas.create_text(200,85,text="Авторизация/Регистрация",font="Courier 18",fill="#282828")
    canvas.create_text(130,135,text="Логин:",font="Courier 20",fill="#282828")
    log_ent = Entry(font="Courier 15",textvariable=log,bg ="#CDB5CD",fg="#282828")
    canvas.create_window(180, 127, anchor=NW, window=log_ent, width=125, height=20)
    canvas.create_text(123, 175, text="Пароль:", font="Courier 20",fill="#282828")
    par_ent = Entry(font="Courier 15",textvariable=pas,bg ="#CDB5CD",show="*")
    canvas.create_window(180, 166, anchor=NW, window=par_ent, width=125, height=20)
    btn = Button(root,text="Авторизация/Регистрация",command=check,bg ="#CDB5CD",fg="#282828",activebackground="#8B7B8B")
    canvas.create_window(110, 210, anchor=NW, window=btn, width=180, height=30)
reg()
mainloop()