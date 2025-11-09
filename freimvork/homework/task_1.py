import tkinter as tk
import json
import os

def clickButton():
    if not os.path.exists("result.txt"):
        file = open("result.txt", "w", encoding="utf-8")
        file.write("")
        file.close()

    file = open("result.txt", "r", encoding="utf-8")
    content = file.read()
    file.close()

    if content.strip() == "":
        data_users = dict()
    else:
        data_users = json.loads(content)

    user = userName.get()
    change_1 = radio_value.get()
    change_2 = radio_value2.get()
    change_3 = radio_value3.get() 
    
    data_questionnaire = dict()
    data_questionnaire[question1.cget("text")] = []
    if change_1 == 1:
        data_questionnaire[question1.cget("text")].append("Комедия")
    elif change_1 == 2:
         data_questionnaire[question1.cget("text")].append("Драма")
    elif change_1 == 3:
         data_questionnaire[question1.cget("text")].append("Боевик")
    elif change_1 == 4:
         data_questionnaire[question1.cget("text")].append("Фантастика")
    elif change_1 == 5:
         data_questionnaire[question1.cget("text")].append("Романтка")

    data_questionnaire[question2.cget("text")] = []
    if change_2 == 1:
        data_questionnaire[question2.cget("text")].append("В кинотеатре")
    elif change_2 == 2:
        data_questionnaire[question2.cget("text")].append("Онлайн дома")
    elif change_2 == 3:
        data_questionnaire[question2.cget("text")].append("На телевизоре с флешки/DVD")
    elif change_2 == 4:
        data_questionnaire[question2.cget("text")].append("На телефоне")

    data_questionnaire[question3.cget("text")] = []
    if change_3 == 1:
        data_questionnaire[question3.cget("text")].append("Сюжет и смысл")
    elif change_3 == 2:
         data_questionnaire[question3.cget("text")].append("Актерская игра")
    elif change_3 == 3:
         data_questionnaire[question3.cget("text")].append("Визуальные эффекты и картинка")
    elif change_3 == 4:
         data_questionnaire[question3.cget("text")].append("Музыкальное сопровождение")
          

    if user not in data_users:
        data_users[user] = []

    data_users[user].append(data_questionnaire)

    file = open("result.txt",  "w", encoding="utf-8")
    json.dump(data_users, file, ensure_ascii=False, indent=4)
    file.close()

baseWindow = tk.Tk()
baseWindow.title("Questionnaire")
baseWindow.geometry("1200x1200")

heading = tk.Label(baseWindow,
                   text="Анкета",
                   fg = "blue",
                   font="Arial 18")
heading.pack()

name = tk.Label(baseWindow,
                text="Введите свое имя",
                fg="#1a5276",
                font="Arial 16")
name.pack()

userName = tk.Entry(baseWindow,
                    width=50)
userName.pack()

frame1 = tk.LabelFrame(baseWindow, 
                       text="Вопрос 1",
                       fg="#1a5276",
                       font="Arial 14",
                       pady=10)
frame1.pack(fill="x", padx=300, pady=10)

radio_value = tk.IntVar()
question1 = tk.Label(frame1,
                     text="Какой жанр фильмов вы предпочитаете?",
                     fg="blue",
                     font="Arial 16")
question1.pack()
radio1 = tk.Radiobutton(frame1, 
                        text="Комедия",
                        font="Arial 14",
                        value=1,
                        variable=radio_value)
radio1.pack()
radio2 = tk.Radiobutton(frame1, 
                        text="Драма",
                        font="Arial 14",
                        value=2,
                        variable=radio_value)
radio2.pack()
radio3 = tk.Radiobutton(frame1, 
                        text="Боевик",
                        font="Arial 14", 
                        value=3,
                        variable=radio_value)
radio3.pack()
radio4 = tk.Radiobutton(frame1, 
                        text="Фантастика",
                        font="Arial 14", 
                        value=4,
                        variable=radio_value)
radio4.pack()
radio5 = tk.Radiobutton(frame1, 
                        text="Романтика",
                        font="Arial 14", 
                        value=5,
                        variable=radio_value)
radio5.pack()

frame2 = tk.LabelFrame(baseWindow, 
                       text="Вопрос 2",
                       fg="#1a5276",
                       font="Arial 14",
                       pady=10)
frame2.pack(fill="x", padx=300, pady=10)

radio_value2 = tk.IntVar()
question2 = tk.Label(frame2, 
                     text="Kак вы чаще всего смотрите фильмы?",
                     fg="blue",
                     font="Arial 16")
question2.pack()
radio_1 = tk.Radiobutton(frame2,
                         text="В кинотеатре",
                         font="Arial 14",
                         value=1,
                         variable=radio_value2)
radio_1.pack()
radio_2 = tk.Radiobutton(frame2,
                         text="Онлайн дома",
                         font="Arial 14",
                         value=2,
                         variable=radio_value2)
radio_2.pack()
radio_3 = tk.Radiobutton(frame2,
                         text="На телевизоре с флешки/DVD",
                         font="Arial 14",
                         value=3,
                         variable=radio_value2)
radio_3.pack()
radio_4 = tk.Radiobutton(frame2,
                         text="На телефоне",
                         font="Arial 14",
                         value=4,
                         variable=radio_value2)
radio_4.pack()


frame3 = tk.LabelFrame(baseWindow, 
                       text="Вопрос 3",
                       fg="#1a5276",
                       font="Arial 14",
                       pady=10)
frame3.pack(fill="x", padx=300, pady=10)

radio_value3 = tk.IntVar()
question3 = tk.Label(frame3,
                     text="Что для вас самое важное в фильме?",
                     fg="blue",
                     font="Arial 16")
question3.pack()
rd1 = tk.Radiobutton(frame3,
                      text="Сюжет и смысл",
                      value=1,
                      font="Arial 14",
                      variable=radio_value3)
rd1.pack()
rd2 = tk.Radiobutton(frame3,
                      text="Актёрская игра",
                      value=2,
                      font="Arial 14",
                      variable=radio_value3)
rd2.pack()
rd3 = tk.Radiobutton(frame3,
                      text="Визуальные эффекты и картинка",
                      value=3,
                      font="Arial 14",
                      variable=radio_value3)
rd3.pack()
rd4 = tk.Radiobutton(frame3,
                      text="Музыкальное сопровождение",
                      value=4,
                      font="Arial 14",
                      variable=radio_value3)
rd4.pack()

click = tk.Button(baseWindow,
                  text = "Отправить",
                  fg="red",
                  font = "Arial 18",
                  command=clickButton)
click.pack()
baseWindow.mainloop()
