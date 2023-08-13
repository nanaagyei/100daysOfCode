from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# --------------------- UI SETUP ---------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=flash_card_front)
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_btn = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_btn, highlightthickness=0, highlightbackground="white")
wrong_button.grid(column=0, row=1)

correct_btn = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_btn, highlightthickness=0, highlightbackground="white")
correct_button.grid(column=1, row=1)



window.mainloop()
