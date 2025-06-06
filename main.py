import tkinter as tk
from pages import MainMenu, Quiz_start, Questions,Add_Questions



class QuizApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Quize Time")

        container = tk.Frame(self)
        container.pack(side="top", fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainMenu, Quiz_start, Questions,Add_Questions):


            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(MainMenu)
        
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


app = QuizApp()
app.mainloop()