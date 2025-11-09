import tkinter as tk
import json
current_question = 0    
count_c = 0
count_un = 0

file = open("test.txt", "r", encoding="utf-8")
data = json.load(file)
file.close()

def show_question():
    q = data["questions"][current_question]
    question.config(text=q["question"])
    for i,option in enumerate(q["answers"]):
        radio_buttoms[i].config(text=f"{i+1}.{q['answers'][option]}")
    answer.set(None)
    check.config(text="")

def check_question():
    global current_question
    global count_c
    global count_un
    q = data["questions"]
    correct = data["questions"][current_question]["correct"]
    choice = answer.get()

    if choice == correct:
        check.config(text="Правильно!",
                     fg="green")
        count_c += 1
        correct_q.config(text=f"Правильно:{count_c}")
    else:
        check.config(text="Не правильно!",
                    fg="red")
        count_un += 1
        uncorrect_q.config(text=f"Правильно:{count_un}")

    if current_question < len(q)-1:
        baseWindow.after(1000,next_question)
    else:
        baseWindow.after(1000,end_test)

def next_question():
    global current_question
    current_question += 1
    show_question()

def end_test():
    global count_c, count_un

    total = count_c + count_un
    percent = round((count_c / total) * 100, 1)

    question.config(
        text=f"Тест завершён!\n"
             f"Количество правильных: {count_c}\n"
             f"Количество неправильных: {count_un}\n"
             f"Процент выполнения: {percent}%"
    )

    if 0<= count_c <= 3:
        end_s.config(text="Оценка:2",
                     fg="red")
    elif 4<=count_c<=5:
        end_s.config(text="Оценка:3",
                     fg="orange")
    elif 6<=count_c<=7:
        end_s.config(text="Оценка:4",
                     fg="green")
    else:
        end_s.config(text="Оценка:5",
                     fg="green")
        
    for rb in radio_buttoms:
        rb.pack_forget()
    click.pack_forget()
    check.pack_forget()
    score_frame.pack_forget()



baseWindow = tk.Tk()
baseWindow.title("Тестирование")
baseWindow.geometry("1200x400")

score_frame = tk.Frame(baseWindow)
score_frame.pack(pady=5)

correct_q = tk.Label(score_frame,
                     text="Правильно: 0",
                     fg="green",
                     font="Arial 10")
correct_q.pack(side="left", padx=10)

uncorrect_q = tk.Label(score_frame,
                       text="Неправильно: 0",
                       fg="red",
                       font="Arial 10")
uncorrect_q.pack(side="left", padx=10)

question = tk.Label(baseWindow,
                    text="",
                    font="Arial 18")
question.pack()


answer = tk.IntVar()
radio_buttoms =[]
for i in range(4):
    rb=tk.Radiobutton(baseWindow,
                      text="",
                      variable=answer,
                      value=i,
                      font="Arial 14")
    rb.pack()
    radio_buttoms.append(rb)

click = tk.Button(baseWindow,
                 text="Ответить",
                 command=check_question,
                 font="Arial 14")
click.pack()

check = tk.Label(baseWindow,
                 text="")
check.pack()

end_s = tk.Label(baseWindow,
                 text="",
                 font="Arial 16")
end_s.pack()

show_question()
baseWindow.mainloop()