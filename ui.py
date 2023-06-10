import tkinter
from tkinter import messagebox
from quiz_brain import QuizBrain 
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz:QuizBrain):
        self.quiz = quiz
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20, pady=20)


        true = tkinter.PhotoImage(file="images/true.png")
        false = tkinter.PhotoImage(file="images/false.png")
        self.true_button = tkinter.Button(image=true, highlightthickness=0, command=self.true_pressed)
        self.false_button = tkinter.Button(image=false, highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)
        
        self.score_label = tkinter.Label(text=f"Score:{self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)


        self.canvas = tkinter.Canvas(width=300, height=250,highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=230, text="", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.config(background="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.get_next()

        self.window.mainloop()
        
    def get_next(self):
        
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():     
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            messagebox.showinfo(title = "Game Over", 
                                message=f"You've completed the quiz.\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            
    
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
            
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next)
        
    