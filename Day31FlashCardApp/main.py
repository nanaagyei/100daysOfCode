from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
# --------------------- DATA READING AND PROCESSING ---------------------- #
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
data_dict_list = data.to_dict(orient="records")
current_word = {}

# --------------------- PICKING WORDS ---------------------- #


def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(data_dict_list)
    french_word = current_word["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(canvas_image, image=flash_card_front)
    flip_timer = window.after(3000, func=flip_card)


def learned_card():
    data_dict_list.remove(current_word)
    next_card()
    to_learn_df = pd.DataFrame(data_dict_list)
    to_learn_df.to_csv("data/words_to_learn.csv", index=False)


def flip_card():
    english_word = current_word["English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")
    canvas.itemconfig(canvas_image, image=flash_card_back)


# --------------------- UI SETUP ---------------------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_front = PhotoImage(file="./images/card_front.png")
flash_card_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=flash_card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_btn = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_btn, highlightthickness=0, highlightbackground="white", command=next_card)
wrong_button.grid(column=0, row=1)

correct_btn = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_btn, highlightthickness=0, highlightbackground="white", command=learned_card)
correct_button.grid(column=1, row=1)

next_card()


window.mainloop()
