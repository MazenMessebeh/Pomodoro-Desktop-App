from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_clicked():
    window.after_cancel(timer)
    timer_title.config(text= "Timer")
    canvas.itemconfig(timer_text, text= "00:00")
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_clicked():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_title.config(text="Break", fg=YELLOW)
    else:
        countdown(work_sec)
        timer_title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min} : {count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_clicked()
        mark = ""
        for i in range(math.floor(reps / 2)):
            mark += "✔"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomadora")
window.minsize(width=600, height=500)
window.config(padx=100, pady=50, bg=PINK)

canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato)
timer_text = canvas.create_text(103, 140, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=2, column=2)

timer_title = Label(text="Timer", font=(FONT_NAME, 36, "bold"), fg=GREEN, bg=PINK)
timer_title.grid(row=1, column=2)

start = Button(text="Start", command=start_clicked)
start.grid(row=3, column=1)

reset = Button(text="Reset", command= reset_clicked)
reset.grid(row=3, column=3)

check = Label(text="", font=(FONT_NAME, 16, "bold"), bg=PINK, fg=GREEN)
check.grid(row=4, column=2)

window.mainloop()
