import tkinter as tk
from tkinter import messagebox
from time import time


class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.start_time = None
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Typing Speed Test")
        self.root.geometry('400x300')  # Set the window size
        self.root.configure(bg='light blue')  # Set the background color

        # Create the input field
        self.input_field = tk.Entry(self.root, highlightbackground="light blue")
        self.input_field.pack()

        # Create the Start, Stop, and Reset buttons
        start_button = tk.Button(self.root, text="Start", highlightbackground="light blue", command=self.start_test)
        start_button.pack()

        stop_button = tk.Button(self.root, text="Stop", highlightbackground="light blue", command=self.stop_test)
        stop_button.pack()

        reset_button = tk.Button(self.root, text="Reset", highlightbackground="light blue", command=self.reset_test)
        reset_button.pack()

        # Create the result label
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def start_test(self):
        self.start_time = time()
        self.input_field.delete(0, tk.END)
        self.input_field.focus()

    def stop_test(self):
        if self.start_time:
            text = self.input_field.get()
            words = len(text.split())
            end_time = time()
            time_taken = max(end_time - self.start_time, 1)  # Avoid division by zero
            speed = round(words / time_taken * 60, 2)  # Words per minute
            messagebox.showinfo("Typing Speed", f"Your typing speed is {speed} words per minute")
            self.start_time = None

    def reset_test(self):
        self.start_time = None
        self.input_field.delete(0, tk.END)
        self.result_label.config(text="")
        self.input_field.focus()


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()


