from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_text = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_text.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.q_text = self.canvas.create_text(150, 125,
                                              width=280,
                                              text=f"Some Text",
                                              fill=THEME_COLOR,
                                              font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30, padx=4)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=self.true_img, highlightthickness=0, highlightbackground=THEME_COLOR)
        self.true_btn.grid(column=0, row=2)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=self.false_img, highlightthickness=0, highlightbackground=THEME_COLOR)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.q_text, text=q_text)

