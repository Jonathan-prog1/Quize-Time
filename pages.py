import tkinter as tk
from tkinter import ttk
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
        label = tk.Label(self, text="Quiz Catagory", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        
        
        
        list = tk.Listbox(self, bg=PAPER,font=LARGE_FONT, width=30, justify='center')
        list.pack()
        list.insert(tk.END,"Math")
        list.insert(tk.END, "Time")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        button1 = ttk.Button(self, text="Start Quiz now", 
                            command=lambda: controller.show_frame(Quiz_start))
        button1.pack()
        
        button2 = ttk.Button(self, text="Back to Main Menu", 
                            command=lambda: controller.show_frame(MainMenu))
        button2.pack()

      

