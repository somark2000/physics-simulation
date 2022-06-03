# imports
import tkinter as tk
from theory.practice.three_body import ThreeBody as tb

global gapp


class ThreeBody:
    def __init__(self):
        self.hm_img = None
        self.bck_img = None
        self.second_frame = None
        self.y_scrollbar = None
        self.my_canvas = None
        self.sec = None
        self.main_frame = None
        self.window = None
        self.app = None
        self.practice = None

    def run(self, practice, app):
        self.practice = practice
        self.app = app
        global gapp
        gapp = app
        # setup for the UI window
        self.window = tk.Tk()
        self.window.configure(bg='#0e1c1d')
        self.window.geometry("1300x900")
        self.window.title("Course - Three-Body Problem")
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
        self.second_frame = tk.Frame(self.my_canvas)
        self.second_frame.configure(bg='#0e1c1d')
        welcome_label = tk.Label(self.second_frame, text="Three-Body Problem")
        welcome_label.configure(bg='#0e1c1d', font=("Arial", 28), fg='white', pady=20)
        t1 = """In classical mechanics, the three-body problem is a problem that involves determining the initial positions and moments of three-point masses and solving their subsequent motion according to Newton's laws of motion and Newton's law of universal gravitation. The three-body problem is a special case of the n-body problem, where, in contrast to the two-body problem, there are no there is a general closed solution. Because the resulting dynamical system is chaotic for most initial conditions, numerical methods are usually required to approximate the trajectory, despite some limited problems that are analytically solvable """
        p1 = tk.Label(self.second_frame, text=t1)
        t2 = """Not much was known about the n-body problem for n ≥ 3 in the past. Previous attempts to understand the three body problem were quantitative and aimed at finding explicit solutions for special situations. The case n = 3 has been studied the most because it is the easiest to develop"""
        p2 = tk.Label(self.second_frame, text=t2)
        t3 = """The N-body problem has the following assumptions:"""
        p3 = tk.Label(self.second_frame, text=t3)
        t4 = """• N-point particles in R3 with masses 𝑚𝑖 , 𝑖 = 1,N"""
        p4 = tk.Label(self.second_frame, text=t4)
        t5 = """• Between any two particles, an attractive force can be determined in the direction of the distance between the two particles"""
        p5 = tk.Label(self.second_frame, text=t5)
        t6 = """• At any given point in time, the displacement vector and its direction are given by all of these attractive forces, and all of their effects together determine the equation of motion for that infinite small time window 𝑑𝑡 → 0"""
        p6 = tk.Label(self.second_frame, text=t6)
        t7 = """In order to study a simpler application in real life, we will consider a heliocentric system, where the central mass will be stationary and the orbiting masses will have their own positions and momentums. Historically the first such problem to be studied was the Sun-Earth-Jupiter system. And now you are invited to try it out and run the simulation yourself"""
        p7 = tk.Label(self.second_frame, text=t7)

        p1.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50)
        p2.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50)
        p3.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50)
        p4.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50)
        p5.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50)
        p6.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50)
        p7.configure(bg='#0e1c1d', font=("Arial", 18), fg='white', wraplength=1100, padx=50)

        buttom = tk.Button(self.second_frame, text='Practice', command=lambda: self.do_practice())
        buttom.configure(bg='#0e1c1d', font=("Arial", 20), fg='white', pady=30, border=0)
        self.hm_img = tk.PhotoImage(file="images/home.png")
        self.bck_img = tk.PhotoImage(file="images/arrow_bck.png")
        back_butt = tk.Button(self.second_frame, image=self.bck_img, command=lambda: self.do_throwatangle(), bg='#0e1c1d',
                              fg='white', pady=30, border=0)
        home_butt = tk.Button(self.second_frame, image=self.hm_img, command=lambda: self.do_course(), bg='#0e1c1d',
                              fg='white', pady=30, border=0)
        preset_butt = tk.Button(self.second_frame, text='Presets', command=lambda: self.training())
        preset_butt.configure(bg='#0e1c1d', font=("Arial", 20), fg='white', pady=30, border=0)

        # pack all the UI elements to the frame
        welcome_label.grid(row=0, column=1, columnspan=2)
        home_butt.grid(row=0, column=4)
        back_butt.grid(row=0, column=0)
        p1.grid(row=1, column=1, columnspan=2)
        p2.grid(row=2, column=1, columnspan=2)
        p3.grid(row=3, column=1, columnspan=2)
        p4.grid(row=4, column=1, columnspan=2)
        p5.grid(row=5, column=1, columnspan=2)
        p6.grid(row=6, column=1, columnspan=2)
        p7.grid(row=7, column=1, columnspan=2)
        buttom.grid(row=8, column=1)
        preset_butt.grid(row=8, column=2)

        # Add that New Frame a Window In The Canvas
        self.my_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

        self.window.mainloop()

    def do_practice(self, m1=0.0, m2=0.0, mc=0.0, s1=4, s2=4, s3=4, v1=0.0, v2=0.0, r1=0.0, r2=0.0, p1=0, p2=0):
        freefall = tb()
        theory = ThreeBody()
        global gapp
        theory.app = gapp
        freefall.app = gapp
        freefall.practice = theory
        self.window.destroy()
        freefall.run(theory, gapp, m1, m2, mc, s1, s2, s3, v1, v2, r1, r2, p1, p2)

    def do_throwatangle(self):
        print(self.practice)
        if type(self.practice) is ThreeBody:
            global gapp
            gapp.do_courses(self.window)
        else:
            self.practice.do_throwatangle(window=self.window)

    def do_course(self):
        global gapp
        print(gapp)
        print(self.practice)
        gapp.do_courses(self.window)

    def training(self):
        b1 = tk.Button(self.second_frame, text='Sun, Earth, Mars',
                       command=lambda: self.do_practice(m1=5.9, m2=6.4, mc=2.1, s1=4, s2=3, s3=10, v1=29.8, v2=24.1, r1=1, r2=1.5))
        b2 = tk.Button(self.second_frame, text='Sun, Earth, Jupiter', command=lambda: self.do_practice(m1=5.9, m2=1.9, mc=2.1, s1=4, s2=7, s3=10, v1=29.8, v2=13.1, r1=1, r2=5.4))
        b3 = tk.Button(self.second_frame, text='Sun, Earth, Ceres', command=lambda: self.do_practice(m1=5.9, m2=9.1, mc=2.1, s1=4, s2=0, s3=10, v1=29.8, v2=17.9, r1=1, r2=2.8))
        b4 = tk.Button(self.second_frame, text='Sun, Earth, Super-Jupiter', command=lambda: self.do_practice(m1=5.9, m2=95, mc=2.1, s1=4, s2=8, s3=10, v1=29.8, v2=13.1, r1=1, r2=5.4))
        b5 = tk.Button(self.second_frame, text='Sun, Jupiter, Saturn', command=lambda: self.do_practice(m1=1.9, m2=5.6, mc=2.1, s1=7, s2=6, s3=10, v1=13.1, v2=9.7, r1=5.4, r2=9.5))
        b6 = tk.Button(self.second_frame, text='Betelgeuse, Earth, Jupiter', command=lambda: self.do_practice(m1=5.9, m2=1.9, mc=2.2, s1=4, s2=7, s3=11, v1=29.8, v2=13.1, r1=1, r2=5.4))

        b1.configure(bg='#0e1c1d', font=("Arial", 20), fg='white', pady=30, border=0)
        b2.configure(bg='#0e1c1d', font=("Arial", 20), fg='white', pady=30, border=0)
        b3.configure(bg='#0e1c1d', font=("Arial", 20), fg='white', pady=30, border=0)
        b4.configure(bg='#0e1c1d', font=("Arial", 20), fg='white', pady=30, border=0)
        b5.configure(bg='#0e1c1d', font=("Arial", 20), fg='white', pady=30, border=0)
        b6.configure(bg='#0e1c1d', font=("Arial", 20), fg='white', pady=30, border=0)

        b1.grid(row=9, column=1)
        b2.grid(row=9, column=2)
        b3.grid(row=10, column=1)
        b4.grid(row=10, column=2)
        b5.grid(row=11, column=1)
        b6.grid(row=11, column=2)
        self.y_scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.my_canvas.yview)
        # self.y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
