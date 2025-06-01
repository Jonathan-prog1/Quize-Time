import tkinter as tk
from tkinter import messagebox, simpledialog, ttk 
import json
from constants import LARGE_FONT,PAPER

class MainMenu(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        

        
        
        label1 = tk.Label(self, text="Welcome to Quize Time a good place to practce for a test", font=LARGE_FONT, relief="raised",bd=10,fg='white',bg='black', padx=20, pady=20)
        label1.pack(pady=10, padx=10)
        

        button1 = ttk.Button(self, text="Start Quize", 
                            command=lambda: controller.show_frame(Quiz_start))
        button1.pack()

        button2 = ttk.Button(self, text="All Questions", 
                            command=lambda: controller.show_frame(Questions))
        button2.pack()
        
        close_button = ttk.Button(self, text="Close", command=parent.quit)
        close_button.pack(side="bottom", pady=10)


class Quiz_start(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

       

        button2 = ttk.Button(self, text="Back to Main Menu", 
                            command=lambda: controller.show_frame(MainMenu))
        button2.pack()

        close_button = ttk.Button(self, text="Close", command=parent.quit)
        close_button.pack(side="bottom", pady=10)

        


class Questions(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Quiz Catagory", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        
        
        
        self.list = tk.Listbox(self, bg=PAPER,font=LARGE_FONT, width=30, justify='center')
        self.list.pack()
        self.list.insert(tk.END,"Math")
        self.list.insert(tk.END, "Time")

        submit_bt = tk.Button(self, text="Add Catagory", font=LARGE_FONT, command=self.new_catagory)
        submit_bt.pack()

        delete_bt = tk.Button(self, text="Delet Catagory", font=LARGE_FONT, command=self.deleted)
        delete_bt.pack()
        
        button1 = ttk.Button(self, text="Start Quiz now", 
                            command=lambda: controller.show_frame(Quiz_start))
        button1.pack()
        
        button2 = ttk.Button(self, text="Back to Main Menu", 
                            command=lambda: controller.show_frame(MainMenu))
        button2.pack()
   
   
    def new_catagory(self):
            self.controller.show_frame(Add_Questions)

        
    def deleted(self):
        item = self.list.get(self.list.curselection())
        if messagebox.askyesno(title="WARNING!", message=f"Are you sure you want to delete your Catagory about: {item}"):

            self.list.delete(self.list.curselection())

class Add_Questions(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.center_frame = tk.Frame(self)
        self.center_frame.pack(expand=True)

        self.questions = []


        # Category Entry
        # Create a frame to hold all widgets and center it
        self.center_frame = tk.Frame(self)
        self.center_frame.pack(expand=True)

        # Category Entry
        self.category_label = tk.Label(self.center_frame, text="Category Name:", font=LARGE_FONT)
        self.category_label.grid(row=0, column=0, columnspan=2, pady=10)
        self.category_entry = tk.Entry(self.center_frame, font=LARGE_FONT)
        self.category_entry.grid(row=1, column=0, columnspan=2, pady=5)

        # Question Entry
        self.question_label = tk.Label(self.center_frame, text="Enter Question:", font=LARGE_FONT)
        self.question_label.grid(row=2, column=0, columnspan=2, pady=10)
        self.question_entry = tk.Entry(self.center_frame, font=LARGE_FONT)
        self.question_entry.grid(row=3, column=0, columnspan=2, pady=5)

        # Answer Entries and Checkbuttons
        self.answers_frame = tk.Frame(self.center_frame)
        self.answers_frame.grid(row=4, column=0, columnspan=2, pady=10)

        self.answer_entries = []
        self.answer_vars = []
        self.answer_checkbuttons = []

        for i in range(4):
            answer_entry = tk.Entry(self.answers_frame, font=LARGE_FONT)
            answer_entry.grid(row=i, column=0, pady=5)
            self.answer_entries.append(answer_entry)

            answer_var = tk.BooleanVar()
            answer_check = tk.Checkbutton(self.answers_frame, text="Correct", variable=answer_var)
            answer_check.grid(row=i, column=1, padx=10)
            self.answer_vars.append(answer_var)
            self.answer_checkbuttons.append(answer_check)

        # Add Question Button
        self.add_question_button = ttk.Button(self.center_frame, text="Add Question", command=self.add_question)
        self.add_question_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Save Questions Button
        self.save_button = ttk.Button(self.center_frame, text="Save Questions", command=self.save_questions)
        self.save_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Back to Main Menu Button
        back_button = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(side="bottom")

        # Close Button
        close_button = ttk.Button(self, text="Close", command=parent.quit)
        close_button.pack(side="bottom")

    def add_question(self):
        category = self.category_entry.get().strip()
        if not category:
            messagebox.showwarning("Input Error", "Please enter a category name.")
            return

        question_text = self.question_entry.get().strip()
        if not question_text:
            messagebox.showwarning("Input Error", "Please enter a question.")
            return

        answers = []
        correct_answer = None
        for i, entry in enumerate(self.answer_entries):
            answer_text = entry.get().strip()
            if answer_text:
                is_correct = self.answer_vars[i].get()
                answers.append(answer_text)
                if is_correct:
                    if correct_answer is not None:
                        messagebox.showwarning("Input Error", "Only one correct answer can be selected.")
                        return
                    correct_answer = len(answers) - 1

        if len(answers) < 2:
            messagebox.showwarning("Input Error", "Please provide at least two answers.")
            return

        if correct_answer is None:
            messagebox.showwarning("Input Error", "Please select the correct answer.")
            return

        question = {
            "question": question_text,
            "answers": answers,
            "correct_answer": correct_answer
        }
        self.questions.append({"category": category, "question": question})

        # Clear Entries for Next Question
        self.question_entry.delete(0, tk.END)
        for entry in self.answer_entries:
            entry.delete(0, tk.END)
        for var in self.answer_vars:
            var.set(False)

        messagebox.showinfo("Question Added", "Question added successfully!")

    def save_questions(self):
        if not self.questions:
            messagebox.showwarning("No Questions", "No questions to save.")
            return

        filename = f"{self.questions[0]['category']}.json"
        data = {"questions": [q["question"] for q in self.questions]}

        try:
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            messagebox.showinfo("Questions Saved", f"Questions saved to '{filename}' successfully!")
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save questions: {e}")
        
    
        
        
        
        '''
        label = tk.Label(self, text="What do you want the Catogory to be for theys Questions?", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.textbox = tk.Entry(self, font=LARGE_FONT)
        self.textbox.pack()
       
        label = tk.Label(self, text="what is the Question you want to add to this Catagory", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.textbox = tk.Entry(self, font=LARGE_FONT)
        self.textbox.pack()
        
        
        close_button = ttk.Button(self, text="Close", command=parent.quit)
        close_button.pack(side="bottom")

        button2 = ttk.Button(self, text="Back to Main Menu", 
                            command=lambda: controller.show_frame(MainMenu))
        button2.pack(side="bottom")

        add_bt = tk.Button(self, text="Add Question", font=LARGE_FONT, command=self.add)
        add_bt.pack(side="bottom")

        

        
        
    def add(self):
        category = simpledialog.askstring("Category", "Enter the category name:")
        if category:
            # Ensure the category name is valid for a file name
            valid_category = "".join(c if c.isalnum() else"_" for c in  category)
            filename = f"{valid_category}.json"

            # Write the data to the JSON file
            with open(filename, "w") as file:
                json.dump(qa_data, file, indent=4)
            print(f"Category: {category}")
            #self.textbox.delete(0, tk.END) # Clear the Entry widget
            
            
            
            
            #category = simpledialog.askstring("Category", "Enter the category name:")
        #if category:
            #print(f"Category: {category}")
        '''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


      

