import tkinter as tk
from tkinter import messagebox, simpledialog, ttk 
import json
import os
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
        self.directory = os.path.abspath('.')  # Set the directory to the current working directory
        


        label = tk.Label(self, text="Quiz Category", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.list = tk.Listbox(self, bg=PAPER, font=LARGE_FONT, width=30, justify='center')
        self.list.pack()
        self.populate_listbox()  # Populate the listbox with files from the 'questions' subdirectory

        submit_bt = tk.Button(self, text="Add Category", font=LARGE_FONT, command=self.new_category)
        submit_bt.pack()

        delete_bt = tk.Button(self, text="Delete Category", font=LARGE_FONT, command=self.deleted)
        delete_bt.pack()

        button1 = ttk.Button(self, text="Start Quiz now", command=lambda: controller.show_frame(Quiz_start))
        button1.pack()

        button2 = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(MainMenu))
        button2.pack()


    def populate_listbox(self):
        try:
            subdirectory = 'questions'
            subdirectory_path = os.path.join(self.directory, subdirectory)

            # List all files in the specified subdirectory, excluding hidden files
            visible_files = [f for f in os.listdir(subdirectory_path) if not f.startswith('.')]
            
            for file in visible_files:
                # Remove file extension
                filename_without_extension = os.path.splitext(file)[0]
                self.list.insert(tk.END, filename_without_extension)
        except FileNotFoundError:
            messagebox.showerror("Directory Not Found", f"The directory '{self.directory}' does not exist.")
        except PermissionError:
            messagebox.showerror("Permission Denied", f"Permission denied to access '{self.directory}'.")
        except FileNotFoundError:
            messagebox.showerror("Subdirectory Not Found", f"The subdirectory '{subdirectory}' does not exist.")

    def new_category(self):
        self.controller.show_frame(Add_Questions)

    def deleted(self):
        try:
            # Get the selected item from the listbox
            selected_item = self.list.get(self.list.curselection())
            # Construct the full file path
            file_path = os.path.join(self.directory, 'questions', selected_item + '.json')
            
            if messagebox.askyesno(title="Confirm Deletion", message=f"Are you sure you want to delete your Category about: {selected_item}"):
                # Check if the file exists
                if os.path.exists(file_path):
                    # Delete the file
                    os.remove(file_path)
                # Remove the item from the listbox
                self.list.delete(self.list.curselection())
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


       

class Add_Questions(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.center_frame = tk.Frame(self)
        self.center_frame.pack(expand=True)

        self.questions = []

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
        self.category_entry.config(state="disabled")
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

        # Define the directory where you want to save the files
        save_directory = "questions"

        # Create the directory if it doesn't exist
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        # Use the category of the first question to name the file
        category = self.questions[0]['category']
        filename = f"{category}.json"
        file_path = os.path.join(save_directory, filename)

        # Prepare the data to be saved
        data = {"questions": [q["question"] for q in self.questions]}

        try:
            # Open the file in write mode and save the data
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)
            messagebox.showinfo("Questions Saved", f"All Questions have been saved for the category: {category}")
            self.controller.show_frame(Questions)
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save questions: {e}")
        

        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


      

