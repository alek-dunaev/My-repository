from tkinter import *
from tkinter import messagebox


def calc_bmi():
    kg = weight_tf.get()
    kg = int(kg)
    m = height_tf.get()
    m = int(m)/100
    bmi = kg / (m * m)
    bmi = round(bmi, 1)
    if bmi < 18.5:
        messagebox.showinfo('Результат', f'ИМТ = {bmi} соответствует недостаточному весу')
    elif 18.5 < bmi < 24.9:
        messagebox.showinfo('Результат', f'ИМТ = {bmi} соответствует нормальному весу')
    elif 24.9 < bmi < 29.9:
        messagebox.showinfo('Результат', f'ИМТ = {bmi} соответствует избыточному весу')
    else:
        messagebox.showinfo('Результат', f'ИМТ = {bmi} соответствует ожирению')


"""Создаём окно приложения"""
window = Tk()
window.geometry('400x300')
window.title('Калькудятор индекса массы тела (ИМТ)')

frame = Frame(
    window,  # указываем где размещаем Frame
    padx=10,  # отступ по горизонтали
    pady=10  # отступ по вертикали
)
frame.pack(expand=True)

height_lb = Label(
    frame,
    text="Введите свой рост (в см)"
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Введите свой вес (в кг)"
)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

cal_btn = Button(
    frame,
    text='Рассчитать ИМТ',
    command=calc_bmi
)
cal_btn.grid(row=5, column=2)

window.mainloop()
