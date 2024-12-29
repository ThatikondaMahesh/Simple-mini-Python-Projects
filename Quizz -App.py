# program to quizz application
import tkinter as tk
from tkinter import messagebox
class Quizz:
    def __init__(self):
        self.quiz_data=[
            {
                "question": "What is the capital of Japan?",
                "options": ["Tokyo", "Beijing", "Seoul", "Bangkok"],
                "correct_answer": 0
            },
            {
                "question": "Who wrote the novel 'Pride and Prejudice'?",
                "options": ["Jane Austen", "Emily Bronte", "Charlotte Bronte", "Louisa May Alcott"],
                "correct_answer": 0
            },
            {
                "question": "What is the chemical symbol for the element Gold?",
                "options": [ "Ag", "Au", "Cu", "Fe"],
                "correct_answer": 1
            }
        ]
        self.current_question_index=0
        self.score=0
        self.window=tk.Tk()
        self.window.title("Quiz app")
        
        self.question_label=tk.Label(self.window,text="")  # labelling for the question in the GUI
        self.question_label.pack()
        
        self.options_frame=tk.Frame(self.window)
        self.options_frame.pack()
        
        self.options_buttons=[]
        for i in range(4):
            button=tk.Button(self.options_frame,text="",width=30,command=lambda i=i : self.check_answer(i))
            button.pack(pady=5)
            self.options_buttons.append(button)
        self.next_question_button=tk.Button(self.window,text="Next question",width=30,command=self.next_question)
        self.next_question_button.pack(pady=10)
    def start(self):
        self.load_question()
        self.window.mainloop()
        
    def load_question(self):                                # loading question
        self.question_data=self.quiz_data[self.current_question_index]
        self.question_label.config(text=self.question_data["question"])
        options=self.question_data["options"]
        for i in range(4):
            self.options_buttons[i].config(text=options[i])
            
            
            
    def check_answer(self,selected_option):         # checkin the answer
        question_data=self.quiz_data[self.current_question_index]
        correct_answer_index=question_data["correct_answer"]
        if correct_answer_index==selected_option :
            self.score+=1
            messagebox.showinfo("Correct anwer","your answer is right")
           
        else:
            messagebox.showinfo("Incorrect anwer","your answer is wrong")
            
        
    def next_question(self):                    # move to next question
        self.current_question_index+=1
        if(self.current_question_index==len(self.quiz_data)):
            messagebox.showinfo("Quiz over",f"your score is{self.score}/{len(self.quiz_data)}")
            self.window.quit()
        else:
            self.load_question()
    
quiz_app=Quizz()
quiz_app.start()
        
        