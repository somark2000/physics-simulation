# imports
import tkinter as tk
from motions.free_fall import FreeFall
from motions.vertical_throw_down import VerticalThrowDown
from motions.vertical_throw_up import VerticalThrowUp
from motions.throw_at_angle import ThrowAtAngle
from motions.three_body_UI import ThreeBody

global gapp

class PracticeWindow:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PracticeWindow, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.window = None
        self.app = None

    def run(self, app):
        # setup for the UI window
        self.app = app
        global gapp
        gapp = app
        self.window = tk.Tk()
        self.window.title("Practice")
        self.window.geometry('800x500')
        bg = tk.PhotoImage(file="images/bg.png")
        bg_label = tk.Label(self.window, image=bg)
        welcome_label = tk.Label(self.window, text="Practice")
        welcome_label.configure(bg='#0e1c1d', font=("Arial", 28), fg='white')

        p1_butt = tk.Button(text='Free fall', command=lambda: self.do_freefall(self.window))
        p1_butt.configure(bg='#0e1c1d', font=("Arial", 20), fg='white')
        p2_butt = tk.Button(text='Throw down', command=lambda: self.do_throwdown(self.window))
        p2_butt.configure(bg='#0e1c1d', font=("Arial", 20), fg='white')
        p3_butt = tk.Button(text='Throw up', command=lambda: self.do_throwup(self.window))
        p3_butt.configure(bg='#0e1c1d', font=("Arial", 20), fg='white')
        p4_butt = tk.Button(text='Throw at an angle', command=lambda: self.do_throwatangle(self.window))
        p4_butt.configure(bg='#0e1c1d', font=("Arial", 20), fg='white')
        p5_butt = tk.Button(text='Three Body Problem', command=lambda: self.do_threebody(self.window))
        p5_butt.configure(bg='#0e1c1d', font=("Arial", 20), fg='white')
        home = tk.PhotoImage(file="images/home.png")
        returned = tk.PhotoImage(file="images/exit.jpg")
        home_butt = tk.Button(bg='#0e1c1d', border=0)
        home_butt.configure(image=home, command=lambda: self.home(self.window))
        # if self.app != None:
        #     home_butt.configure(image=home, command=lambda: self.home(window))
        # else:
        #     home_butt.configure(image=returned, command=lambda: window.destroy())

        bg_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        welcome_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
        p1_butt.place(relx=0.35, rely=0.40, anchor=tk.CENTER)
        p2_butt.place(relx=0.65, rely=0.40, anchor=tk.CENTER)
        p3_butt.place(relx=0.35, rely=0.55, anchor=tk.CENTER)
        p4_butt.place(relx=0.65, rely=0.55, anchor=tk.CENTER)
        p5_butt.place(relx=0.5, rely=0.68, anchor=tk.CENTER)
        home_butt.place(relx=0.95, rely=0.05, anchor=tk.CENTER)

        self.window.mainloop()

    def do_freefall(self, window):
        global gapp
        freefall = FreeFall()
        practice = PracticeWindow()
        window.destroy()
        freefall.run(practice, gapp)

    def do_throwup(self, window):
        global gapp
        throwup = VerticalThrowUp()
        practice = PracticeWindow()
        window.destroy()
        throwup.run(practice, gapp)

    def do_throwdown(self, window):
        global gapp
        throwdown = VerticalThrowDown()
        practice = PracticeWindow()
        window.destroy()
        throwdown.run(practice, gapp)

    def do_throwatangle(self, window):
        global gapp
        throwangle = ThrowAtAngle()
        practice = PracticeWindow()
        window.destroy()
        throwangle.run(practice, gapp)

    def do_threebody(self, window):
        global gapp
        threebody = ThreeBody()
        practice = PracticeWindow()
        window.destroy()
        threebody.run(practice, gapp)

    def home(self, window):
        global gapp
        window.destroy()
        gapp.run()
