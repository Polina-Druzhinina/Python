import tkinter as tk

def clickButton():
    x = entry1.get()
    y = entry2.get()
    print(x, y, type(x))
    z = int(x) + int(y)
    label3.config(text = str(z))

baseWindow = tk.Tk() #можно любле название до точки, контейнер(родительский элемент)
baseWindow.title("My programm")
baseWindow.geometry("1000x600")

#создаем и добавляем элементы интерфейса
label1 = tk.Label(baseWindow, text="Введите первое слагаемое",
                  fg = "#FF5561",
                  font="Arial 14")
label1.pack() #упаковщик pack, по умолчанию по центру
entry1 = tk.Entry(baseWindow,
                  fg = "#FF5561",
                  bg = "white",
                  font="Arial 18",
                  borderwidth="3",
                  width="40") #сколько символов
entry1.pack()

label2 = tk.Label(baseWindow, text="Введите второе слагаемое",
                  fg = "#FF5561",
                  font="Arial 14")
label2.pack() #упаковщик pack, по умолчанию по центру
entry2 = tk.Entry(baseWindow,
                  fg = "#FF5561",
                  bg = "white",
                  font="Arial 18",
                  borderwidth="3",
                  width="40") #сколько символов
entry2.pack()

click = tk.Button(baseWindow,
                  text="Сложить",
                  fg = "#FF5561",
                  font="Arial 18",
                  command=clickButton)
click.pack()

label3 = tk.Label(baseWindow, 
                  text="Результат:",
                  fg = "#FF5561",
                  font="Arial 14")
label3.pack()
baseWindow.mainloop()

