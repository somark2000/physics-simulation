# imports
import tkinter as tk

class CourseWindow():
    def run(self):
        # setup for the UI window
        window = tk.Tk()
        window.title("Courses")
        window.geometry('800x500')
        bg = tk.PhotoImage(file="images/bg.png")
        bg_label = tk.Label(window, image=bg)
        welcome_label = tk.Label(window, text="Courses")
        welcome_label.configure(bg='#0e1c1d', font=("Arial", 28), fg='white')

        bg_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        welcome_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

        window.mainloop()