# imports
import tkinter as tk
from theory.practice.freefall import FreeFall as ff
global gapp


class FreeFall:
    def __init__(self):
        self.y_scrollbar = None
        self.my_canvas = None
        self.sec = None
        self.main_frame = None
        self.window = None
        self.app = None
        self.practice = None

    def run(self, practice, app):
        self.practice = practice
        global gapp
        gapp = app
        # setup for the UI window
        self.window = tk.Tk()
        self.window.configure(bg='#0e1c1d')
        self.window.geometry("1300x900")
        self.window.title("Course - Free Fall")
        # Create A Main frame
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        # Create Frame for X Scrollbar
        self.sec = tk.Frame(self.main_frame)
        self.sec.pack(fill=tk.X, side=tk.BOTTOM)

        # Create A Canvas
        self.my_canvas = tk.Canvas(self.main_frame)
        self.my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Add A Scrollbars to Canvas
        self.y_scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.my_canvas.yview)
        self.y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas
        self.my_canvas.configure(yscrollcommand=self.y_scrollbar.set)
        self.my_canvas.configure(bg='#0e1c1d')
        self.my_canvas.bind("<Configure>", lambda e: self.my_canvas.config(scrollregion=self.my_canvas.bbox(tk.ALL)))

        # Create Another Frame INSIDE the Canvas
        second_frame = tk.Frame(self.my_canvas)
        second_frame.configure(bg='#0e1c1d')
        welcome_label = tk.Label(second_frame, text="Free Fall")
        welcome_label.configure(bg='#0e1c1d', font=("Arial", 28), fg='white', pady=40)
        t1 = """Free fall is considered the simplest motion a projectile can make in an external gravitational field. 
        In this case it is assumed that the projectile in the initial time is at rest at the initial altitude 𝑦0 = 
        ℎ, so the initial velocity is considered to be zero 𝑣0 = 0 and the acceleration due to the downward 
        direction of the gravitational field of the earth is 𝑎 = −𝑔, as shown below. """
        p1 = tk.Label(second_frame, text=t1)
        t2 = """In this case, the equation of motion can be written as follows"""
        p2 = tk.Label(second_frame, text=t2)
        t3 = """Starting from the fact that speed is the first derivative of equation of motion, the velocity of the 
        bullet can be written as follows """
        p3 = tk.Label(second_frame, text=t3)
        t4 = """In this case the time dependencies of both the altitude and the speed of the projectile are shown 
        below """
        p4 = tk.Label(second_frame, text=t4)
        t5 = """For further practice click below"""
        p5 = tk.Label(second_frame, text=t5)

        p1.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50, pady=25)
        p2.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50, pady=25)
        p3.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50, pady=25)
        p4.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50, pady=25)
        p5.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50, pady=25)

        img1 = tk.PhotoImage(file="images/ff1.png")
        img1_lbl = tk.Label(second_frame, image=img1, pady=25)
        img2 = tk.PhotoImage(file="images/ff2.png")
        img2_lbl = tk.Label(second_frame, image=img2, pady=25)
        img3 = tk.PhotoImage(file="images/ff3.png")
        img3_lbl = tk.Label(second_frame, image=img3, pady=25)
        img4 = tk.PhotoImage(file="images/ff4.png")
        img4_lbl = tk.Label(second_frame, image=img4, pady=25)
        buttom = tk.Button(second_frame, text='Practice', command=self.do_practice)
        buttom.configure(bg='#0e1c1d', font=("Arial", 20), fg='white', pady=30, border=0)
        fw_img = tk.PhotoImage(file="images/arrow_fw.png")
        hm_img = tk.PhotoImage(file="images/home.png")
        forward_butt = tk.Button(second_frame, image=fw_img, command=lambda: self.do_throwup(),bg='#0e1c1d', fg='white', pady=30, border=0)
        home_butt = tk.Button(second_frame, image=hm_img, command=lambda: self.do_course(),bg='#0e1c1d', fg='white', pady=30, border=0)

        # pack all the UI elements to the frame
        welcome_label.grid(row=0, column=1)
        p1.grid(row=1, column=1, columnspan=3)
        img1_lbl.grid(row=2, column=1)
        p2.grid(row=3, column=1)
        img2_lbl.grid(row=4, column=1)
        p3.grid(row=5, column=1)
        img3_lbl.grid(row=6, column=1)
        p4.grid(row=7, column=1)
        img4_lbl.grid(row=8, column=1)
        p5.grid(row=9, column=1)
        buttom.grid(row=10, column=1)
        forward_butt.grid(row=0, column=2)
        home_butt.grid(row=0, column=0)

        # Add that New Frame a Window In The Canvas
        self.my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        self.window.mainloop()

    def do_practice(self):
        freefall = ff()
        theory = FreeFall()
        global gapp
        theory.app = gapp
        freefall.app = gapp
        freefall.practice = theory
        self.window.destroy()
        freefall.run(theory, gapp)

    def do_course(self):
        global gapp
        print(gapp)
        print(self.practice)
        gapp.do_courses(self.window)

    def do_throwup(self):
        if type(self.practice) is FreeFall:
            global gapp
            gapp.do_courses(self.window)
        else:
            self.practice.do_throwup(window=self.window)
