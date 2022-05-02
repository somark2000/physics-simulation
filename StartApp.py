import tkinter as tk
from tkinter import messagebox
from practice_window import PracticeWindow
from course_window import CourseWindow

class StartApp:
    def do_practice(self, window):
        practice = PracticeWindow()
        window.destroy()
        practice.run()

    def do_courses(self, window):
        course = CourseWindow()
        window.destroy()
        course.run()

    def help(self):
        messagebox.showinfo(title="Info", message="Dear User!\n ")

    def run(self):
        window = tk.Tk()
        window.title("Home")
        window.geometry('800x500')
        bg = tk.PhotoImage(file="images/bg.png")
        bg_label = tk.Label(window, image=bg)
        welcome_label = tk.Label(window, text="Welcome!")
        welcome_label.configure(bg='#0e1c1d', font=("Arial", 35), fg='white')
        stud_butt = tk.Button(text='Courses', command=lambda: self.do_courses(window))
        stud_butt.configure(bg='#0e1c1d', font=("Arial", 20), fg='white', border=0)
        play_butt = tk.Button(text='Practice', command=lambda: self.do_practice(window))
        play_butt.configure(bg='#0e1c1d', font=("Arial", 20), fg='white', border=0)
        inf = tk.PhotoImage(file="images/infow.png")
        info_butt = tk.Button(image=inf, bg='#0e1c1d', border=0, command=lambda: self.help())

        # place UI elements
        bg_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        welcome_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
        stud_butt.place(relx=0.4, rely=0.55, anchor=tk.CENTER)
        play_butt.place(relx=0.6, rely=0.55, anchor=tk.CENTER)
        info_butt.place(relx=0.95, rely=0.05, anchor=tk.CENTER)

        window.mainloop()

# show the window
if __name__ == "__main__":
    app = StartApp()
    app.run()