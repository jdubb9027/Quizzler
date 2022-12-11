from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.score = self.quiz.score
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Text",
            fill=THEME_COLOR,
            font=FONT,
            width=290
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_img, command=self.answer_is_true, bg=THEME_COLOR, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_img, bg=THEME_COLOR, command=self.answer_is_false, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def choose_category(self):

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You Completed the Quiz! Your Total Score is: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_is_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def answer_is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
